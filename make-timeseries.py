# make-timeseries.py -- process timestamp data into regular time series data
# Copyright 2016 Ben Elliston

import pandas as pd
import sample
import re
import iso8601
import argparse
from datetime import timedelta

parser = argparse.ArgumentParser(description='Process timestamped data')
argparser = argparse.ArgumentParser()
argparser.add_argument('filename')
argparser.add_argument('start')
argparser.add_argument('end')
argparser.add_argument("-r", type=str, default='1h',
                       help='Resolution n[smh] [default: 5m]')
argparser.add_argument('--sampling', type=str, default='last',
                       choices=['min', 'max', 'last', 'or'])
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

df = pd.read_csv(args.filename, parse_dates=True, index_col=0)
df.sort()
assert df.shape[1] == 1

t = iso8601.parse_date(args.start)
t2 = iso8601.parse_date(args.end)
assert t < t2, 'start time must come before end time'

while t < t2:
    fn = sample.switch[args.func]
    rows = df[t:t + deltat]
    s = '%s, %s' % (t.isoformat(), fn(rows))
    s = re.sub("  ", " ", s)
    s = re.sub(", nan", ", NaN", s)
    print s
    t += deltat
