# The PEP 484 type hints stub file for the _3d module.
#
# Generated by SIP 6.1.1


import typing

import PyQt5.sip

from PyQt5 import QtXml
from PyQt5 import QtGui
from PyQt5 import QtCore
from qgis import _core

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        PyQt5.sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], PyQt5.sip.Buffer, int, None]


class QgsMaterialSettingsRenderingTechnique(int):
    Triangles = ... # type: QgsMaterialSettingsRenderingTechnique
    Lines = ... # type: QgsMaterialSettingsRenderingTechnique
    InstancedPoints = ... # type: QgsMaterialSettingsRenderingTechnique
    Points = ... # type: QgsMaterialSettingsRenderingTechnique
    TrianglesWithFixedTexture = ... # type: QgsMaterialSettingsRenderingTechnique


class Qgs3DAlgorithms(_core.QgsProcessingProvider):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def loadAlgorithms(self) -> None: ...
    def supportsNonFileBasedOutput(self) -> bool: ...
    def name(self) -> str: ...
    def helpId(self) -> str: ...
    def id(self) -> str: ...
    def svgIconPath(self) -> str: ...
    def icon(self) -> QtGui.QIcon: ...


class Qgs3D(PyQt5.sip.wrapper):

    @staticmethod
    def materialRegistry() -> 'QgsMaterialRegistry': ...
    @staticmethod
    def initialize() -> None: ...
    @staticmethod
    def instance() -> 'Qgs3D': ...


class Qgs3DMapSettings(QtCore.QObject, _core.QgsTemporalRangeObject):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'Qgs3DMapSettings') -> None: ...

    def shadowSettingsChanged(self) -> None: ...
    def skyboxSettingsChanged(self) -> None: ...
    def fieldOfViewChanged(self) -> None: ...
    def directionalLightsChanged(self) -> None: ...
    def pointLightsChanged(self) -> None: ...
    def showLabelsChanged(self) -> None: ...
    def showLightSourceOriginsChanged(self) -> None: ...
    def showCameraViewCenterChanged(self) -> None: ...
    def showTerrainTilesInfoChanged(self) -> None: ...
    def showTerrainBoundingBoxesChanged(self) -> None: ...
    def renderersChanged(self) -> None: ...
    def terrainMapThemeChanged(self) -> None: ...
    def terrainShadingChanged(self) -> None: ...
    def maxTerrainGroundErrorChanged(self) -> None: ...
    def maxTerrainScreenErrorChanged(self) -> None: ...
    def mapTileResolutionChanged(self) -> None: ...
    def terrainVerticalScaleChanged(self) -> None: ...
    def terrainGeneratorChanged(self) -> None: ...
    def terrainLayersChanged(self) -> None: ...
    def layersChanged(self) -> None: ...
    def selectionColorChanged(self) -> None: ...
    def backgroundColorChanged(self) -> None: ...
    def setIsSkyboxEnabled(self, enabled: bool) -> None: ...
    def isSkyboxEnabled(self) -> bool: ...
    def outputDpi(self) -> float: ...
    def setOutputDpi(self, dpi: float) -> None: ...
    def setFieldOfView(self, fieldOfView: float) -> None: ...
    def fieldOfView(self) -> float: ...
    def setDirectionalLights(self, directionalLights: typing.Iterable['QgsDirectionalLightSettings']) -> None: ...
    def setPointLights(self, pointLights: typing.Iterable['QgsPointLightSettings']) -> None: ...
    def directionalLights(self) -> typing.List['QgsDirectionalLightSettings']: ...
    def pointLights(self) -> typing.List['QgsPointLightSettings']: ...
    def showLabels(self) -> bool: ...
    def setShowLabels(self, enabled: bool) -> None: ...
    def showLightSourceOrigins(self) -> bool: ...
    def setShowLightSourceOrigins(self, enabled: bool) -> None: ...
    def showCameraViewCenter(self) -> bool: ...
    def setShowCameraViewCenter(self, enabled: bool) -> None: ...
    def showTerrainTilesInfo(self) -> bool: ...
    def setShowTerrainTilesInfo(self, enabled: bool) -> None: ...
    def showTerrainBoundingBoxes(self) -> bool: ...
    def setShowTerrainBoundingBoxes(self, enabled: bool) -> None: ...
    def renderers(self) -> typing.List[_core.QgsAbstract3DRenderer]: ...
    def setRenderers(self, renderers: typing.Iterable[_core.QgsAbstract3DRenderer]) -> None: ...
    def terrainMapTheme(self) -> str: ...
    def setTerrainMapTheme(self, theme: str) -> None: ...
    def terrainShadingMaterial(self) -> 'QgsPhongMaterialSettings': ...
    def setTerrainShadingMaterial(self, material: 'QgsPhongMaterialSettings') -> None: ...
    def isTerrainShadingEnabled(self) -> bool: ...
    def setTerrainShadingEnabled(self, enabled: bool) -> None: ...
    def maxTerrainGroundError(self) -> float: ...
    def setMaxTerrainGroundError(self, error: float) -> None: ...
    def maxTerrainScreenError(self) -> float: ...
    def setMaxTerrainScreenError(self, error: float) -> None: ...
    def mapTileResolution(self) -> int: ...
    def setMapTileResolution(self, res: int) -> None: ...
    def terrainVerticalScale(self) -> float: ...
    def setTerrainVerticalScale(self, zScale: float) -> None: ...
    def terrainLayers(self) -> typing.List[_core.QgsMapLayer]: ...
    def setTerrainLayers(self, layers: typing.Iterable[_core.QgsMapLayer]) -> None: ...
    def layers(self) -> typing.List[_core.QgsMapLayer]: ...
    def setLayers(self, layers: typing.Iterable[_core.QgsMapLayer]) -> None: ...
    def selectionColor(self) -> QtGui.QColor: ...
    def setSelectionColor(self, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def backgroundColor(self) -> QtGui.QColor: ...
    def setBackgroundColor(self, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def setMapThemeCollection(self, mapThemes: _core.QgsMapThemeCollection) -> None: ...
    def mapThemeCollection(self) -> _core.QgsMapThemeCollection: ...
    def setPathResolver(self, resolver: _core.QgsPathResolver) -> None: ...
    def pathResolver(self) -> _core.QgsPathResolver: ...
    def setTransformContext(self, context: _core.QgsCoordinateTransformContext) -> None: ...
    def transformContext(self) -> _core.QgsCoordinateTransformContext: ...
    def crs(self) -> _core.QgsCoordinateReferenceSystem: ...
    def setCrs(self, crs: _core.QgsCoordinateReferenceSystem) -> None: ...
    def worldToMapCoordinates(self, worldCoords: _core.QgsVector3D) -> _core.QgsVector3D: ...
    def mapToWorldCoordinates(self, mapCoords: _core.QgsVector3D) -> _core.QgsVector3D: ...
    def origin(self) -> _core.QgsVector3D: ...
    def setOrigin(self, origin: _core.QgsVector3D) -> None: ...
    def resolveReferences(self, project: _core.QgsProject) -> None: ...
    def writeXml(self, doc: QtXml.QDomDocument, context: _core.QgsReadWriteContext) -> QtXml.QDomElement: ...
    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...


class Qgs3DTypes(PyQt5.sip.wrapper):

    class CullingMode(int):
        NoCulling = ... # type: Qgs3DTypes.CullingMode
        Front = ... # type: Qgs3DTypes.CullingMode
        Back = ... # type: Qgs3DTypes.CullingMode
        FrontAndBack = ... # type: Qgs3DTypes.CullingMode

    class AltitudeBinding(int):
        AltBindVertex = ... # type: Qgs3DTypes.AltitudeBinding
        AltBindCentroid = ... # type: Qgs3DTypes.AltitudeBinding

    class AltitudeClamping(int):
        AltClampAbsolute = ... # type: Qgs3DTypes.AltitudeClamping
        AltClampRelative = ... # type: Qgs3DTypes.AltitudeClamping
        AltClampTerrain = ... # type: Qgs3DTypes.AltitudeClamping

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'Qgs3DTypes') -> None: ...


class QgsVectorLayer3DTilingSettings(PyQt5.sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsVectorLayer3DTilingSettings') -> None: ...

    def readXml(self, elem: QtXml.QDomElement) -> None: ...
    def writeXml(self, elem: QtXml.QDomElement) -> None: ...
    def showBoundingBoxes(self) -> bool: ...
    def setShowBoundingBoxes(self, enabled: bool) -> None: ...
    def setZoomLevelsCount(self, count: int) -> None: ...
    def zoomLevelsCount(self) -> int: ...


class QgsAbstractVectorLayer3DRenderer(_core.QgsAbstract3DRenderer):

    def __init__(self) -> None: ...

    def readXmlBaseProperties(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def writeXmlBaseProperties(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def copyBaseProperties(self, r: 'QgsAbstractVectorLayer3DRenderer') -> None: ...
    def resolveReferences(self, project: _core.QgsProject) -> None: ...
    def tilingSettings(self) -> QgsVectorLayer3DTilingSettings: ...
    def setTilingSettings(self, settings: QgsVectorLayer3DTilingSettings) -> None: ...
    def layer(self) -> _core.QgsVectorLayer: ...
    def setLayer(self, layer: _core.QgsVectorLayer) -> None: ...


class QgsCameraPose(PyQt5.sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsCameraPose') -> None: ...

    def readXml(self, elem: QtXml.QDomElement) -> None: ...
    def writeXml(self, doc: QtXml.QDomDocument) -> QtXml.QDomElement: ...
    def setHeadingAngle(self, heading: float) -> None: ...
    def headingAngle(self) -> float: ...
    def setPitchAngle(self, pitch: float) -> None: ...
    def pitchAngle(self) -> float: ...
    def setDistanceFromCenterPoint(self, distance: float) -> None: ...
    def distanceFromCenterPoint(self) -> float: ...
    def setCenterPoint(self, point: _core.QgsVector3D) -> None: ...
    def centerPoint(self) -> _core.QgsVector3D: ...


class QgsLayoutItem3DMap(_core.QgsLayoutItem, _core.QgsTemporalRangeObject):

    def __init__(self, layout: _core.QgsLayout) -> None: ...

    def readPropertiesFromElement(self, element: QtXml.QDomElement, document: QtXml.QDomDocument, context: _core.QgsReadWriteContext) -> bool: ...
    def writePropertiesToElement(self, element: QtXml.QDomElement, document: QtXml.QDomDocument, context: _core.QgsReadWriteContext) -> bool: ...
    def draw(self, context: _core.QgsLayoutItemRenderContext) -> None: ...
    def refresh(self) -> None: ...
    def finalizeRestoreFromXml(self) -> None: ...
    def displayName(self) -> str: ...
    def assignFreeId(self) -> None: ...
    def mapSettings(self) -> Qgs3DMapSettings: ...
    def setMapSettings(self, settings: Qgs3DMapSettings) -> None: ...
    def cameraPose(self) -> QgsCameraPose: ...
    def setCameraPose(self, pose: QgsCameraPose) -> None: ...
    def icon(self) -> QtGui.QIcon: ...
    def type(self) -> int: ...
    @staticmethod
    def create(layout: _core.QgsLayout) -> 'QgsLayoutItem3DMap': ...


class QgsPointLightSettings(PyQt5.sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsPointLightSettings') -> None: ...

    def readXml(self, elem: QtXml.QDomElement) -> None: ...
    def writeXml(self, doc: QtXml.QDomDocument) -> QtXml.QDomElement: ...
    def setQuadraticAttenuation(self, value: float) -> None: ...
    def quadraticAttenuation(self) -> float: ...
    def setLinearAttenuation(self, value: float) -> None: ...
    def linearAttenuation(self) -> float: ...
    def setConstantAttenuation(self, value: float) -> None: ...
    def constantAttenuation(self) -> float: ...
    def setIntensity(self, intensity: float) -> None: ...
    def intensity(self) -> float: ...
    def setColor(self, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def color(self) -> QtGui.QColor: ...
    def setPosition(self, pos: _core.QgsVector3D) -> None: ...
    def position(self) -> _core.QgsVector3D: ...


class QgsDirectionalLightSettings(PyQt5.sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsDirectionalLightSettings') -> None: ...

    def readXml(self, elem: QtXml.QDomElement) -> None: ...
    def writeXml(self, doc: QtXml.QDomDocument) -> QtXml.QDomElement: ...
    def setIntensity(self, intensity: float) -> None: ...
    def intensity(self) -> float: ...
    def setColor(self, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def color(self) -> QtGui.QColor: ...
    def setDirection(self, direction: _core.QgsVector3D) -> None: ...
    def direction(self) -> _core.QgsVector3D: ...


class QgsRuleBased3DRendererMetadata(_core.Qgs3DRendererAbstractMetadata):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsRuleBased3DRendererMetadata') -> None: ...

    def createRenderer(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> _core.QgsAbstract3DRenderer: ...


class QgsRuleBased3DRenderer(QgsAbstractVectorLayer3DRenderer):

    class Rule(PyQt5.sip.wrapper):

        class RegisterResult(int):
            Filtered = ... # type: QgsRuleBased3DRenderer.Rule.RegisterResult
            Inactive = ... # type: QgsRuleBased3DRenderer.Rule.RegisterResult
            Registered = ... # type: QgsRuleBased3DRenderer.Rule.RegisterResult

        def __init__(self, symbol: _core.QgsAbstract3DSymbol, filterExp: str = ..., description: str = ..., elseRule: bool = ...) -> None: ...

        def save(self, doc: QtXml.QDomDocument, context: _core.QgsReadWriteContext) -> QtXml.QDomElement: ...
        @staticmethod
        def create(ruleElem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> 'QgsRuleBased3DRenderer.Rule': ...
        def clone(self) -> 'QgsRuleBased3DRenderer.Rule': ...
        def findRuleByKey(self, key: str) -> 'QgsRuleBased3DRenderer.Rule': ...
        def removeChildAt(self, i: int) -> None: ...
        def insertChild(self, i: int, rule: 'QgsRuleBased3DRenderer.Rule') -> None: ...
        def appendChild(self, rule: 'QgsRuleBased3DRenderer.Rule') -> None: ...
        def parent(self) -> 'QgsRuleBased3DRenderer.Rule': ...
        def descendants(self) -> typing.List['QgsRuleBased3DRenderer.Rule']: ...
        def children(self) -> typing.List['QgsRuleBased3DRenderer.Rule']: ...
        def setRuleKey(self, key: str) -> None: ...
        def setIsElse(self, iselse: bool) -> None: ...
        def setActive(self, state: bool) -> None: ...
        def setDescription(self, description: str) -> None: ...
        def setFilterExpression(self, filterExp: str) -> None: ...
        def setSymbol(self, symbol: _core.QgsAbstract3DSymbol) -> None: ...
        def ruleKey(self) -> str: ...
        def isElse(self) -> bool: ...
        def active(self) -> bool: ...
        def description(self) -> str: ...
        def filterExpression(self) -> str: ...
        def symbol(self) -> _core.QgsAbstract3DSymbol: ...

    def __init__(self, root: 'QgsRuleBased3DRenderer.Rule') -> None: ...

    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def writeXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def clone(self) -> 'QgsRuleBased3DRenderer': ...
    def type(self) -> str: ...
    def rootRule(self) -> 'QgsRuleBased3DRenderer.Rule': ...


class QgsVectorLayer3DRendererMetadata(_core.Qgs3DRendererAbstractMetadata):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsVectorLayer3DRendererMetadata') -> None: ...

    def createRenderer(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> _core.QgsAbstract3DRenderer: ...


class QgsVectorLayer3DRenderer(QgsAbstractVectorLayer3DRenderer):

    def __init__(self, s: typing.Optional[_core.QgsAbstract3DSymbol] = ...) -> None: ...

    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def writeXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def clone(self) -> 'QgsVectorLayer3DRenderer': ...
    def type(self) -> str: ...
    def symbol(self) -> _core.QgsAbstract3DSymbol: ...
    def setSymbol(self, symbol: _core.QgsAbstract3DSymbol) -> None: ...


class QgsMaterialContext(PyQt5.sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsMaterialContext') -> None: ...

    def setSelectionColor(self, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def selectionColor(self) -> QtGui.QColor: ...
    def setIsSelected(self, isSelected: bool) -> None: ...
    def isSelected(self) -> bool: ...


class QgsAbstractMaterialSettings(PyQt5.sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsAbstractMaterialSettings') -> None: ...

    def writeXml(self, element: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def readXml(self, element: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def clone(self) -> 'QgsAbstractMaterialSettings': ...
    def type(self) -> str: ...


class QgsGoochMaterialSettings(QgsAbstractMaterialSettings):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsGoochMaterialSettings') -> None: ...

    def toExportParameters(self) -> typing.Dict[str, str]: ...
    def writeXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def setBeta(self, beta: float) -> None: ...
    def setAlpha(self, alpha: float) -> None: ...
    def setShininess(self, shininess: float) -> None: ...
    def setSpecular(self, specular: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def setDiffuse(self, diffuse: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def setCool(self, cool: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def setWarm(self, warm: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def beta(self) -> float: ...
    def alpha(self) -> float: ...
    def shininess(self) -> float: ...
    def specular(self) -> QtGui.QColor: ...
    def diffuse(self) -> QtGui.QColor: ...
    def cool(self) -> QtGui.QColor: ...
    def warm(self) -> QtGui.QColor: ...
    def clone(self) -> 'QgsGoochMaterialSettings': ...
    @staticmethod
    def supportsTechnique(technique: QgsMaterialSettingsRenderingTechnique) -> bool: ...
    @staticmethod
    def create() -> QgsAbstractMaterialSettings: ...
    def type(self) -> str: ...


class QgsMaterialSettingsAbstractMetadata(PyQt5.sip.wrapper):

    @typing.overload
    def __init__(self, type: str, visibleName: str, icon: QtGui.QIcon = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsMaterialSettingsAbstractMetadata') -> None: ...

    def supportsTechnique(self, technique: QgsMaterialSettingsRenderingTechnique) -> bool: ...
    def create(self) -> QgsAbstractMaterialSettings: ...
    def icon(self) -> QtGui.QIcon: ...
    def visibleName(self) -> str: ...
    def type(self) -> str: ...


class QgsMaterialRegistry(PyQt5.sip.wrapper):

    def __init__(self) -> None: ...

    def createMaterialSettings(self, type: str) -> QgsAbstractMaterialSettings: ...
    def addMaterialSettingsType(self, metadata: QgsMaterialSettingsAbstractMetadata) -> bool: ...
    def materialSettingsTypes(self) -> typing.List[str]: ...
    def materialSettingsMetadata(self, type: str) -> QgsMaterialSettingsAbstractMetadata: ...


class QgsPhongMaterialSettings(QgsAbstractMaterialSettings):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsPhongMaterialSettings') -> None: ...

    def writeXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def setShininess(self, shininess: float) -> None: ...
    def setSpecular(self, specular: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def setDiffuse(self, diffuse: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def setAmbient(self, ambient: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def toExportParameters(self) -> typing.Dict[str, str]: ...
    def shininess(self) -> float: ...
    def specular(self) -> QtGui.QColor: ...
    def diffuse(self) -> QtGui.QColor: ...
    def ambient(self) -> QtGui.QColor: ...
    def clone(self) -> 'QgsPhongMaterialSettings': ...
    @staticmethod
    def create() -> QgsAbstractMaterialSettings: ...
    @staticmethod
    def supportsTechnique(technique: QgsMaterialSettingsRenderingTechnique) -> bool: ...
    def type(self) -> str: ...


class QgsPhongTexturedMaterialSettings(QgsAbstractMaterialSettings):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsPhongTexturedMaterialSettings') -> None: ...

    def writeXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def setTextureRotation(self, rotation: float) -> None: ...
    def setTextureScale(self, scale: float) -> None: ...
    def setDiffuseTexturePath(self, path: str) -> None: ...
    def setShininess(self, shininess: float) -> None: ...
    def setSpecular(self, specular: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def setAmbient(self, ambient: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def textureRotation(self) -> float: ...
    def requiresTextureCoordinates(self) -> bool: ...
    def textureScale(self) -> float: ...
    def diffuseTexturePath(self) -> str: ...
    def toExportParameters(self) -> typing.Dict[str, str]: ...
    def shininess(self) -> float: ...
    def specular(self) -> QtGui.QColor: ...
    def ambient(self) -> QtGui.QColor: ...
    def clone(self) -> 'QgsPhongTexturedMaterialSettings': ...
    @staticmethod
    def create() -> QgsAbstractMaterialSettings: ...
    @staticmethod
    def supportsTechnique(technique: QgsMaterialSettingsRenderingTechnique) -> bool: ...
    def type(self) -> str: ...


class QgsSimpleLineMaterialSettings(QgsAbstractMaterialSettings):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QgsSimpleLineMaterialSettings') -> None: ...

    def writeXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def toExportParameters(self) -> typing.Dict[str, str]: ...
    def setAmbient(self, ambient: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def ambient(self) -> QtGui.QColor: ...
    def clone(self) -> 'QgsSimpleLineMaterialSettings': ...
    @staticmethod
    def create() -> QgsAbstractMaterialSettings: ...
    @staticmethod
    def supportsTechnique(technique: QgsMaterialSettingsRenderingTechnique) -> bool: ...
    def type(self) -> str: ...


class QgsLine3DSymbol(_core.QgsAbstract3DSymbol):

    def __init__(self) -> None: ...

    def setMaterial(self, material: QgsAbstractMaterialSettings) -> None: ...
    def material(self) -> QgsAbstractMaterialSettings: ...
    def setRenderAsSimpleLines(self, enabled: bool) -> None: ...
    def renderAsSimpleLines(self) -> bool: ...
    def setExtrusionHeight(self, extrusionHeight: float) -> None: ...
    def extrusionHeight(self) -> float: ...
    def setHeight(self, height: float) -> None: ...
    def height(self) -> float: ...
    def setWidth(self, width: float) -> None: ...
    def width(self) -> float: ...
    def setAltitudeBinding(self, altBinding: Qgs3DTypes.AltitudeBinding) -> None: ...
    def altitudeBinding(self) -> Qgs3DTypes.AltitudeBinding: ...
    def setAltitudeClamping(self, altClamping: Qgs3DTypes.AltitudeClamping) -> None: ...
    def altitudeClamping(self) -> Qgs3DTypes.AltitudeClamping: ...
    def compatibleGeometryTypes(self) -> typing.Any: ...
    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def writeXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def clone(self) -> _core.QgsAbstract3DSymbol: ...
    def type(self) -> str: ...
    @staticmethod
    def create() -> _core.QgsAbstract3DSymbol: ...


class QgsPoint3DSymbol(_core.QgsAbstract3DSymbol):

    class Shape(int):
        Cylinder = ... # type: QgsPoint3DSymbol.Shape
        Sphere = ... # type: QgsPoint3DSymbol.Shape
        Cone = ... # type: QgsPoint3DSymbol.Shape
        Cube = ... # type: QgsPoint3DSymbol.Shape
        Torus = ... # type: QgsPoint3DSymbol.Shape
        Plane = ... # type: QgsPoint3DSymbol.Shape
        ExtrudedText = ... # type: QgsPoint3DSymbol.Shape
        Model = ... # type: QgsPoint3DSymbol.Shape
        Billboard = ... # type: QgsPoint3DSymbol.Shape

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QgsPoint3DSymbol') -> None: ...

    def billboardTransform(self) -> QtGui.QMatrix4x4: ...
    def setTransform(self, transform: QtGui.QMatrix4x4) -> None: ...
    def transform(self) -> QtGui.QMatrix4x4: ...
    def setBillboardSymbol(self, symbol: _core.QgsMarkerSymbol) -> None: ...
    def billboardSymbol(self) -> _core.QgsMarkerSymbol: ...
    def setShapeProperties(self, properties: typing.Dict[str, typing.Any]) -> None: ...
    def shapeProperties(self) -> typing.Dict[str, typing.Any]: ...
    def setShape(self, shape: 'QgsPoint3DSymbol.Shape') -> None: ...
    def shape(self) -> 'QgsPoint3DSymbol.Shape': ...
    @staticmethod
    def shapeToString(shape: 'QgsPoint3DSymbol.Shape') -> str: ...
    @staticmethod
    def shapeFromString(shape: str) -> 'QgsPoint3DSymbol.Shape': ...
    def setMaterial(self, material: QgsAbstractMaterialSettings) -> None: ...
    def material(self) -> QgsAbstractMaterialSettings: ...
    def setAltitudeClamping(self, altClamping: Qgs3DTypes.AltitudeClamping) -> None: ...
    def altitudeClamping(self) -> Qgs3DTypes.AltitudeClamping: ...
    def compatibleGeometryTypes(self) -> typing.Any: ...
    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def writeXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def clone(self) -> _core.QgsAbstract3DSymbol: ...
    def type(self) -> str: ...
    @staticmethod
    def create() -> _core.QgsAbstract3DSymbol: ...


class QgsPolygon3DSymbol(_core.QgsAbstract3DSymbol):

    def __init__(self) -> None: ...

    def renderedFacade(self) -> int: ...
    def setRenderedFacade(self, side: int) -> None: ...
    def setEdgeColor(self, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def edgeColor(self) -> QtGui.QColor: ...
    def setEdgeWidth(self, width: float) -> None: ...
    def edgeWidth(self) -> float: ...
    def setEdgesEnabled(self, enabled: bool) -> None: ...
    def edgesEnabled(self) -> bool: ...
    def setAddBackFaces(self, add: bool) -> None: ...
    def addBackFaces(self) -> bool: ...
    def setInvertNormals(self, invert: bool) -> None: ...
    def invertNormals(self) -> bool: ...
    def setCullingMode(self, mode: Qgs3DTypes.CullingMode) -> None: ...
    def cullingMode(self) -> Qgs3DTypes.CullingMode: ...
    def setMaterial(self, material: QgsAbstractMaterialSettings) -> None: ...
    def material(self) -> QgsAbstractMaterialSettings: ...
    def setExtrusionHeight(self, extrusionHeight: float) -> None: ...
    def extrusionHeight(self) -> float: ...
    def setHeight(self, height: float) -> None: ...
    def height(self) -> float: ...
    def setAltitudeBinding(self, altBinding: Qgs3DTypes.AltitudeBinding) -> None: ...
    def altitudeBinding(self) -> Qgs3DTypes.AltitudeBinding: ...
    def setAltitudeClamping(self, altClamping: Qgs3DTypes.AltitudeClamping) -> None: ...
    def altitudeClamping(self) -> Qgs3DTypes.AltitudeClamping: ...
    @staticmethod
    def create() -> _core.QgsAbstract3DSymbol: ...
    def compatibleGeometryTypes(self) -> typing.Any: ...
    def readXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def writeXml(self, elem: QtXml.QDomElement, context: _core.QgsReadWriteContext) -> None: ...
    def clone(self) -> _core.QgsAbstract3DSymbol: ...
    def type(self) -> str: ...


class Qgs3DMapExportSettings(PyQt5.sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'Qgs3DMapExportSettings') -> None: ...

    def setScale(self, scale: float) -> None: ...
    def setTerrainTextureResolution(self, resolution: int) -> None: ...
    def setExportTextures(self, exportTextures: bool) -> None: ...
    def setExportNormals(self, exportNormals: bool) -> None: ...
    def setSmoothEdges(self, smoothEdges: bool) -> None: ...
    def setTerrainResolution(self, resolution: int) -> None: ...
    def setSceneFolderPath(self, sceneFolderPath: str) -> None: ...
    def setSceneName(self, sceneName: str) -> None: ...
    def scale(self) -> float: ...
    def terrainTextureResolution(self) -> int: ...
    def exportTextures(self) -> bool: ...
    def exportNormals(self) -> bool: ...
    def smoothEdges(self) -> bool: ...
    def terrrainResolution(self) -> int: ...
    def sceneFolderPath(self) -> str: ...
    def sceneName(self) -> str: ...
