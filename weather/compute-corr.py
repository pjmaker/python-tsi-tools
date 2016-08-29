import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr


def xcorr(x, y, k, normalize=True):
    n = x.shape[0]
    # initialize the output array
    out = np.empty((2 * k) + 1, dtype=np.double)
    lags = np.arange(-k, k + 1)

    # pre-compute E(x), E(y)
    mu_x = x.mean()
    mu_y = y.mean()

    # loop over lags
    for ii, lag in enumerate(lags):

        # use slice indexing to get 'shifted' views of the two input signals
        if lag < 0:
            xi = x[:lag]
            yi = y[-lag:]
        elif lag > 0:
            xi = x[:-lag]
            yi = y[lag:]
        else:
            xi = x
            yi = y

        # x - mu_x; y - mu_y
        xdiff = xi - mu_x
        ydiff = yi - mu_y

        # E[(x - mu_x) * (y - mu_y)]
        out[ii] = xdiff.dot(ydiff) / n

        # NB: xdiff.dot(ydiff) == (xdiff * ydiff).sum()

    if normalize:
        # E[(x - mu_x) * (y - mu_y)] / (sigma_x * sigma_y)
        out /=  np.std(x) * np.std(y)

    return lags, out

### Alice Springs

alice_temp = np.genfromtxt('Alice-2015.csv', delimiter=',', usecols=(7))
alice_solar = np.genfromtxt('AliceSolar-2015.csv', delimiter=',', usecols=(5))

temp_nans = np.isnan(alice_temp)
alice_temp = alice_temp[~temp_nans]
alice_solar = alice_solar[~temp_nans]

solar_nans = np.isnan(alice_solar)
alice_temp = alice_temp[~solar_nans]
alice_solar = alice_solar[~solar_nans]

### Darwin

darwin_temp = np.genfromtxt('Darwin-2015.csv', delimiter=',', usecols=(7))
darwin_solar = np.genfromtxt('DarwinSolar-2015.csv', delimiter=',', usecols=(5))

temp_nans = np.isnan(darwin_temp)
darwin_temp = darwin_temp[~temp_nans]
darwin_solar = darwin_solar[~temp_nans]

solar_nans = np.isnan(darwin_solar)
solar_zeros = np.equal(darwin_solar, 0)
darwin_temp = darwin_temp[np.logical_not(np.logical_or(solar_nans, solar_zeros))]
darwin_solar = darwin_solar[np.logical_not(np.logical_or(solar_nans, solar_zeros))]

print spearmanr(alice_temp, alice_solar)
