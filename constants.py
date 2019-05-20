ID = 'id'
BOUND1 = 'bound1'
BOUND2 = 'bound2'

WEATHER = 'weather'
WEATHER_X = 'Day Number'
WEATHER_Y = 'Temperature'
WEATHER_TITLE = 'Temperature Highs and Lows over Month and Minimum Spread'
WEATHER_UPPER_LABEL = 'High Temps'
WEATHER_LOWER_LABEL = 'Low Temps'

# Everythin from line 7 to 36 is included.  Only the first 3 rows are needed
WEATHER_ARGS = {
    'filepath_or_buffer':   'w_data.dat', 
    'sep':                  '\s+',
    'engine':               'python',
    'header':               None, 
    'skiprows':             [0,1,2,3,4],
    'usecols':              [0,1,2],
    'skipfooter':           2
}


SOCCER = 'soccer'
SOCCER_X = 'Team Number'
SOCCER_Y = 'Points Scored'
SOCCER_TITLE = 'Soccer Points Scored and Minimum Spread'
SOCCER_UPPER_LABEL = 'Points For'
SOCCER_LOWER_LABEL = 'Points Against'

# Everything from line 4 to 24 (excluding line 20) are included.  Columns 1 6 and 8 are used
SOCCER_ARGS = {
    'filepath_or_buffer':   'soccer.dat', 
    'sep':                  '\s+',
    'engine':               'python',
    'header':               None, 
    'skiprows':             [0,1,2,20],
    'usecols':              [1,6,8],
    'index_col':            False,
    'skipfooter':           1
}

MIN_LABEL = "Minimum Spread"

