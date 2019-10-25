# AMUSING sample characterisation:

Tomás Ruiz-Lara


***************************************
# TABLES
***************************************

## Hyperleda:

In this table I compile all the available information for the AMUSING sample of galaxies using hyperleda. All the columns are as follows:

Amusing Name --> The name according to the original AMUSING table

redshift_amusing --> redshift according to the original AMUSING table

def_name --> most common name

SN_name --> Name of the SN linked to this obeject

SN_type --> SN type

pgc -->  Hyperleda internal number

hl_names(pgc) --> 	list of all names

objtype --> 	type of object

al1950	 --> RA 1950 (hours decimal value)

de1950 --> 	DEC 1950 (degrees decimal value)

celposb(pgc) --> 	B1950 position (character string)

al2000 --> 	RA 2000 (hours decimal value)

de2000 --> 	DEC 2000 (degrees decimal value)

celposj(pgc) --> 	J2000 position (character string)

l2	 --> galactic longitude (degrees)

b2	 --> galactic latitude (degrees)

sgl --> 	supergalactic longitude (degrees)

sgb --> 	supergalactic latitude (degrees)

f_astrom --> 	Precision flag on the celestial position

type	 --> morphological type

bar	 --> bar (B or blank)

ring	 --> ring (R or blank)

multiple --> 	multiple (M or blank)

compactness --> 	Compactness (C=Compact or D=Diffuse or blank )

t --> 	morphological type code

e_t --> 	actual error on t

lc	 --> luminosity class code

e_lc	 --> actual error on lc

logd25	 --> log10 of apparent diameter (d25 in 0.1')

e_logd25 --> 	actual error on logd25

logr25	 --> log10 of axis ratio (major axis/minor axis)

e_logr25 --> 	actual error on logr25

pa --> 	major axis position angle (North Eastwards) in degrees

brief --> 	mean effective surface brightness (mag.arcsec-2)

e_brief --> 	actual error on brief

bt	 --> total B-magnitude

e_bt --> 	actual error on bt

it	 --> total I-magnitude

e_it --> 	actual error on it

ubt --> 	total U-B color

bvt --> 	total B-V color

ube --> 	effective U-B color

bve --> 	effective B-V color

vmaxg --> 	Apparent maximum rotation velocity of gas

e_vmaxg	 --> actual error on vmaxg

vmaxs	 --> Apparent maximum rotation velocity of stars

e_vmaxs	 --> actual error on vmaxs

vdis	 --> Central velocity dispersion (in km/s)

e_vdis	 --> actual error on vdis

mg2 --> 	Central Mg2 Lick index (in mag)

e_mg2 --> 	actual error on mg2

m21	 --> 21-cm line flux in magnitude (see definition in text)

e_m21 --> 	actual error on m21

mfir	 --> far infrared magnitude (see definition in text)

vrad --> 	heliocentric radial velocity from radio measurement (in km/s)

e_vrad --> 	actual error on vrad

vopt --> 	heliocentric radial velocity from optical measurement (in km/s)

e_vopt	 --> actual error on vopt

v	 --> mean heliocentric radial velocity (in km/s)

e_v --> 	actual error on v

ag	 --> Galactic extinction in B magnitude

ai	 --> extinction due to inclination in B magnitude (see text)

incl --> 	inclination between line of sight and polar axis (in degrees)

a21	 --> 21-cm self absorption in magnitude

lambda --> 	luminosity index

logdc --> 	log10 of apparent corrected diameter (dc in 0.1')

btc	 --> total apparent corrected B-magnitude

ubtc --> 	total apparent corrected U-B color

bvtc	 --> total apparent corrected B-V color

bri25 --> 	mean surface brightness within isophote 25 (mag.arcsec-2)

vrot	 --> maximum velocity rotation (in km/s)

e_vrot --> 	actual error on vrot

m21c --> 	corrected 21-cm line flux in magnitude (see text)

hic	 --> 21-cm index bt-m21c in magnitude

vlg	 --> radial velocity with respect to the Local Group (km/s)

vgsr --> 	radial velocity with respect to the GSR (km/s)

vvir --> 	radial velocity corrected for Virgocentric infall (km/s)

v3k	 --> radial velocity with respect to the CMB radiation (km/s)

modz	 --> redshift distance modulus

mod0	 --> true distance modulus (from parameters)

mabs	 --> absolute B-magnitude 

Pointings --> Number of pointings MUSE data

RA_pointing --> RA of the different pointings

DEC_pointing --> DEC of the different pointings

RA_SN --> RA of the different SNs

DEC_SN --> DEC of the different SNs

Source --> program or source from where the data come from

RA_DSS --> RA of the central point in the DSS images

DEC_DSS --> DEC of the central point in the DSS images

offset_RA --> Distance (in arcsec and RA) from the SN to the centre of the galaxy (coords_SN - coords_gal)

offset_DEC --> Distance (in arcsec and DEC) from the SN to the centre of the galaxy (coords_SN - coords_gal)





****************************************************
# Virtual Observatory
****************************************************

Although all this information might be important to characterise the AMUSING sample, having optical images to see how they look like and to play with the data (obtain surface brightness profiles, ellipticity and position angle of the disc, etc.) is crucial.

## Carnegie-Irvine survey

Some of the galaxies are also part of the Carnegie-Irvine Survey (https://cgs.obs.carnegiescience.edu/CGS/Home.html). All the information from that survey (analysis of the light distribution, masses, colour profiles, etc etc...) can be downloaded for those galaxies in the survey's webpage (https://cgs.obs.carnegiescience.edu/CGS/Home.html).

## DSS

I have downloaded all the fits files for the galaxies in the AMUSING sample using the red bands with two different fields of view (5'x5' and 15'x15'). With all these data we can further characterise the sample. I have created also some png files (see folder named 'images') for a quicker visualization of the galaxies.

## SDSS

 I cross-check the AMUSING sample with SDSS database and I obtain 20 galaxies in common. I download colour images for visualization purposes. To download photometric and spectroscopic data use SDSS_query.py.




