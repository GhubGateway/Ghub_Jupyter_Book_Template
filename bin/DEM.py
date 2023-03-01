#----------------------------------------------------------------------------------------------------------------------
# Class: DEM
# Component of: ghub_vhub_exercise2 (github.com)
# Called from: Invoked as a thread from ghub_exercise1.ipynb
# Purpose: Run a Pegasus workflow via the HUBzero hublib.cmd interface
# Author: Renette Jones-Ivey
# Date: Feb 2023
#---------------------------------------------------------------------------------------------------------------------
import sys
import numpy as np
import os
import time
import shutil

# References:
# https://pypi.org/project/elevation/
# https://grasswiki.osgeo.org/wiki/GRASS_Python_Scripting_Library
# https://baharmon.github.io/python-in-grass

sys.path.append ('./elevation')
#print("sys.path: ", sys.path)

import elevation
#help (elevation)

#CCR: /util/academic/grass7.2.2/anaconda2/lib/python2.7/site-packages/osgeo/gdal.py
from osgeo import gdal
#help(gdal)

def main(argv):
    
    print ('DEM.py...')
    #print (argv)
    
    print ('os.path.expanduser("~"): ', os.path.expanduser('~'))
    workingdir = os.getcwd()
    print ('workingdir: ', workingdir)

    lat_south = float(argv[1])
    lat_north = float(argv[2])
    lon_west = float(argv[3])
    lon_east = float(argv[4])
    grassgis_database = os.path.join(workingdir, argv[5])
    grassgis_location = argv[6]
    grassgis_mapset = argv[7]
    grassgis_map = argv[8]
    
    #'''
    print('lat_south: ', lat_south)
    print('lat_north : ', lat_north)
    print('lon_west: ', lon_west)
    print('lon_east: ', lon_east)
    print('grassgis_database: ', grassgis_database)
    print('grassgis_location ', grassgis_location)
    print('grassgis_mapset: ', grassgis_mapset)
    print('grassgis_map: ', grassgis_map)
    #'''
    
    # Set GISBASE environment variable
    gisbase = '/util/academic/grass7.2.2/grass-7.2.2'
    os.environ['GISBASE'] = gisbase
    print ("os.environ['GISBASE']: ", os.environ['GISBASE'])
    
    # Set GISLOCK environment variable
    os.environ['GISLOCK'] = '$$'
    
    # define GRASS-Python environment
    grass_python_dir = os.path.join(gisbase, "etc", "python")
    print ('grass_python_dir: ', grass_python_dir)
    sys.path.append(grass_python_dir)
    print ('sys.path: ', sys.path)
    import grass.script as grass_script
    #help (grass)
    
    import grass.script.setup as grass_setup
    # Notes for setting up
    #help (grass_setup)
    
    #print ('Current GRASS 7 environment: ', grass_script.gisenv())
    
    start_time = time.time()
    
    print ('workingdir: ', workingdir)
    
    # Geotiff has only 1 band
    geotiff1 = os.path.join(workingdir, 'elevation1.tif')
    print ('geotiff1: ', geotiff1)
    geotiff2 = os.path.join(workingdir, 'elevation2.tif')
    print ('geotiff2: ', geotiff2)
    
    #'''
    # clip the SRTM1 30m DEM and save it to elevation1.tif.
        
    # Bounding box: left bottom right top
    elevation.clip(bounds=(lon_west, lat_south, lon_east, lat_north), output=geotiff1)
    # clean up stale temporary files and fix the cache in the event of a server error
    elevation.clean()
    #'''
    
    # elevation1.tif: Band 1 Block=256x256 Type=Int16, ColorInterp=Gray
    print (gdal.Info(geotiff1))
    
    # Note Titan2D needs floating point data
    
    ds = gdal.Open(geotiff1)
    ds = gdal.Translate(geotiff2, ds, outputType=gdal.GDT_Float32)
    ds = None
    
    #Band 1 Block=7200x1 Type=Float32, ColorInterp=Gray    
    print (gdal.Info(geotiff2))
        
    if os.path.exists(grassgis_database):
        print ('removing: ', grassgis_database)
        shutil.rmtree(grassgis_database)
    os.mkdir(grassgis_database)
    #os.makedirs(database)

    #Create the rc file
    gisrc = grass_setup.init (gisbase, dbase=grassgis_database, location=grassgis_location, mapset=grassgis_mapset)
    print ("os.environ['GISRC']: ", os.environ['GISRC'])
    f = open(gisrc,'r')
    output = f.read()
    f.close()
    print ('gisrc contents: ', output)
    
    #print ("os.environ['MAPSET']: ", os.environ['MAPSET'])
    
    # OGR: vector data
    # GDAL: rastor data
    
    # This creates the PERMANENT mapset
    grass_script.run_command('g.proj', flags='c', georef=geotiff2, location=grassgis_location)
    
    print ('OK1')
    
    # Getting errors when Mapset is not PERMANENT?
    #os.mkdir(os.path.join(grassgis_database, grassgis_location, grassgis_mapset))
    #print(grass_script.run_command('g.mapset', flags='c', location=grassgis_location, mapset=grassgis_mapset))
    
    print ('OK2')
    
    # Create the Grass GIS fcell raster file
    grass_script.run_command(
        'r.in.gdal',
        input = geotiff2,
        output = grassgis_map,
        overwrite=True)
    
    print ('OK3')
    
    grass_script.run_command(
        'r.colors',
        map = grassgis_map,
        color = 'elevation')
    
    print ('OK4')
    
    env = grass_script.gisenv()
    print ('env: ', env)
    env['GRASS_OVERWRITE'] = True
    env['GRASS_VERBOSE'] = True
    env['GRASS_MESSAGE_FORMAT'] = 'text'
    gisdbase = env['GISDBASE']
    print ('gisbase: ', gisdbase)
    location = env['LOCATION_NAME']
    print ('location: ', location)
    mapset = env['MAPSET']
    print ('mapset: ', mapset)
    print ('env: ', env)
    
    # list rasters in mapset
    print(grass_script.run_command('g.list', type='rast', flags='p'))
    
    print ('OK5')
    
    '''
    #raster_list = grass_script.list_grouped('rast')[mapset]
    #print ('raster_list: ', raster_list)
    
    #location = "maploc/PERMANENT/cell/elevation-DEM"
    #maploc_filepath = os.path.join(database, location)
    #print ('maploc_filepath: ', maploc_filepath)
    
    raster =  grassgis_map
    
    #png_file = os.path.join(
            #database,
            #location,
            #mapset,
            #raster+'.png')
    raster_png_file = raster + '.png'
    print ('raster_png_file: ', raster_png_file)
    
    #Select the region
    grass_script.run_command(
        'g.region',
        raster=raster,
        res=0.1)
    
    print ('OK6')
    
    #The Cairo driver generates PNG, BMP, PPM, PS, PDF or SVG images by GRASS display commands, using the Cairo graphics library.
    grass_script.run_command(
        'd.mon',
        start='cairo',
        width=1000,
        height=1000,
        output=raster_png_file,
        overwrite=True)
    
    print ('OK7')
    
    grass_script.run_command(
        'd.mon',
        stop='cairo')
    
    print ('OK8')
    '''
    
    os.remove(gisrc)
    
    elapsed_time = time.time() - start_time
    print ('elapsed time: ', np.round(elapsed_time/60.0, 2), ' [min]')

if __name__ == "__main__":

    main(sys.argv)


    
