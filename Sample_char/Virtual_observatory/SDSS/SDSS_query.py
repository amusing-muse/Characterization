from astroquery.sdss import SDSS
from astropy import coordinates as coords
import requests
from astropy import units as u
import urllib
from astropy.io import ascii
import numpy as np
import os

PATH = '/home/tomas/Documents/Astronomia/AMUSING/Sample_char/Virtual_observatory'

input_data = ascii.read(PATH+'/listMUSE.txt')

missing = open('SDSS_missing.txt', 'w')

Galaxy, RA, DEC, RED = input_data['Galaxy'], input_data['RA'], input_data['DEC'], input_data['RED']

for i in np.arange(len(Galaxy)):

    gal_name = Galaxy[i]

    print gal_name

    #if os.path.isdir(PATH+'/'+str(Galaxy)) == True:
    #    pass
    #else:
    #    os.system('mkdir '+PATH+'/'+str(gal_name))

    RAi, DECi = RA[i], DEC[i]

    pos = coords.SkyCoord(str(RAi)+' '+str(DECi), unit=(u.hourangle, u.deg))
    xid = SDSS.query_region(pos, spectro=True)  #ra   dec   objid   run  rerun camcol field   z  plate  mjd  fiberID  specobjid run2d instrument
    print xid

    if xid is not None:
        ra, dec, rerun, run, camcol, field, mjd, fiberID, plate = xid[0]['ra'], xid[0]['dec'], xid[0]['rerun'], xid[0]['run'], xid[0]['camcol'], xid[0]['field'], xid[0]['mjd'], xid[0]['fiberID'], xid[0]['plate']

        #bands = ['u', 'g', 'r', 'i', 'z']

        #bands = ['u', 'g']

        #for band in bands:
            #urllib.urlretrieve('http://dr12.sdss3.org./sas/dr12/boss/photoObj/frames/'+str(rerun)+'/'+str(run)+'/'+str(camcol)+'/frame-'+str(band)+'-00'+str(run)+'-'+str(camcol)+'-0'+str(field)+'.fits.bz2', PATH+'/'+str(gal_name)+'/frame-'+str(band)+'-00'+str(run)+'-'+str(camcol)+'-0'+str(field)+'.fits.bz2') #retrieve photometry

        #urllib.urlretrieve('http://dr12.sdss3.org/sas/dr12/sdss/spectro/redux/26/spectra/0'+str(plate)+'/spec-0'+str(plate)+'-'+str(mjd)+'-0'+str(fiberID)+'.fits', PATH+'/'+str(gal_name)+'/spec-0'+str(plate)+'-'+str(mjd)+'-0'+str(fiberID)+'.fits') #retrieve spectroscopy

        urllib.urlretrieve('http://skyservice.pha.jhu.edu/DR12/ImgCutout/getjpeg.aspx?ra='+str(ra)+'&dec='+str(dec)+'&scale=0.25&width=400&height=400&opt=GST', PATH+'/SDSS/'+str(gal_name)+'.jpg') #retrieve jpg image

    else:
        print 'missing', gal_name
        missing.write(gal_name+' \n')

missing.close()

