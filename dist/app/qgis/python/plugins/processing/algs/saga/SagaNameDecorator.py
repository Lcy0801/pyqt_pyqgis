# -*- coding: utf-8 -*-

groups = {
'climate_tools': 'Climate and Weather - Climate and Weather Tools',
'contrib_perego': 'Raster - Filter (Perego 2009)',
'grid_analysis': 'Raster - Analysis',
'grid_calculus': 'Raster - Calculus',
'grid_filter': 'Raster - Filter',
'grid_gridding': 'Raster - Rasterizing',
'grid_spline': 'Raster - Spline Interpolation',
'grid_tools': 'Raster - Tools',
'imagery_classification': 'Imagery - Classification',
'imagery_isocluster': 'Imagery - ISODATA Clustering',
'imagery_maxent': 'Imagery - Maximum Entropy',
'imagery_segmentation': 'Imagery - Segmentation',
'imagery_svm': 'Imagery - SVM',
'imagery_tools': 'Imagery - Tools',
'io_gdal': 'Import/Export - GDAL/OGR',
'io_gps': 'Import/Export - GPS Tools',
'io_grid': 'Import/Export - Rasters',
'io_grid_image': 'Import/Export - Images',
'io_shapes': 'Import/Export - Features',
'io_shapes_dxf': 'Import/Export - DXF',
'io_table': 'Import/Export - Tables',
'io_virtual': 'Import/Export - Virtual',
'io_webservices': 'Import/Export - Web Services',
'pj_georeference': 'Projection - Georeferencing',
'pj_proj4': 'Projection - Proj.4',
'shapes_grid': 'Features - Features-Raster Tools',
'shapes_lines': 'Features - Lines',
'shapes_points': 'Features - Points',
'shapes_polygons': 'Features - Polygons',
'shapes_tools': 'Features - Tools',
'shapes_transect': 'Features - Transects',
'sim_air_flow': 'Simulation - Air Flow Simulations',
'sim_cellular_automata': 'Simulation - Cellular Automata',
'sim_ecosystems_hugget': 'Simulation - Modelling the Human Impact on Nature',
'sim_erosion': 'Simulation - Erosion',
'sim_fire_spreading': 'Simulation - Fire Spreading Analysis',
'sim_geomorphology': 'Simulation - Geomorphology',
'sim_hydrology': 'Simulation - Hydrology',
'sim_landscape_evolution': 'Simulation - Landscape Evolution',
'sim_qm_of_esp': 'Simulation - QM of ESP',
'sim_rivflow': 'Simulation - RivFlow',
'statistics_grid': 'Spatial and Geostatistics - Rasters',
'statistics_kriging': 'Spatial and Geostatistics - Kriging',
'statistics_points': 'Spatial and Geostatistics - Points',
'statistics_regression': 'Spatial and Geostatistics - Regression',
'ta_channels': 'Terrain Analysis - Channels',
'ta_cliffmetrics': 'Terrain Analysis - CliffMetrics',
'ta_compound': 'Terrain Analysis - Compound Analyses',
'ta_hydrology': 'Terrain Analysis - Hydrology',
'ta_lighting': 'Terrain Analysis - Lighting, Visibility',
'ta_morphometry': 'Terrain Analysis - Morphometry',
'ta_preprocessor': 'Terrain Analysis - Preprocessing',
'ta_profiles': 'Terrain Analysis - Profiles',
'ta_slope_stability': 'Terrain Analysis - Slope Stability',
'toolchains_terrain_analysis': 'Tool Chains - Terrain Analysis',
'toolchains_toolchains': 'Tool Chains - Tool Chains',
'toolchains_grid_filter': 'Tool Chains - Raster Filters',
'toolchains_grid_tools': 'Tool Chains - Raster Tools',
'toolchains_imagery': 'Tool Chains - Imagery',
'toolchains_group_files': 'Tool Chains - Files',
'toolchains_polygon_tools': 'Tool Chains - Polygon Tools',
'toolchains_shapes_tools': 'Tool Chains - Features Tools',
'toolchains_climate_tools': 'Tool Chains - Climate and Weather Tools',
'toolchains_tta_tools': 'Tool Chains - Travel Time Analysis'}

def decoratedGroupName(name):
	return groups.get(name, name)

algorithms = {
'Earth''s Orbital Parameters': 'Earth''s Orbital Parameters',
'Annual Course of Daily Insolation': 'Annual Course of Daily Insolation',
'Daily Insolation over Latitude': 'Daily Insolation over Latitude',
'Monthly Global by Latitude': 'Monthly Global by Latitude',
'Evapotranspiration (Table)': 'Evapotranspiration (Table)',
'Daily to Hourly Evapotranspiration': 'Daily to Hourly Evapotranspiration',
'Evapotranspiration (Grid)': 'Evapotranspiration (Raster)',
'Sunrise and Sunset': 'Sunrise and Sunset',
'Bioclimatic Variables': 'Bioclimatic Variables',
'Tree Growth Season': 'Tree Growth Season',
'Wind Effect Correction': 'Wind Effect Correction',
'Frost Change Frequency': 'Frost Change Frequency',
'Thermic Belt Classification': 'Thermic Belt Classification',
'Snow Cover': 'Snow Cover',
'Growing Degree Days': 'Growing Degree Days',
'Climate Classification': 'Climate Classification',
'PhenIps (Table)': 'PhenIps (Table)',
'PhenIps (Grids, Annual)': 'PhenIps (Rasters, Annual)',
'PhenIps (Grids, Days)': 'PhenIps (Rasters, Days)',
'Soil Water Balance (Days)': 'Soil Water Balance (Days)',
'Cloud Overlap': 'Cloud Overlap',
'Temperature Lapse Rates': 'Temperature Lapse Rates',
'Air Pressure Adjustment': 'Air Pressure Adjustment',
'Land Surface Temperature': 'Land Surface Temperature',
'Average With Thereshold 1': 'Average With Thereshold 1',
'Average With Thereshold 2': 'Average With Thereshold 2',
'Average With Thereshold 3': 'Average With Thereshold 3',
'Average With Mask 1': 'Average With Mask 1',
'Average With Mask 2': 'Average With Mask 2',
'Destriping': 'Destriping',
'Destriping with Mask': 'Destriping with Mask',
'Directional Average': 'Directional Average',
'Accumulated Cost': 'Accumulated Cost',
'Least Cost Paths': 'Least Cost Paths',
'Covered Distance': 'Covered Distance',
'Pattern Analysis': 'Pattern Analysis',
'Layer of extreme value': 'Layer of extreme value',
'Analytical Hierarchy Process': 'Analytical Hierarchy Process',
'Aggregation Index': 'Aggregation Index',
'Cross-Classification and Tabulation': 'Cross-Classification and Tabulation',
'Fragmentation (Standard)': 'Fragmentation (Standard)',
'Fragmentation (Alternative)': 'Fragmentation (Alternative)',
'Fragmentation Classes from Density and Connectivity': 'Fragmentation Classes from Density and Connectivity',
'Accumulation Functions': 'Accumulation Functions',
'IMCORR - Feature Tracking': 'IMCORR - Feature Tracking',
'Diversity of Categories': 'Diversity of Categories',
'Shannon Index': 'Shannon Index',
'Simpson Index': 'Simpson Index',
'Rao''s Q Diversity Index (Classic)': 'Rao''s Q Diversity Index (Classic)',
'Rao''s Q Diversity Index': 'Rao''s Q Diversity Index',
'Coverage of Categories': 'Coverage of Categories',
'Grid Normalization': 'Raster Normalization',
'Grid Calculator': 'Raster Calculator',
'Grid Volume': 'Raster Volume',
'Grid Difference': 'Raster Difference',
'Function Plotter': 'Function Plotter',
'Geometric Figures': 'Geometric Figures',
'Random Terrain': 'Random Terrain',
'Random Field': 'Random Field',
'Grids Sum': 'Rasters Sum',
'Grids Product': 'Rasters Product',
'Grid Standardization': 'Raster Standardization',
'Fuzzify': 'Fuzzify',
'Fuzzy Intersection (AND)': 'Fuzzy Intersection (AND)',
'Fuzzy Union (OR)': 'Fuzzy Union (OR)',
'Metric Conversions': 'Metric Conversions',
'Gradient Vector from Cartesian to Polar Coordinates': 'Gradient Vector from Cartesian to Polar Coordinates',
'Gradient Vector from Polar to Cartesian Coordinates': 'Gradient Vector from Polar to Cartesian Coordinates',
'Fractal Brownian Noise': 'Fractal Brownian Noise',
'Grid Division': 'Raster Division',
'Histogram Matching': 'Histogram Matching',
'Simple Filter': 'Simple Filter',
'Gaussian Filter': 'Gaussian Filter',
'Laplacian Filter': 'Laplacian Filter',
'Multi Direction Lee Filter': 'Multi Direction Lee Filter',
'Filter Clumps': 'Filter Clumps',
'Majority/Minority Filter': 'Majority/Minority Filter',
'DTM Filter (slope-based)': 'DTM Filter (slope-based)',
'Morphological Filter': 'Morphological Filter',
'Rank Filter': 'Rank Filter',
'Mesh Denoise': 'Mesh Denoise',
'Resampling Filter': 'Resampling Filter',
'Geodesic Morphological Reconstruction': 'Geodesic Morphological Reconstruction',
'Binary Erosion-Reconstruction': 'Binary Erosion-Reconstruction',
'Connectivity Analysis': 'Connectivity Analysis',
'Sieve Classes': 'Sieve Classes',
'Wombling (Edge Detection)': 'Wombling (Edge Detection)',
'Wombling for Multiple Features (Edge Detection)': 'Wombling for Multiple Features (Edge Detection)',
'Simple Filter (Restricted to Polygons)': 'Simple Filter (Restricted to Polygons)',
'Shapes to Grid': 'Features to Raster',
'Inverse Distance Weighted': 'Inverse Distance Weighted',
'Nearest Neighbour': 'Nearest Neighbour',
'Natural Neighbour': 'Natural Neighbour',
'Modifed Quadratic Shepard': 'Modifed Quadratic Shepard',
'Triangulation': 'Triangulation',
'Kernel Density Estimation': 'Kernel Density Estimation',
'Angular Distance Weighted': 'Angular Distance Weighted',
'Grid Cell Area Covered by Polygons': 'Raster Cell Area Covered by Polygons',
'Polygons to Grid': 'Polygons to Raster',
'Polygon Categories to Grid': 'Polygon Categories to Raster',
'Thin Plate Spline': 'Thin Plate Spline',
'Thin Plate Spline (TIN)': 'Thin Plate Spline (TIN)',
'B-Spline Approximation': 'B-Spline Approximation',
'Multilevel B-Spline': 'Multilevel B-Spline',
'Multilevel B-Spline from Grid Points': 'Multilevel B-Spline from Raster Points',
'Cubic Spline Approximation': 'Cubic Spline Approximation',
'Multilevel B-Spline for Categories': 'Multilevel B-Spline for Categories',
'Resampling': 'Resampling',
'Mosaicking': 'Mosaicking',
'Constant Grid': 'Constant Raster',
'Patching': 'Patching',
'Close One Cell Gaps': 'Close One Cell Gaps',
'Close Gaps': 'Close Gaps',
'Grid Buffer': 'Raster Buffer',
'Threshold Buffer': 'Threshold Buffer',
'Grid Proximity Buffer': 'Raster Proximity Buffer',
'Change Data Storage': 'Change Data Storage',
'Crop to Data': 'Crop to Data',
'Invert Data/No-Data': 'Invert Data/No-Data',
'Grid Cell Index': 'Raster Cell Index',
'Grids from classified grid and table': 'Rasters from classified grid and table',
'Grid Masking': 'Raster Masking',
'Close Gaps with Spline': 'Close Gaps with Spline',
'Proximity Grid': 'Proximity Raster',
'Tiling': 'Tiling',
'Shrink and Expand': 'Shrink and Expand',
'Close Gaps with Stepwise Resampling': 'Close Gaps with Stepwise Resampling',
'Transpose Grids': 'Transpose Rasters',
'Clip Grids': 'Clip Rasters',
'Select Grid from List': 'Select Raster from List',
'Copy Grid': 'Copy Raster',
'Invert Grid': 'Invert Raster',
'Mirror Grid': 'Mirror Raster',
'Change a Grid''s No-Data Value': 'Change a Raster''s No-Data Value',
'Combine Classes': 'Combine Classes',
'Change Grid Values - Flood Fill': 'Change Raster Values - Flood Fill',
'Supervised Classification for Grids': 'Supervised Classification for Rasters',
'K-Means Clustering for Grids': 'K-Means Clustering for Rasters',
'Confusion Matrix (Two Grids)': 'Confusion Matrix (Two Rasters)',
'Decision Tree': 'Decision Tree',
'Confusion Matrix (Polygons / Grid)': 'Confusion Matrix (Polygons / Raster)',
'ISODATA Clustering for Grids': 'ISODATA Clustering for Rasters',
'Maximum Entropy Classifcation': 'Maximum Entropy Classifcation',
'Maximum Entropy Presence Prediction': 'Maximum Entropy Presence Prediction',
'Grid Skeletonization': 'Raster Skeletonization',
'Seed Generation': 'Seed Generation',
'Seeded Region Growing': 'Seeded Region Growing',
'Superpixel Segmentation': 'Superpixel Segmentation',
'SVM Classification': 'SVM Classification',
'Vegetation Index (Distance Based)': 'Vegetation Index (Distance Based)',
'Vegetation Index (Slope Based)': 'Vegetation Index (Slope Based)',
'Enhanced Vegetation Index': 'Enhanced Vegetation Index',
'Tasseled Cap Transformation': 'Tasseled Cap Transformation',
'IHS Sharpening': 'IHS Sharpening',
'Colour Normalized Brovey Sharpening': 'Colour Normalized Brovey Sharpening',
'Colour Normalized Spectral Sharpening': 'Colour Normalized Spectral Sharpening',
'Principal Component Based Image Sharpening': 'Principal Component Based Image Sharpening',
'Top of Atmosphere Reflectance': 'Top of Atmosphere Reflectance',
'Automated Cloud Cover Assessment': 'Automated Cloud Cover Assessment',
'Landsat Import with Options': 'Landsat Import with Options',
'Textural Features': 'Textural Features',
'Local Statistical Measures': 'Local Statistical Measures',
'Universal Image Quality Index': 'Universal Image Quality Index',
'Import Landsat Scene': 'Import Landsat Scene',
'Import Sentinel-2 Scene': 'Import Sentinel-2 Scene',
'Import Raster': 'Import Raster',
'Export Raster': 'Export Raster',
'Export GeoTIFF': 'Export GeoTIFF',
'Import Shapes': 'Import Features',
'Export Shapes': 'Export Features',
'Export Shapes to KML': 'Export Features to KML',
'Import NetCDF': 'Import NetCDF',
'Create Raster Catalogue from Files': 'Create Raster Catalogue from Files',
'Create Raster Catalogues from Directory': 'Create Raster Catalogues from Directory',
'GDAL Formats': 'GDAL Formats',
'Create Virtual Raster (VRT)': 'Create Virtual Raster (VRT)',
'Import from Virtual Raster (VRT)': 'Import from Virtual Raster (VRT)',
'GPX to shapefile': 'GPX to shapefile',
'GPSBabel': 'GPSBabel',
'Export ESRI Arc/Info Grid': 'Export ESRI Arc/Info Raster',
'Export Surfer Grid': 'Export Surfer Raster',
'Export Grid to XYZ': 'Export Raster to XYZ',
'Import USGS SRTM Grid': 'Import USGS SRTM Raster',
'Export True Color Bitmap': 'Export True Color Bitmap',
'Import Erdas LAN/GIS': 'Import Erdas LAN/GIS',
'Import WRF Geogrid Binary Format': 'Import WRF Geogrid Binary Format',
'Export WRF Geogrid Binary Format': 'Export WRF Geogrid Binary Format',
'Import, Clip and Resample Grids': 'Import, Clip and Resample Rasters',
'Import CRU Grids': 'Import CRU Rasters',
'Import Grids from KML': 'Import Rasters from KML',
'Export GStat Shapes': 'Export GStat Features',
'Import GStat Shapes': 'Import GStat Features',
'Export Shapes to XYZ': 'Export Features to XYZ',
'Import Shapes from XYZ': 'Import Features from XYZ',
'Export Shapes to Generate': 'Export Features to Generate',
'Export Surfer Blanking File': 'Export Surfer Blanking File',
'Import Surfer Blanking Files': 'Import Surfer Blanking Files',
'Export Atlas Boundary File': 'Export Atlas Boundary File',
'Import Atlas Boundary File': 'Import Atlas Boundary File',
'Export WASP terrain map file': 'Export WASP terrain map file',
'Import WASP terrain map file': 'Import WASP terrain map file',
'Import GPX': 'Import GPX',
'Export GPX': 'Export GPX',
'Export Scalable Vector Graphics (SVG) File': 'Export Scalable Vector Graphics (SVG) File',
'Import Simple Features from Well Known Text': 'Import Simple Features from Well Known Text',
'Export Simple Features to Well Known Text': 'Export Simple Features to Well Known Text',
'Import Building Sketches from CityGML': 'Import Building Sketches from CityGML',
'Export Polygons to HTML Image Map': 'Export Polygons to HTML Image Map',
'Import DXF Files': 'Import DXF Files',
'Export Text Table': 'Export Text Table',
'Import Text Table': 'Import Text Table',
'Import Text Table with Numbers only': 'Import Text Table with Numbers only',
'Create Virtual Point Cloud Dataset': 'Create Virtual Point Cloud Dataset',
'Create Tileshape from Virtual Point Cloud': 'Create Tileshape from Virtual Point Cloud',
'Get Grid from Virtual Point Cloud': 'Get Raster from Virtual Point Cloud',
'Remove Overlap from Virtual Point Cloud Tiles': 'Remove Overlap from Virtual Point Cloud Tiles',
'Geocoding': 'Geocoding',
'Warping Shapes': 'Warping Features',
'Direct Georeferencing of Airborne Photographs': 'Direct Georeferencing of Airborne Photographs',
'Define Georeference for Grids': 'Define Georeference for Rasters',
'World File from Flight and Camera Settings': 'World File from Flight and Camera Settings',
'Georeference with Coordinate Grids': 'Georeference with Coordinate Rasters',
'Set Coordinate Reference System': 'Set Coordinate Reference System',
'Coordinate Transformation (Shapes List)': 'Coordinate Transformation (Features List)',
'Coordinate Transformation (Grid List)': 'Coordinate Transformation (Raster List)',
'Coordinate Transformation (Grid)': 'Coordinate Transformation (Raster)',
'Change Longitudinal Range for Grids': 'Change Longitudinal Range for Rasters',
'Latitude/Longitude Graticule': 'Latitude/Longitude Graticule',
'Coordinate Reference System Picker': 'Coordinate Reference System Picker',
'Tissot''s Indicatrix': 'Tissot''s Indicatrix',
'Geographic Coordinate Grids': 'Geographic Coordinate Rasters',
'Geographic Distances': 'Geographic Distances',
'Geographic Distances (Pair of Coordinates)': 'Geographic Distances (Pair of Coordinates)',
'UTM Projection (Grid List)': 'UTM Projection (Raster List)',
'UTM Projection (Grid)': 'UTM Projection (Raster)',
'UTM Projection (Shapes List)': 'UTM Projection (Features List)',
'Single Coordinate Transformation': 'Single Coordinate Transformation',
'Coordinate Conversion (Grids)': 'Coordinate Conversion (Rasters)',
'Coordinate Conversion (Table)': 'Coordinate Conversion (Table)',
'Add Grid Values to Points': 'Add Raster Values to Points',
'Add Grid Values to Shapes': 'Add Raster Values to Features',
'Grid Statistics for Polygons': 'Raster Statistics for Polygons',
'Grid Values to Points': 'Raster Values to Points',
'Grid Values to Points (randomly)': 'Raster Values to Points (randomly)',
'Contour Lines from Grid': 'Contour Lines from Raster',
'Vectorising Grid Classes': 'Vectorising Raster Classes',
'Clip Grid with Polygon': 'Clip Raster with Polygon',
'Grid Statistics for Points': 'Raster Statistics for Points',
'Local Minima and Maxima': 'Local Minima and Maxima',
'Grid System Extent': 'Raster System Extent',
'Gradient Vectors from Surface': 'Gradient Vectors from Surface',
'Gradient Vectors from Direction and Length': 'Gradient Vectors from Direction and Length',
'Gradient Vectors from Directional Components': 'Gradient Vectors from Directional Components',
'Grid Classes Area for Polygons': 'Raster Classes Area for Polygons',
'Convert Polygons to Lines': 'Convert Polygons to Lines',
'Convert Points to Line(s)': 'Convert Points to Line(s)',
'Line Properties': 'Line Properties',
'Line-Polygon Intersection': 'Line-Polygon Intersection',
'Line Simplification': 'Line Simplification',
'Split Lines with Lines': 'Split Lines with Lines',
'Line Smoothing': 'Line Smoothing',
'Split Lines at Points': 'Split Lines at Points',
'Line Crossings': 'Line Crossings',
'Convert Table to Points': 'Convert Table to Points',
'Count Points in Polygons': 'Count Points in Polygons',
'Create Point Grid': 'Create Point Raster',
'Point to Point Distances': 'Point to Point Distances',
'Populate Polygons with Points': 'Populate Polygons with Points',
'Convert Lines to Points': 'Convert Lines to Points',
'Add Coordinates to Points': 'Add Coordinates to Points',
'Remove Duplicate Points': 'Remove Duplicate Points',
'Clip Points with Polygons': 'Clip Points with Polygons',
'Separate points by direction': 'Separate points by direction',
'Points Filter': 'Points Filter',
'Convex Hull': 'Convex Hull',
'Points Thinning': 'Points Thinning',
'Convert Multipoints to Points': 'Convert Multipoints to Points',
'Thiessen Polygons': 'Thiessen Polygons',
'Aggregate Point Observations': 'Aggregate Point Observations',
'Snap Points to Points': 'Snap Points to Points',
'Snap Points to Lines': 'Snap Points to Lines',
'Snap Points to Grid': 'Snap Points to Raster',
'Create Random Points': 'Create Random Points',
'Snap Points to Polygons': 'Snap Points to Polygons',
'3D Points Selection': '3D Points Selection',
'Point to Line Distances': 'Point to Line Distances',
'Polygon Centroids': 'Polygon Centroids',
'Convert Lines to Polygons': 'Convert Lines to Polygons',
'Convert Polygon/Line Vertices to Points': 'Convert Polygon/Line Vertices to Points',
'Polygon Shape Indices': 'Polygon Shape Indices',
'Polygon-Line Intersection': 'Polygon-Line Intersection',
'Polygons to Edges and Nodes': 'Polygons to Edges and Nodes',
'Polygon Parts to Separate Polygons': 'Polygon Parts to Separate Polygons',
'Polygon Clipping': 'Polygon Clipping',
'Polygon Self-Intersection': 'Polygon Self-Intersection',
'Intersect': 'Intersect',
'Difference': 'Difference',
'Symmetrical Difference': 'Symmetrical Difference',
'Union': 'Union',
'Update': 'Update',
'Identity': 'Identity',
'Flatten Polygon Layer': 'Flatten Polygon Layer',
'Shared Polygon Edges': 'Shared Polygon Edges',
'Polygon Generalization': 'Polygon Generalization',
'Merge Layers': 'Merge Layers',
'Select by Attributes... (Numerical Expression)': 'Select by Attributes... (Numerical Expression)',
'Select by Attributes... (String Expression)': 'Select by Attributes... (String Expression)',
'Select by Location...': 'Select by Location...',
'Copy Selection to New Shapes Layer': 'Copy Selection to New Features Layer',
'Delete Selection from Shapes Layer': 'Delete Selection from Features Layer',
'Invert Selection of Shapes Layer': 'Invert Selection of Features Layer',
'Split Shapes Layer Completely': 'Split Features Layer Completely',
'Transform Shapes': 'Transform Features',
'Create Graticule': 'Create Graticule',
'Copy Shapes from Region': 'Copy Features from Region',
'Split Shapes Layer': 'Split Features Layer',
'Split Shapes Layer Randomly': 'Split Features Layer Randomly',
'Split Table/Shapes by Attribute': 'Split Table/Features by Attribute',
'Shapes Buffer': 'Features Buffer',
'Get Shapes Extents': 'Get Features Extents',
'QuadTree Structure to Shapes': 'QuadTree Structure to Features',
'Polar to Cartesian Coordinates': 'Polar to Cartesian Coordinates',
'Generate Shapes': 'Generate Features',
'Convert Vertex Type (2D/3D)': 'Convert Vertex Type (2D/3D)',
'Merge Tables': 'Merge Tables',
'Land Use Scenario Generator': 'Land Use Scenario Generator',
'Select Shapes from List': 'Select Features from List',
'Remove Invalid Shapes': 'Remove Invalid Features',
'Copy Shapes': 'Copy Features',
'Focal Mechanism (Beachball Plots)': 'Focal Mechanism (Beachball Plots)',
'Transect through polygon shapefile': 'Transect through polygon shapefile',
'Cold Air Flow': 'Cold Air Flow',
'Conway''s Game of Life': 'Conway''s Game of Life',
'Wa-Tor': 'Wa-Tor',
'Hodgepodge Machine': 'Hodgepodge Machine',
'01: A Simple Litter System': '01: A Simple Litter System',
'02: Carbon Cycle Simulation for Terrestrial Biomass': '02: Carbon Cycle Simulation for Terrestrial Biomass',
'03: Spatially Distributed Simulation of Soil Nitrogen Dynamics': '03: Spatially Distributed Simulation of Soil Nitrogen Dynamics',
'MMF-SAGA Soil Erosion Model': 'MMF-SAGA Soil Erosion Model',
'Fire Risk Analysis': 'Fire Risk Analysis',
'Simulation': 'Simulation',
'Gravitational Process Path Model': 'Gravitational Process Path Model',
'Overland Flow (Kinematic Wave)': 'Overland Flow (Kinematic Wave)',
'TOPMODEL': 'TOPMODEL',
'Water Retention Capacity': 'Water Retention Capacity',
'Diffuse Pollution Risk': 'Diffuse Pollution Risk',
'Surface and Gradient': 'Surface and Gradient',
'Concentration': 'Concentration',
'Surface, Gradient and Concentration': 'Surface, Gradient and Concentration',
'Quasi-Dynamic Flow Accumulation': 'Quasi-Dynamic Flow Accumulation',
'Overland Flow': 'Overland Flow',
'SaLEM': 'SaLEM',
'Diffusive Hillslope Evolution (FTCS)': 'Diffusive Hillslope Evolution (FTCS)',
'Fill Sinks (QM of ESP)': 'Fill Sinks (QM of ESP)',
'Flow Accumulation (QM of ESP)': 'Flow Accumulation (QM of ESP)',
'Successive Flow Routing': 'Successive Flow Routing',
'Diffusive Hillslope Evolution (ADI)': 'Diffusive Hillslope Evolution (ADI)',
'RiverBasin': 'RiverBasin',
'LandFlow Version 1.0 (build 3.5.1b)': 'LandFlow Version 1.0 (build 3.5.1b)',
'RiverGridGeneration': 'RiverRasterGeneration',
'GridCombination': 'RasterCombination',
'Fast Representativeness': 'Fast Representativeness',
'Focal Statistics': 'Focal Statistics',
'Representativeness (Grid)': 'Representativeness (Raster)',
'Radius of Variance (Grid)': 'Radius of Variance (Raster)',
'Statistics for Grids': 'Statistics for Rasters',
'Zonal Grid Statistics': 'Zonal Raster Statistics',
'Directional Statistics for Single Grid': 'Directional Statistics for Single Raster',
'Global Moran''s I for Grids': 'Global Moran''s I for Rasters',
'Principal Component Analysis': 'Principal Component Analysis',
'Multi-Band Variation': 'Multi-Band Variation',
'Inverse Principal Components Rotation': 'Inverse Principal Components Rotation',
'Longitudinal Grid Statistics': 'Longitudinal Raster Statistics',
'Meridional Grid Statistics': 'Meridional Raster Statistics',
'Save Grid Statistics to Table': 'Save Raster Statistics to Table',
'Categorical Coincidence': 'Categorical Coincidence',
'Focal PCA on a Grid': 'Focal PCA on a Raster',
'Unique Value Statistics for Grids': 'Unique Value Statistics for Rasters',
'Ordinary Kriging': 'Ordinary Kriging',
'Simple Kriging': 'Simple Kriging',
'Universal Kriging': 'Universal Kriging',
'Regression Kriging': 'Regression Kriging',
'Variogram (Dialog)': 'Variogram (Dialog)',
'Variogram': 'Variogram',
'Variogram Cloud': 'Variogram Cloud',
'Minimum Distance Analysis': 'Minimum Distance Analysis',
'Spatial Point Pattern Analysis': 'Spatial Point Pattern Analysis',
'Regression Analysis (Points and Predictor Grid)': 'Regression Analysis (Points and Predictor Raster)',
'Multiple Regression Analysis (Points and Predictor Grids)': 'Multiple Regression Analysis (Points and Predictor Rasters)',
'Polynomial Regression': 'Polynomial Regression',
'GWR for Single Predictor (Gridded Model Output)': 'GWR for Single Predictor (Rasterded Model Output)',
'GWR for Single Predictor Grid': 'GWR for Single Predictor Raster',
'GWR for Multiple Predictor Grids': 'GWR for Multiple Predictor Rasters',
'Multiple Regression Analysis (Grid and Predictor Grids)': 'Multiple Regression Analysis (Raster and Predictor Rasters)',
'Trend Analysis': 'Trend Analysis',
'Trend Analysis (Shapes)': 'Trend Analysis (Features)',
'Multiple Linear Regression Analysis': 'Multiple Linear Regression Analysis',
'Multiple Linear Regression Analysis (Shapes)': 'Multiple Linear Regression Analysis (Features)',
'GWR for Grid Downscaling': 'GWR for Raster Downscaling',
'Zonal Multiple Regression Analysis (Points and Predictor Grids)': 'Zonal Multiple Regression Analysis (Points and Predictor Rasters)',
'Channel Network': 'Channel Network',
'Watershed Basins': 'Watershed Basins',
'Watershed Basins (Extended)': 'Watershed Basins (Extended)',
'Vertical Distance to Channel Network': 'Vertical Distance to Channel Network',
'Overland Flow Distance to Channel Network': 'Overland Flow Distance to Channel Network',
'Channel Network and Drainage Basins': 'Channel Network and Drainage Basins',
'Strahler Order': 'Strahler Order',
'Valley Depth': 'Valley Depth',
'CliffMetrics': 'CliffMetrics',
'Basic Terrain Analysis': 'Basic Terrain Analysis',
'Flow Accumulation (Top-Down)': 'Flow Accumulation (Top-Down)',
'Flow Accumulation (Recursive)': 'Flow Accumulation (Recursive)',
'Flow Accumulation (Flow Tracing)': 'Flow Accumulation (Flow Tracing)',
'Upslope Area': 'Upslope Area',
'Flow Path Length': 'Flow Path Length',
'Slope Length': 'Slope Length',
'Cell Balance': 'Cell Balance',
'Edge Contamination': 'Edge Contamination',
'SAGA Wetness Index': 'SAGA Wetness Index',
'Lake Flood': 'Lake Flood',
'Flow Width and Specific Catchment Area': 'Flow Width and Specific Catchment Area',
'Topographic Wetness Index (TWI)': 'Topographic Wetness Index (TWI)',
'Stream Power Index': 'Stream Power Index',
'LS Factor': 'LS Factor',
'Melton Ruggedness Number': 'Melton Ruggedness Number',
'TCI Low': 'TCI Low',
'LS-Factor, Field Based': 'LS-Factor, Field Based',
'Slope Limited Flow Accumulation': 'Slope Limited Flow Accumulation',
'Maximum Flow Path Length': 'Maximum Flow Path Length',
'Flow between fields': 'Flow between fields',
'Flow Accumulation (Parallelizable)': 'Flow Accumulation (Parallelizable)',
'Isochrones Variable Speed': 'Isochrones Variable Speed',
'Analytical Hillshading': 'Analytical Hillshading',
'Potential Incoming Solar Radiation': 'Potential Incoming Solar Radiation',
'Sky View Factor': 'Sky View Factor',
'Topographic Correction': 'Topographic Correction',
'Topographic Openness': 'Topographic Openness',
'Visibility (points)': 'Visibility (points)',
'Geomorphons': 'Geomorphons',
'Slope, Aspect, Curvature': 'Slope, Aspect, Curvature',
'Convergence Index': 'Convergence Index',
'Convergence Index (Search Radius)': 'Convergence Index (Search Radius)',
'Surface Specific Points': 'Surface Specific Points',
'Curvature Classification': 'Curvature Classification',
'Hypsometry': 'Hypsometry',
'Real Surface Area': 'Real Surface Area',
'Morphometric Protection Index': 'Morphometric Protection Index',
'Multiresolution Index of Valley Bottom Flatness (MRVBF)': 'Multiresolution Index of Valley Bottom Flatness (MRVBF)',
'Downslope Distance Gradient': 'Downslope Distance Gradient',
'Mass Balance Index': 'Mass Balance Index',
'Effective Air Flow Heights': 'Effective Air Flow Heights',
'Diurnal Anisotropic Heat': 'Diurnal Anisotropic Heat',
'Land Surface Temperature (Lapse Rates)': 'Land Surface Temperature (Lapse Rates)',
'Relative Heights and Slope Positions': 'Relative Heights and Slope Positions',
'Wind Effect (Windward / Leeward Index)': 'Wind Effect (Windward / Leeward Index)',
'Terrain Ruggedness Index (TRI)': 'Terrain Ruggedness Index (TRI)',
'Vector Ruggedness Measure (VRM)': 'Vector Ruggedness Measure (VRM)',
'Topographic Position Index (TPI)': 'Topographic Position Index (TPI)',
'TPI Based Landform Classification': 'TPI Based Landform Classification',
'Terrain Surface Texture': 'Terrain Surface Texture',
'Terrain Surface Convexity': 'Terrain Surface Convexity',
'Terrain Surface Classification (Iwahashi and Pike)': 'Terrain Surface Classification (Iwahashi and Pike)',
'Morphometric Features': 'Morphometric Features',
'Valley and Ridge Detection (Top Hat Approach)': 'Valley and Ridge Detection (Top Hat Approach)',
'Fuzzy Landform Element Classification': 'Fuzzy Landform Element Classification',
'Upslope and Downslope Curvature': 'Upslope and Downslope Curvature',
'Wind Exposition Index': 'Wind Exposition Index',
'Multi-Scale Topographic Position Index (TPI)': 'Multi-Scale Topographic Position Index (TPI)',
'Wind Shelter Index': 'Wind Shelter Index',
'Flat Detection': 'Flat Detection',
'Sink Drainage Route Detection': 'Sink Drainage Route Detection',
'Sink Removal': 'Sink Removal',
'Fill Sinks (Planchon/Darboux, 2001)': 'Fill Sinks (Planchon/Darboux, 2001)',
'Fill Sinks (Wang & Liu)': 'Fill Sinks (Wang & Liu)',
'Fill Sinks XXL (Wang & Liu)': 'Fill Sinks XXL (Wang & Liu)',
'Burn Stream Network into DEM': 'Burn Stream Network into DEM',
'Breach Depressions': 'Breach Depressions',
'Cross Profiles': 'Cross Profiles',
'Profiles from Lines': 'Profiles from Lines',
'Profile from points': 'Profile from points',
'SAFETYFACTOR': 'SAFETYFACTOR',
'TOBIA': 'TOBIA',
'SHALSTAB': 'SHALSTAB',
'WETNESS': 'WETNESS',
'WEDGEFAIL': 'WEDGEFAIL',
'ANGMAP': 'ANGMAP',
'Terrain Clustering': 'Terrain Clustering',
'Flow Accumulation (One Step)': 'Flow Accumulation (One Step)',
'LS Factor (One Step)': 'LS Factor (One Step)',
'Summit Extraction': 'Summit Extraction',
'Relief Segmentation': 'Relief Segmentation',
'Topographic Wetness Index (One Step)': 'Topographic Wetness Index (One Step)',
'Upslope Height, Slope, Aspect': 'Upslope Height, Slope, Aspect',
'Grid Values and Polygon Attributes to Points': 'Raster Values and Polygon Attributes to Points',
'Directional Grid Statistics': 'Directional Raster Statistics',
'Contour Lines from Points': 'Contour Lines from Points',
'Simple Filter for Multiple Grids': 'Simple Filter for Multiple Rasters',
'Notch Filter for Grids': 'Notch Filter for Rasters',
'Sieve and Clump': 'Sieve and Clump',
'Change a Grid''s No-Data Value [Bulk Processing]': 'Change a Raster''s No-Data Value [Bulk Processing]',
'Cloud Detection': 'Cloud Detection',
'Local Climate Zone Classification': 'Local Climate Zone Classification',
'Object Based Image Segmentation': 'Object Based Image Segmentation',
'Import Text Tables': 'Import Text Tables',
'Largest Circles in Polygons': 'Largest Circles in Polygons',
'Remove Boundary Polygons': 'Remove Boundary Polygons',
'Select and Delete': 'Select and Delete',
'Lapse Rate Based Temperature Downscaling': 'Lapse Rate Based Temperature Downscaling',
'Lapse Rate Based Temperature Downscaling (Bulk Processing)': 'Lapse Rate Based Temperature Downscaling (Bulk Processing)',
'Land Cover Scenario Offset': 'Land Cover Scenario Offset',
'Travel Time Calculation': 'Travel Time Calculation'}

def decoratedAlgorithmName(name):
	return algorithms.get(name, name)

