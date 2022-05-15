# -*- coding: utf-8 -*-

"""
***************************************************************************
    ImportIntoPostGIS.py
    ---------------------
    Date                 : October 2012
    Copyright            : (C) 2012 by Victor Olaya
    Email                : volayaf at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'October 2012'
__copyright__ = '(C) 2012, Victor Olaya'

from qgis.core import (QgsVectorLayerExporter,
                       QgsFeatureSink,
                       QgsProcessing,
                       QgsProcessingException,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterString,
                       QgsProcessingParameterField,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterProviderConnection,
                       QgsProcessingParameterDatabaseSchema,
                       QgsProcessingParameterDatabaseTable,
                       QgsWkbTypes,
                       QgsProviderRegistry,
                       QgsProviderConnectionException,
                       QgsDataSourceUri,
                       QgsAbstractDatabaseProviderConnection)

from processing.algs.qgis.QgisAlgorithm import QgisAlgorithm


class ImportIntoPostGIS(QgisAlgorithm):
    DATABASE = 'DATABASE'
    TABLENAME = 'TABLENAME'
    SCHEMA = 'SCHEMA'
    INPUT = 'INPUT'
    OVERWRITE = 'OVERWRITE'
    CREATEINDEX = 'CREATEINDEX'
    GEOMETRY_COLUMN = 'GEOMETRY_COLUMN'
    LOWERCASE_NAMES = 'LOWERCASE_NAMES'
    DROP_STRING_LENGTH = 'DROP_STRING_LENGTH'
    FORCE_SINGLEPART = 'FORCE_SINGLEPART'
    PRIMARY_KEY = 'PRIMARY_KEY'
    ENCODING = 'ENCODING'

    def group(self):
        return self.tr('Database')

    def groupId(self):
        return 'database'

    def __init__(self):
        super().__init__()

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSource(self.INPUT,
                                                              self.tr('Layer to import'),
                                                              types=[QgsProcessing.TypeVector]))

        db_param = QgsProcessingParameterProviderConnection(
            self.DATABASE,
            self.tr('Database (connection name)'), 'postgres'
        )
        self.addParameter(db_param)

        schema_param = QgsProcessingParameterDatabaseSchema(
            self.SCHEMA,
            self.tr('Schema (schema name)'), connectionParameterName=self.DATABASE, defaultValue='public', optional=True)
        self.addParameter(schema_param)

        table_param = QgsProcessingParameterDatabaseTable(
            self.TABLENAME,
            self.tr('Table to import to (leave blank to use layer name)'), defaultValue=None, connectionParameterName=self.DATABASE,
            schemaParameterName=self.SCHEMA, optional=True, allowNewTableNames=True)
        self.addParameter(table_param)

        self.addParameter(QgsProcessingParameterField(self.PRIMARY_KEY,
                                                      self.tr('Primary key field'), None, self.INPUT,
                                                      QgsProcessingParameterField.Any, False, True))
        self.addParameter(QgsProcessingParameterString(self.GEOMETRY_COLUMN,
                                                       self.tr('Geometry column'), 'geom'))
        self.addParameter(QgsProcessingParameterString(self.ENCODING,
                                                       self.tr('Encoding'), 'UTF-8',
                                                       False, True))
        self.addParameter(QgsProcessingParameterBoolean(self.OVERWRITE,
                                                        self.tr('Overwrite'), True))
        self.addParameter(QgsProcessingParameterBoolean(self.CREATEINDEX,
                                                        self.tr('Create spatial index'), True))
        self.addParameter(QgsProcessingParameterBoolean(self.LOWERCASE_NAMES,
                                                        self.tr('Convert field names to lowercase'), True))
        self.addParameter(QgsProcessingParameterBoolean(self.DROP_STRING_LENGTH,
                                                        self.tr('Drop length constraints on character fields'), False))
        self.addParameter(QgsProcessingParameterBoolean(self.FORCE_SINGLEPART,
                                                        self.tr('Create single-part geometries instead of multi-part'),
                                                        False))

    def name(self):
        return 'importintopostgis'

    def displayName(self):
        return self.tr('Export to PostgreSQL')

    def shortDescription(self):
        return self.tr('Exports a vector layer to a PostgreSQL database')

    def tags(self):
        return self.tr('import,postgis,table,layer,into,copy').split(',')

    def processAlgorithm(self, parameters, context, feedback):
        connection_name = self.parameterAsConnectionName(parameters, self.DATABASE, context)

        # resolve connection details to uri
        try:
            md = QgsProviderRegistry.instance().providerMetadata('postgres')
            conn = md.createConnection(connection_name)
        except QgsProviderConnectionException:
            raise QgsProcessingException(self.tr('Could not retrieve connection details for {}').format(connection_name))

        schema = self.parameterAsSchema(parameters, self.SCHEMA, context)
        overwrite = self.parameterAsBoolean(parameters, self.OVERWRITE, context)
        createIndex = self.parameterAsBoolean(parameters, self.CREATEINDEX, context)
        convertLowerCase = self.parameterAsBoolean(parameters, self.LOWERCASE_NAMES, context)
        dropStringLength = self.parameterAsBoolean(parameters, self.DROP_STRING_LENGTH, context)
        forceSinglePart = self.parameterAsBoolean(parameters, self.FORCE_SINGLEPART, context)
        primaryKeyField = self.parameterAsString(parameters, self.PRIMARY_KEY, context) or 'id'
        encoding = self.parameterAsString(parameters, self.ENCODING, context)

        source = self.parameterAsSource(parameters, self.INPUT, context)
        if source is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))

        table = self.parameterAsDatabaseTableName(parameters, self.TABLENAME, context)
        if table:
            table.strip()
        if not table or table == '':
            table = source.sourceName()
            table = table.replace('.', '_')
        table = table.replace(' ', '')[0:62]
        providerName = 'postgres'

        geomColumn = self.parameterAsString(parameters, self.GEOMETRY_COLUMN, context)
        if not geomColumn:
            geomColumn = 'geom'

        options = {}
        if overwrite:
            options['overwrite'] = True
        if convertLowerCase:
            options['lowercaseFieldNames'] = True
            geomColumn = geomColumn.lower()
        if dropStringLength:
            options['dropStringConstraints'] = True
        if forceSinglePart:
            options['forceSinglePartGeometryType'] = True

        # Clear geometry column for non-geometry tables
        if source.wkbType() == QgsWkbTypes.NoGeometry:
            geomColumn = None

        uri = QgsDataSourceUri(conn.uri())
        uri.setSchema(schema)
        uri.setTable(table)
        uri.setKeyColumn(primaryKeyField)
        uri.setGeometryColumn(geomColumn)

        if encoding:
            options['fileEncoding'] = encoding

        exporter = QgsVectorLayerExporter(uri.uri(), providerName, source.fields(),
                                          source.wkbType(), source.sourceCrs(), overwrite, options)

        if exporter.errorCode() != QgsVectorLayerExporter.NoError:
            raise QgsProcessingException(
                self.tr('Error importing to PostGIS\n{0}').format(exporter.errorMessage()))

        features = source.getFeatures()
        total = 100.0 / source.featureCount() if source.featureCount() else 0
        for current, f in enumerate(features):
            if feedback.isCanceled():
                break

            if not exporter.addFeature(f, QgsFeatureSink.FastInsert):
                feedback.reportError(exporter.errorMessage())

            feedback.setProgress(int(current * total))

        exporter.flushBuffer()
        if exporter.errorCode() != QgsVectorLayerExporter.NoError:
            raise QgsProcessingException(
                self.tr('Error importing to PostGIS\n{0}').format(exporter.errorMessage()))

        if geomColumn and createIndex:
            try:
                options = QgsAbstractDatabaseProviderConnection.SpatialIndexOptions()
                options.geometryColumnName = geomColumn
                conn.createSpatialIndex(schema, table, options)
            except QgsProviderConnectionException as e:
                raise QgsProcessingException(self.tr('Error creating spatial index:\n{0}').format(e))

        try:
            conn.vacuum(schema, table)
        except QgsProviderConnectionException as e:
            feedback.reportError(self.tr('Error vacuuming table:\n{0}').format(e))

        return {}
