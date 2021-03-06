#*******************************************************************************
# Environment variable that numbers the rank of the processor in question. 
# This is a string and on daint, it is 'ALPS_APP_PE', on laptops with OpenMPI, it is 'OMPI_COMM_WORLD_RANK'
# -- not needed anymore, since working with mpi4py again.
# ******************************************************************************
# rankvariable = 'OMPI_COMM_WORLD_RANK'

# print screen output
verbose=True

# save intermediate result at every time window or every couple of windows as determined by the next parameter interm_nstack (attention, this needs some storage space and is also slower.)
write_all=False
# save intermediate windows not after every time window, but after this many single windows have been stacked:
interm_nstack = 1
# provide a name that will appear as 'stamp' on all correlations calculated in this run
corrname='noisy'

# Set to True if updating on a previous run?
update = False
	
#*******************************************************************************
# Specifics for data distribution to cores
# ******************************************************************************
# station ID list; containing entries in format net.sta.loc.cha
idfile = 'INPUT/correlationlist.txt'
# How many station pairs for each core? Typically the number of files opened by that core is about n+1
npairs = 1
# channel: LH, BH, VH...
channel='LH'
# component: choose between Z, RT, T, R. 'All channels' is not implemented yet
components='Z'
# Mix channels?
mix_cha=False

 #*******************************************************************************
# selection
#*******************************************************************************

# Input directory containing data. Can only handle one input directory at the moment.
indir='/Volumes/cowpox/DATA/processed/noisy'
# Enter preprocessing run name(s). Put * for any preprocessing
prepname='noisy'
    #*******************************************************************************
# Time
#*******************************************************************************
# Sampling rate.If different from sampling rate, data will be downsampled before correlation.
Fs = [0.5]
#Start date. Will only process files from this
startdate='20140101'
#End date. Will only process files until this. Format yyyymmdd
enddate='20150101'
#Length of the time windows to be correlated, in seconds
winlen = 32768#6553.6
#Overlap in SECONDS
#Groos et al. recommend an overlap that is equal to the maximum lag
olap=6000
    
   
    #*******************************************************************************#Correlations
#*******************************************************************************
#apply bandpass before correlating
apply_bandpass = True
filter=(0.003,0.01,3)

#apply pretreatment
cap_glitches=False
glitch_thresh = 15.
apply_onebit=False
apply_white=False
white_freqs=(0.01,2.)
white_tape=0.02
apply_ram=False
ram_window=50.
ram_filter=(0.02,0.066667,4)
taper_traces=True
perc_taper=0.02
	
#Type of correlations

#Autocorrelation yes or no
autocorr=False
# Type of correlation: 'ccc' or 'pcc' or 'both'
corrtype='ccc'
# Normalize the correlation? (otherwise it remains a covariance)
normalize_correlation=True
# Maximum lag in seconds
max_lag=12000
# Obtain a phase weight? (cf Schimmel and Paulssen 2007)
get_pws=False
#For phase cross-correlation: Specify exponent (cf Schimmel et al. 2013)
pcc_nu=1


    #*******************************************************************************#Self-check of input
#*******************************************************************************

if type(verbose) != bool:
    msg = 'Control input file: verbose must be boolean'
    raise TypeError(msg)
    
if type(write_all) != bool:
    msg = 'Control input file: write_all must be boolean'
    raise TypeError(msg)

if type(interm_nstack) != int and type(interm_nstack) != float:
    msg = 'Control input file: interm_nstack must be str or float'
    raise TypeError(msg)
    
if type(update) != bool:
    msg = 'Control input file: update must be boolean'
    raise TypeError(msg)
    
if type(mix_cha) != bool:
    msg = 'Control input file: mix_cha must be boolean'
    raise TypeError(msg)

if type(apply_bandpass) != bool:
    msg = 'Control input file: apply_bandpass must be boolean'
    raise TypeError(msg)
    
if type(apply_onebit) != bool:
    msg = 'Control input file: apply_onebit must be boolean'
    raise TypeError(msg)
    
if type(apply_white) != bool:
    msg = 'Control input file: apply_white must be boolean'
    raise TypeError(msg)
    
if type(apply_ram) != bool:
    msg = 'Control input file: apply_white must be boolean'
    raise TypeError(msg)
    
if type(get_pws) != bool:
    msg = 'Control input file: get_pws must be boolean'
    raise TypeError(msg)
    
if type(cap_glitches) != bool:
    msg = 'Control input file: cap_glitches must be boolean'
    raise TypeError(msg)
    
if type(autocorr) != bool:
    msg = 'Control input file: verbose must be boolean'
    raise TypeError(autocorr)

if type(corrname) != str:
    msg = 'Control input file: corrname must be str'
    raise TypeError(msg)
    
if type(idfile) != str:
    msg = 'Control input file: idfile must be str'
    raise TypeError(msg)
    
if type(channel) != str:
    msg = 'Control input file: channel must be str'
    raise TypeError(msg)
    
if type(components) != str:
    msg = 'Control input file: components must be str'
    raise TypeError(msg)
    
if type(indir) != str:
    msg = 'Control input file: indir must be str'
    raise TypeError(msg)
    
if type(startdate) != str:
    msg = 'Control input file: startdate must be str'
    raise TypeError(msg)

if type(enddate) != str:
    msg = 'Control input file: enddate must be str'
    raise TypeError(msg)

if type(prepname) != str:
    msg = 'Control input file: prepname must be str'
    raise TypeError(msg)
    
if type(corrtype) != str:
    msg = 'Control input file: corrtype must be str'
    raise TypeError(msg)

if corrtype == 'both' and apply_white == True:
    msg = 'Are you sure you want to whiten before phase\
    cross correlation?'
    warn(msg)
    
if type(npairs) != int:
    msg = 'Control input file: npairs must be int'
    raise TypeError(msg)
    
if type(filter) != tuple:
    msg = 'Control input file: filter must be tuple'
    raise TypeError(msg)
    
if type(Fs) != list:
    msg = 'Control input file: Fs must be list'
    raise TypeError(msg)
    
if type(white_freqs) != tuple:
    msg = 'Control input file: white_freqs must be tuple'
    raise TypeError(msg)

if type(winlen) not in (float,int):
    msg = 'Control input file: winlen must be float or integer'
    raise TypeError(msg)
    
if type(olap) not in (float,int):
    msg = 'Control input file: olap must be float or integer'
    raise TypeError(msg)

if type(max_lag) not in (float,int):
    msg = 'Control input file: max_lag must be float or integer'
    raise TypeError(msg)
    
if type(pcc_nu) not in (float,int):
    msg = 'Control input file: pcc_nu must be float or integer'
    raise TypeError(msg)
