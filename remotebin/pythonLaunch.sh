#!/bin/sh

# On Vhub, this file is installed to /apps/$tooldir/dev/remotebin directory

commandError=0
ERROR_EXIT_CODE=1

# Verify the python files do not contain unallowed system calls
pyFiles=$(ls *.py 2> /dev/null)
#echo ${pyFiles}
for pyFile in ${pyFiles} ; do
   echo "Verifying pyFile: ${pyFile}"
   for command in system popen subprocess ; do
      commandCount=$(grep -c -E "${command}[[:space:]]*\(|${command}[[:space:]]*\.\.\." ${pyFile})
      if [ ${commandCount} -gt 0 ] ; then
         echo "The Python command ${command} is not allowed in file ${pyFile}"
         commandError=1
      fi
   done
done

if [ ${commandError} -eq 1 ] ; then
   exit ${ERROR_EXIT_CODE}
fi

. /util/common/Lmod/lmod/lmod/init/sh

# Load grass module
module load grass/7.2.2

# Now have access to:
#/util/academic/grass7.2.2/bin/grass
#/util/academic/grass7.2.2/anaconda2/bin/python
#/util/academic/grass7.2.2/anaconda2/lib/python2.7/site-packages/osgeo/gdal.py
# GDAL command line tools:
#/util/academic/grass7.2.2/anaconda2/bin/gdalinfo
#/util/academic/grass7.2.2/anaconda2/bin/gdal_translate

# Install the elevation package,
# requires GDAL command line tools
python -m pip install --target=./elevation elevation

python "$@"

