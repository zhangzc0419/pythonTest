from datetime import datetime, timedelta
import re

# now = datetime.now()
# print now


# dt = datetime(1991, 4, 19)
# print dt
#
# t = 1429417200.0
# print(datetime.fromtimestamp(t))

# t = 1429417200.0
# print datetime.fromtimestamp(t)
# print datetime.utcfromtimestamp(t)

# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print cday

# now = datetime.now()
# print now.strftime('%A, %B %d %H:%M')

# now = datetime.now()
# print now
# print now + timedelta(hours=10)
# print now - timedelta(days=1)
# print now + timedelta(days=2, hours=12)

def datetime2timestamp(dt, convert_to_utc=False):
    ''' Converts a datetime object to UNIX timestamp in milliseconds. '''
    if isinstance(dt, datetime.datetime):
        if convert_to_utc:
            dt = dt + datetime.timedelta(hours=-8)
        timestamp = total_seconds(dt - EPOCH)
        return long(timestamp)
    return dt
print datetime2timestamp(datetime.now())
