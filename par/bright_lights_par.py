#!/usr/bin/python

#------------------------------------------------------------------------------
#   Purpose:    Outline definitions for match filter python code
#   Author:     Calum John Chamberlain
#------------------------------------------------------------------------------

"""
Outline definitions for bright_lights python code
"""
from obspy import UTCDateTime
stations=['EORO','WHYM','COSA','FOZ',
          'GOVA','LABE','MTFO','RPZ',
          'COVA','FRAN','POCR','SOLU',
          'WHAT','POCR2','WHAT2']   # List of stations to use for template
                                        # generation

nllpath='./grid/3D'                       # Path to nonlinloc .csv grid files of
                                        # travel times
# volume=[(-43.8,-43.55),
        # (169.5,170.0),
        # (20,35)]
# volume=[(-43.8,-43.55),
        # # (169.5,170.05),
        # # (15,40)]
volume=[(-43.8,-43.75),(169.6,169.85),(25,28)]
                                        # List of tuples in the form:
                                        # [(minlat,maxlat),(minlong,laxlong),
                                        # (mindepth,maxdepth)]
                                        # Where coordinates are decimal degrees
                                        # in lat and long and km in depth
resolution=(0.02,2)                     # Horizontal and vertical resolution
                                        # for resampled grid in decimal
                                        # degrees and km respectively.
                                        # with depth increasing down
startdate=UTCDateTime('2013-03-28')     # obspy UTCDateTime object giving
                                        # date to start looking for templates
                                        # beyond
enddate=UTCDateTime('2013-03-29')       # As above, but the end date
threshold=10                            # Threshold value, if threshtype is
                                        # set to MAD then this will by the
                                        # MAD to the power of this value
thresh_type='RMS'                       # Threshold type, can be either MAD
                                        # or abs (case-sensitive)
phase='P'                               # Can be either P or S, will use this
                                        # when reading in the travel-time
                                        # grids.
ps_ratio=1.68                           # P to S ratio if only one grid type
                                        # provided, P is S*ps_ratio
nodesimthresh=0.0625                    # Minimum cumulative difference in
                                        # network moveout, should be about the
                                        # period of twice the maximum frequency
                                        # of the signal you want to detect
coherance=0.2                           # Coherance threshold to remove
                                        # incoherant peaks in the network
                                        # response.
