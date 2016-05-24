# sample.py -- various sampling methods for a bucket of observations
# Copyright 2016 Ben Elliston

# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

import pandas as pd
import numpy as np

# Collect points between t-1 and t.
# Here is a sample with six data points.
sample = pd.DataFrame({'A': [1, 3, 5, np.nan, 6, 8]})
empty = pd.DataFrame([])

nan = float('nan')


def avgsample(df):
    """
    Return the average value in the data frame.

    >>> avgsample(empty)
    nan
    >>> round(avgsample(sample), 1)
    4.6
    """
    if len(df) == 0:
        return nan
    else:
        return np.mean(df.iloc[::, 0])


def minsample(df):
    """
    Return the minimum value in the data frame.

    >>> minsample(empty)
    nan
    >>> minsample(sample)
    1.0
    """
    if len(df) == 0:
        return nan
    else:
        return min(df.iloc[::, 0])


def maxsample(df):
    """
    Return the maximum value in the data frame.

    >>> maxsample(empty)
    nan
    >>> maxsample(sample)
    8.0
    """
    if len(df) == 0:
        return nan
    else:
        return max(df.iloc[::, 0])


def orsample(df):
    """
    Return the bitwise-OR of every value in the data frame.

    >>> orsample(empty)
    0
    >>> result = 1 | 3 | 5 | 6 | 8
    >>> assert result == orsample(sample)
    """
    if len(df) == 0:
        return 0
    result = 0
    for val in df.iloc[::, 0]:
        if val > 0:
            result |= int(val)
    return result


def lastsample(df):
    """
    Return the last sample in the data frame.

    >>> lastsample(empty)
    nan
    >>> lastsample(sample)
    8.0
    """
    if len(df) == 0:
        return nan
    else:
        return df.iloc[-1, 0]

switch = {'min': minsample, 'max': maxsample, 'or': orsample,
          'last': lastsample, 'avg': avgsample}
