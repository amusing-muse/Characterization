import numpy as np
from astropy.io import fits
from astropy.io import ascii
import os


table_data = ascii.read('files.txt', format='no_header')
filename = table_data['col1']

path = '/eridano/lgalbany/AMUSING/'

for index, name in enumerate(list(filename)):
    if os.path.isfile(name+'.V.fits.gz') == True and os.path.isfile(path+name+'.fits') == True:
        cube = fits.open(path+name+'.fits')
        cube_data = cube[1].data
        cube_head = cube[1].header
        
        Vmap = fits.open(name+'.V.fits.gz', mode='update')
        Vmap_data = Vmap[0].data
        Vmap_head = Vmap[0].header
        
        Vmap_head['CRPIX1'] = cube_head['CRPIX1']
        Vmap_head['CRPIX2'] = cube_head['CRPIX2']
        Vmap_head['CD1_1'] = cube_head['CD1_1']
        Vmap_head['CD1_2'] = cube_head['CD1_2']
        Vmap_head['CD2_1'] = cube_head['CD2_1']
        Vmap_head['CD2_2'] = cube_head['CD2_2']
        Vmap_head['CUNIT1'] = cube_head['CUNIT1']
        Vmap_head['CUNIT2'] = cube_head['CUNIT2']
        Vmap_head['CTYPE1'] = cube_head['CTYPE1']
        Vmap_head['CTYPE2'] = cube_head['CTYPE2']
        Vmap_head['CSYER1'] = cube_head['CSYER1']
        Vmap_head['CSYER2'] = cube_head['CSYER2']
        Vmap_head['CRVAL1'] = cube_head['CRVAL1']     
        Vmap_head['CRVAL2'] = cube_head['CRVAL2']         
        
        Vmap.flush()
        Vmap.close()

