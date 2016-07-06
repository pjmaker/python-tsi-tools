# make-timeseries.py -- process timestamp data into regular time series data
# Copyright 2016 Ben Elliston

# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

import pandas as pd
import sample
import re
import sys
import iso8601
import argparse
from datetime import timedelta

import tags

PROJECT_NUMBER = 'CAR001'
PROJECT_NAME = 'SETuP'
DATA_FREQUENCY = {'60m': 'LOWRES', '1h': 'LOWRES', '30m': 'MEDRES', '15m': 'MEDRES',
                  '1m': 'HIRES', '5s': 'HIRES'}


def mkfilename(siteid, month, year, res):
    """
    Filename convention as follows:
    [PROJECT NUMBER]_[PROJECT NAME]_[YYYY-MM]_[DATA FREQUENCY].csv

    >>> mkfilename('BULM', 1, 2016, '1m')
    'CAR001_SETuP_BULM_2016-01_HIRES.csv'
    """

    assert year >= 1900
    assert month > 0 and month < 13
    try:
        res = DATA_FREQUENCY[res]
    except KeyError:
        raise KeyError('valid resolutions are %s' %
                       ', '.join(DATA_FREQUENCY.keys()))
    return '%s_%s_%s_%4d-%02d_%s.csv' % (PROJECT_NUMBER, PROJECT_NAME,
                                         siteid, year, month, res)

parser = argparse.ArgumentParser(description='Process timestamped data')
argparser = argparse.ArgumentParser()
argparser.add_argument("-v", action="store_true")
argparser.add_argument("-r", type=str, default='1h',
                       help='Resolution n[smh] [default: 1h]')
argparser.add_argument('--sampling', type=str, default='last',
                       choices=['min', 'max', 'last', 'avg', 'or'])
argparser.add_argument('start')
argparser.add_argument('end')
argparser.add_argument('filenames', nargs='+')
args = argparser.parse_args()

# Compute time delta.
val = int(args.r[:-1])
if args.r[-1] is 's':
    deltat = timedelta(seconds=val)
elif args.r[-1] is 'm':
    deltat = timedelta(minutes=val)
elif args.r[-1] is 'h':
    deltat = timedelta(hours=val)
else:
    raise ValueError('invalid specification %s' % args.r)

dataframes = []
siteid = None

for fname in args.filenames:
    fields = fname.split('_')
    assert len(fields) >= 4, "ill-formed filename %s" % fname
    pitag = '_'.join(fields[4:-2])
    if siteid is None:
        # first file sets the site ID
        siteid = fields[3]
    else:
        # make sure every CSV file belongs to the same site
        assert siteid == fields[3], 'site %s != %s' % (fields[3], siteid)
    try:
        tag = tags.transform(pitag)
    except ValueError:
        if args.v:
            print >>sys.stderr, "skipping unknown or unmapped tag: %s" % pitag
        continue
    df = pd.read_csv(fname, parse_dates=True, index_col=0)
    assert df.shape[1] == 1
    df.sort_index()
    dataframes.append((tag, df))

t = iso8601.parse_date(args.start)
t2 = iso8601.parse_date(args.end)
assert t < t2, 'start time must come before end time'

filename = mkfilename(siteid, t.month, t.year, args.r)
print 'creating', filename

f = open(filename, 'w')
print >>f, "t," + ','.join([tg for tg, _ in dataframes])

fn = sample.switch[args.sampling]
while t < t2:
    s = "%s," % t.strftime("%Y/%m/%d %H:%M:%S")
    for (_, df) in dataframes:
        rows = df[t:t + deltat]
        s += '%s,' % fn(rows)
    # a bit of cleanup before printing
    s = re.sub("  ", " ", s)
    s = re.sub(",(nan|NaN)", ",", s)
    s = re.sub(",$", "", s)
    print >>f, s
    t += deltat

print 'closing', filename
f.close()
