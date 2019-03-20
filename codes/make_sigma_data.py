#!/usr/bin/env python
#Write new file

import numpy as np

# physical constants for natural units c = G = 1
c=2.99792458*(10**8)
G=6.67428*(10**(-11))
s_mass=G*(1.98892*10**(30))/(c**3)

# common function shortcuts
log10 = np.log10
pi = np.pi
sqrt = np.sqrt

filename = "SIGMA_DATA.lst"

gal_name = []
sigma = []
RA = []
DEC = []
distance = []
sigma = []
k_mag = []


catalog = np.loadtxt("galaxy_data/2mass_galaxies.lst", usecols = (1,2,3,4))
cat_name = np.genfromtxt("galaxy_data/2mass_galaxies.lst",  usecols=(5), dtype='str')

dyn_smbh_name = np.genfromtxt("galaxy_data/schutzMa_extension.txt", usecols=(0), dtype='str', skip_header = 2)
dyn_smbh_mass = np.genfromtxt("galaxy_data/schutzMa_extension.txt", usecols = (4), skip_header = 2)

ext_catalog = np.loadtxt("galaxy_data/added_Mks.lst", usecols = (1,2,3,4,5), skiprows = 2)
ext_name = np.genfromtxt("galaxy_data/added_Mks.lst", usecols=(0), dtype='str', skip_header = 2)

sigma_name = np.loadtxt("galaxy_data/2mass_GRP_sigma.lst", usecols = (0), dtype = 'str')
sigma_sigma = np.loadtxt("galaxy_data/2mass_GRP_sigma.lst", usecols = (1))

# Identify galaxies with dynamically measured supermassive black holes (33)

ext_bh_mass = ext_catalog[:,3] # in units of solar masses

all_dyn_bh_name = np.hstack((dyn_smbh_name, ext_name)) # names of galaxies w dyn. BH masses
all_dyn_bh_mass = np.hstack((dyn_smbh_mass, ext_bh_mass)) #BH masses of these galaxies

# Given parameters (derived or from 2MASS)
RA = pi/180*catalog[:,0]
DEC = pi/180*catalog[:,1]
distance = catalog[:,2]
k_mag = catalog[:,3]
 
# Extend catalog with galaxies having dynmically measured SMBHs which are not in original list

RA = np.hstack((RA, pi/180*ext_catalog[:,0]))
DEC = np.hstack((DEC, pi/180*ext_catalog[:,1]))
distance = np.hstack((distance, ext_catalog[:,2]))
k_mag = np.hstack((k_mag, ext_catalog[:,4]))
cat_name = np.hstack((cat_name, ext_name))


final_size = len(sigma_name)

final_RA = []
final_DEC = []
final_dist = []
final_mag = []
final_name = []
final_sigma = []

for i in range(final_size):
    if np.isin(sigma_name[i], cat_name):
        gal_ind = np.where(cat_name==sigma_name[i])[0][0]
        final_RA.append(RA[gal_ind])
        final_DEC.append(DEC[gal_ind])
        final_dist.append(distance[gal_ind])
        final_mag.append(k_mag[gal_ind])
        final_name.append(cat_name[gal_ind])
        final_sigma.append(sigma_sigma[i])

dest_file = "galaxy_data/"+str(filename)
result_file = open(dest_file, "a")

for R, D, Di, M, N, S in zip(final_RA, final_DEC, final_dist, final_mag, final_name, final_sigma):
    result_file.write('{0} {1} {2} {3} {4} {5}\n'.format(R, D, Di, M, N, S))
result_file.close()




