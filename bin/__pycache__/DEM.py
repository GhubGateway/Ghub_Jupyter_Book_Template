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

sys.path.append ('./elevation')
print("sys.path: ", sys.path)

import elevation
#help (elevation)

#/util/academic/grass7.2.2/anaconda2/lib/python2.7/site-packages/osgeo/gdal.py
from osgeo import gdal

def main(argv):
    
    print ("DEM...")
    #print (argv)
    
    print ('os.path.expanduser("~"): ', os.path.expanduser("~"))
    workingdir = os.getcwd()
    print ('workingdir: ', workingdir)

    lat_bottom = float(argv[1])
    lat_top = float(argv[2])
    lon_left = float(argv[3])
    lon_right = float(argv[4])
    grassgis_database = os.path.join(workingdir, argv[5])
    grassgis_location = argv[6]
    grassgis_mapset = argv[7]
    grassgis_map = argv[8]
    
    #'''
    print('lat_bottom: ', lat_bottom)
    print('lat_top : ', lat_top)
    print('lon_left: ', lon_left)
    print('lon_right: ', lon_right)
    print('grassgis_database: ', grassgis_database)
    print('grassgis_location ', grassgis_location)
    print('grassgis_mapset: ', grassgis_mapset)
    print('grassgis_map: ', grassgis_map)
    #'''
    
    # Set GISBASE environment variable
    gisbase = '/util/academic/grass7.2.2/grass-7.2.2'
    os.environ['GISBASE'] = gisbase
    print ("os.environ['GISBASE']: ", os.environ['GISBASE'])
    
    # Set GISRC environment variable
    #gisrc = './rc'
    #os.environ['GISRC'] = gisrc
    
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
    
    # elevation / gdal
    start_time1 = time.time()
    start_time2 = time.time()
    
    print ('workingdir: ', workingdir)
    
    # Geotiff has only 1 band
    geotiff = os.path.join(workingdir, 'elevation.tif')
    print ('geotiff: ', geotiff)
    
    '''
    # clip the SRTM1 30m DEM and save it to elevation.tif.
    # elevation.tif: Band 1 Block=256x256 Type=Int16, ColorInterp=Gray
    # Titan2D needs floating point data
        
    # Rome
    # Bounding box: left bottom right top
    elevation.clip(bounds=(lon_left, lat_bottom, lon_right, lat_top), output=geotiff)
    # clean up stale temporary files and fix the cache in the event of a server error
    elevation.clean()
    '''
    
    ds = gdal.Open(geotiff)
    ds = gdal.Translate('xxx.tif', ds, outputType=float)
    ds = None
    
    elapsed_time = time.time() - start_time2
    print ('elapsed time: ', np.round(elapsed_time/60.0, 2), ' [min]')
    
    start_time2 = time.time()
    
    #database = os.path.join(workingdir, database)
    #location = "maploc"
    #mapset = "PERMANENT"
    
    if os.path.exists(grassgis_database):
        print ('removing: ', grassgis_database)
        shutil.rmtree(grassgis_database)
    os.mkdir(grassgis_database)
    #os.makedirs(database)

    #grass_setup.write_gisrc(gisbase, location=location, mapset=mapset)
    gisrc = grass_setup.init (gisbase, dbase=grassgis_database, location=grassgis_location, mapset=grassgis_mapset)
    print ('gisrc filepath: \n', gisrc)
    f = open(gisrc,'r')
    output = f.read()
    f.close()
    print ('gisrc contents: \n', output)
    
    print ("os.environ['GISRC']: ", os.environ['GISRC'])
    #print ("os.environ['MAPSET']: ", os.environ['MAPSET'])
    
    # OGR: vector data
    # GDAL: rastor data
    
    # grass --text -c Rome-DEM.tif location
    # https://gis.stackexchange.com/questions/328291/creating-new-grass-locations-while-looping-in-python-script
    # https://baharmon.github.io/python-in-grass
    # https://grasswiki.osgeo.org/wiki/GRASS_Python_Scripting_Library
    
    # This creates the PERMANENT mapset
    grass_script.run_command('g.proj', flags='c', georef=geotiff, location=grassgis_location)
    
    print ('OK1')
    
    #os.mkdir(os.path.join(grassgis_database, grassgis_location, grassgis_mapset))
    #xxx = grass_script.run_command('g.mapset', flags='c', location=grassgis_location, mapset=grassgis_mapset)
    #print (xxx)
    
    print ('OK2')
    
    grass_script.run_command(
        'r.in.gdal',
        input = 'elevation.tif',
        output = grassgis_map,
        overwrite=True)
    
    print ('OK3')
    
    grass_script.run_command(
        'r.colors',
        map = grassgis_map,
        color = 'elevation')
    
    print ('OK4')
    
    elapsed_time = time.time() - start_time2
    print ('elapsed time: ', np.round(elapsed_time/60.0, 2), ' [min]')
    
    start_time2 = time.time()
    
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
    grass_script.run_command('g.list', type='rast', flags='p')
    
    print ('OK5')
    
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
    
    #grass_script.run_command(
    #    'd.text',
    #    text="Test of GRASS_RENDER_COMMAND redirection")
    
    print ('OK8')
    
    #grass_script.run_command(
        #'d.rast',
        #map=raster)
           
    print ('OK9')
    
    grass_script.run_command(
        'd.mon',
        stop='cairo')
    
    print ('OK10')
    
    os.remove(gisrc)
    
    elapsed_time = time.time() - start_time2
    print ('elapsed time: ', np.round(elapsed_time/60.0, 2), ' [min]')

    elapsed_time = time.time() - start_time1
    print ('elapsed time: ', np.round(elapsed_time/60.0, 2), ' [min]')

if __name__ == "__main__":

    main(sys.argv)


    
