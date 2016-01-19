Introduction
============

This is a python setup for analysing irregularly sampled time series
data using pandas, numpy, etc.

Overview
========

Input Data Format
----------------- 
		 
The incoming data is kept in ASIM format using ISO8601 time stamps
and looks like:: 
		 
   t,R_K_PG_BULM_Fed3Pact
   1999-12-31 14:30:00.000+00:00, NaN
   2015-06-18 16:06:54.000+00:00, NaN
   2015-06-18 16:14:00.000+00:00, 20.00000
   2015-06-18 16:14:10.000+00:00, NaN
   2015-07-18 16:14:14.535+00:00, 50.00000
   2015-07-18 16:14:30.535+00:00, NaN
		 
The timestamps are all in UCT and 
		 
The values are plain old numbers using NaN to indicate loss
of signal, e.g. a communications link failure, Values maintain
their old value until the next sample.
		 
Reading data into a Pandas DataFrame
------------------------------------
		 
Multiple data files can be read into a single pandas DataFrame, e.g
reading Test1.csv and Test2.csv containing the data for all 
timestamps in the series in a DataFrame. Extra fields include:
		 
   #. t - the timestamp for a particular point in time which is the index.
   #. Test1, Test2 - the actual data (in this example).
   #. dt - the duration that all variables remain the same, i.e. the time in seconds
      to the next row.
   #. wTest1, wTest2 - the time intergral for Test1 at this time.
   #. tTest1, tTest2 - the duration for each value or 0 if it is not a number (NaN)
		 
The frame data looks like::
		 
  *                            Test1  Test2  Remarks           dt
  t                                                                                                    
  1999-12-31 14:30:00.000000    NaN    NaN      NaN  0.000000e+00
  1999-12-31 14:30:00.000000    NaN    NaN      NaN  4.879930e+08
  2015-06-18 16:06:54.000000    NaN    NaN      NaN  0.000000e+00
  2015-06-18 16:06:54.000000    NaN    NaN      NaN  4.260000e+02
  2015-06-18 16:14:00.000000     20    NaN      NaN  2.000000e+00
  2015-06-18 16:14:02.000000     20    120      NaN  8.000000e+00
  2015-06-18 16:14:10.000000    NaN    120      NaN  2.009999e+00
  2015-06-18 16:14:12.009999    NaN    NaN      NaN  2.592003e+06
  2015-07-18 16:14:14.535000     50    NaN      NaN  2.000000e+00
  2015-07-18 16:14:16.535000     50      5      NaN  1.400000e+01
  2015-07-18 16:14:30.535000    NaN      5      NaN  0.000000e+00
  2015-07-18 16:14:30.535000    NaN    NaN      NaN           NaN

Along with w*, t* values which will look like::

  *                          wTest1  tTest1     wTest2     tTest2
  t                                                                                                    
  1999-12-31 14:30:00.000000    NaN       0        NaN   0.000000
  1999-12-31 14:30:00.000000    NaN       0        NaN   0.000000
  2015-06-18 16:06:54.000000    NaN       0        NaN   0.000000
  2015-06-18 16:06:54.000000    NaN       0        NaN   0.000000
  2015-06-18 16:14:00.000000     40       2        NaN   0.000000
  2015-06-18 16:14:02.000000    160       8  960.00000   8.000000
  2015-06-18 16:14:10.000000    NaN       0  241.19988   2.009999
  2015-06-18 16:14:12.009999    NaN       0        NaN   0.000000
  2015-07-18 16:14:14.535000    100       2        NaN   0.000000
  2015-07-18 16:14:16.535000    700      14   70.00000  14.000000
  2015-07-18 16:14:30.535000    NaN       0    0.00000   0.000000
  2015-07-18 16:14:30.535000    NaN       0        NaN   0.000000

Where Test1.csv is::

  t,R_K_PG_BULM_Fed3Pact
  1999-12-31 14:30:00.000+00:00, NaN
  2015-06-18 16:06:54.000+00:00, NaN
  2015-06-18 16:14:00.000+00:00, 20.00000
  2015-06-18 16:14:10.000+00:00, NaN
  2015-07-18 16:14:14.535+00:00, 50.00000
  2015-07-18 16:14:30.535+00:00, NaN

And Test2.csv is::

  t,R_K_PG_BULM_PvPact
  1999-12-31 14:30:00.000+00:00, NaN
  2015-06-18 16:06:54.000+00:00, NaN
  2015-06-18 16:14:02.000+00:00, 120.00000
  2015-06-18 16:14:12.010+00:00, NaN
  2015-07-18 16:14:16.535+00:00, 5.00000
  2015-07-18 16:14:30.535+00:00, NaN


