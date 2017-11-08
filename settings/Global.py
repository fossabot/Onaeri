##################
# Basic settings #
##################
transitionTime = 1              # Lamp transition time in seconds, unsigned float


#####################
# Advanced settings #
#####################
commandsTries = 3               # Amount of times to try sending a command, unsigned int
mainLoopDelay = 1               # Time in seconds between main loops, unsigned float

settingFileExtention = '.py'    # Extention of settings file, String


###############
# Data tables #
###############
minPerTimeCode  = .5            # Minutes per datapoint, unsigned float
totalDataPoints = round((24*60) // minPerTimeCode)
