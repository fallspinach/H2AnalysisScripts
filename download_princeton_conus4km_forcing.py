import os
from datetime import datetime, timedelta

dapserver = 'http://stream.princeton.edu:8080/opendap/Forecast_Monitoring/Forcing_CONUS_4km/'

# pull forcing data
day1 = datetime(2008,  1,  1)
day2 = datetime(2008, 12, 31)

day = day1
while day <= day2:
    fileurl= '%4d/%4d%02d/Forcing_CONUS_150s_%4d%02d%02d.nc' % (day.year, day.year, day.month, day.year, day.month, day.day)
    os.system('wget '+dapserver+fileurl)
    day += timedelta(days=1)
