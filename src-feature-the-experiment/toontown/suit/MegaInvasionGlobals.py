from toontown.parties.ToontownTimeZone import ToontownTimeZone
from datetime import datetime

INVASION_TIME_FORMAT = '%Y-%m-%d %H:%M'

START_TIME = 0
END_TIME = 1
SUIT_DEPT = 2
SUIT_INDEX = 3
SUIT_AMOUNT = 4
REOCCURING = 5
HOLIDAY_ID = 6

RANDOM = -1

invasions = [
    # START, END, DEPT, INDEX, AMOUNT, REOCCURING, HOLIDAY_ID
    ['2015-08-16 14:00', '2015-08-16 16:00', RANDOM, 2, 500, True, None],
    ['2015-08-16 16:30', '2015-08-16 21:00', RANDOM, RANDOM, 500, True, None],
    ['2015-08-16 21:30', '2015-08-17 03:00', 1, RANDOM, 500, True, None],
    ['2015-08-17 03:30', '2015-08-17 07:00', RANDOM, 4, 500, True, None],
    ['2015-08-17 07:30', '2015-08-17 12:30', RANDOM, 5, 500, True, None],
    ['2015-08-17 13:00', '2015-08-17 23:00', RANDOM, RANDOM, 500, True, None],
    ['2015-08-18 00:00', '2015-08-18 08:00', RANDOM, 1, 500, True, None], 
]

safeShards = ['Corky Bay']


def parseInvasionTime(invasionTime):
    return datetime.strptime(invasionTime, INVASION_TIME_FORMAT).replace(tzinfo=ToontownTimeZone())
