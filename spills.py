# spills.py -- estimate spills from a PV/diesel hybrid system
#
# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# To see usage:
# python spills.py --help

import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Simulate spilling')
argparser = argparse.ArgumentParser()
argparser.add_argument("-p", type=int, default=200,
                       help='PV capacity')
argparser.add_argument("-d", type=int, default=320,
                       help='Diesel capacity')
argparser.add_argument("-m", type=float, default=0.4,
                       help='Minimum load factor [default: 0.4]')
argparser.add_argument("-r", type=int, default=25,
                       help='Spinning reserve [default: 25 kW]')
args = argparser.parse_args()

# Demand is in column 2 (col 1 for numpy)
demand = np.genfromtxt('CAR001_SETuP_TITR_2015-01_MEDRES.csv', missing_values='NaN', delimiter=',', usecols=(1))

# Solar irradiance is in column 6 (col 5 for numpy)
solar = np.genfromtxt('AliceSolar-2015.csv', missing_values='NaN', delimiter=',', usecols=(5))

# Filter NaNs from solar data (and corresponding value from the demand
# time series).
nans = np.isnan(solar)
solar = solar[~nans]
demand = demand[~nans]

# Likewise, filter NaNs from demand (and corresponding value from the
# demand time series).
nans = np.isnan(demand)
solar = solar[~nans]
demand = demand[~nans]

# Note that we approximate solar PV output by assuming the PV array
# produces its rated output when solar irradiance reaches its maximum
# value in the time series.
maxsolar = solar.max()
nsteps = solar.shape[0]

def schedule(load):
    """
    Schedule for a given load. Return the number of gensets required
    and their total minimum output.
    """
    numsets = np.ceil(load / args.d)
    return numsets, numsets * args.d * args.m

def fuelcons(nsets, load):
    """Return diesel fuel use per half-hour."""
    litres = nsets * 12 + 72 * (load / float(nsets * args.d))
    # nb. per half hour
    return litres * 0.5

print args
pvgen = 0
for i in xrange(nsteps):
    pvgen += ((solar[i] / maxsolar) * args.p) * 0.5
print 'Total generation:', int(pvgen), 'kWh'

fuel = 0
spills = 0
kwh = 0

for i in xrange(nsteps):
    assert demand[i] != np.nan and solar[i] != np.nan

    load = demand[i]
    pvpower = (solar[i] / maxsolar) * args.p
    nsets, minload = schedule(load + args.r)
    pvsetp = load - minload

    if pvpower > pvsetp:
        spills += (pvpower - pvsetp) * 0.5  # kw -> kWh
        kwh += pvsetp * 0.5
    else:
        kwh += pvpower * 0.5

    residual = load - min(pvpower, pvsetp)
    # useful for debugging
    # print i, 'load=', int(load), 'pv=', int(pvpower), 'units=', int(nsets), 'minload=', int(minload), 'pvsetp=', int(pvsetp)
    fuel += fuelcons(nsets, residual)

print 'Total PV used:', int(kwh), 'kWh'
print 'Spilled energy:', int(spills), 'kWh', '(%.1f%%)' % (spills / pvgen * 100)
print 'Total fuel consumption:', int(fuel), 'L'
