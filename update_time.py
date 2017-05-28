#!/usr/bin/python
#
# File:   nts_sync.py
# Author: Jason Letbetter
# Date:   8/24/2006
#
# This software gets the date from a naval time server and updates the system
# clock for posix OS supporting the "date" command.  It also requires an
# internet connection.
#
# WARNING: It will not work if your system clock is already off by more than
# 1 month.
#
# TIP: Use kcron to schedule this script on a periodic basis.
#
# Example:
# jason@gummybear:~$ nts_sync.py
# Before update: Sat Aug 26 08:48:41 CDT 2006
# Updating to: Sat Aug 26 13:48:41 UTC 2006
# After update: Sat Aug 26 08:48:41 CDT 2006
#


import os
import re
import requests
import sys
from subprocess import Popen, PIPE


def main(argv):
    # Print current date
    sys.stdout.write('Before update: ')
    sys.stdout.flush()
    os.system('date')
    # Update date from naval server
    date = get_date()
    sys.stdout.write('Updating to: ')
    sys.stdout.flush()
    os.system('sudo date -u %s' % date)
    # Print updated date
    sys.stdout.write('After update: ')
    sys.stdout.flush()
    os.system('date')


def get_local_year(svr_mo):
    # Use the local machine's year b/c naval server doesn't have it
    p_result = Popen('date', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    date, err = p_result.communicate()
    yr = int(date[-5:-1], 10)
    # TRICKY: We have to be careful around January 1st
    svr_mo = int(svr_mo)
    loc_mo = int(month_map[date[4:7]])
    # Assume local machine is slow and its near Jan 1st
    if svr_mo == 1 and loc_mo == 12:
        yr += 1
    # Assume local machine is fast and its near Jan 1st
    elif svr_mo == 12 and loc_mo == 1:
        yr -= 1
    return str(yr)


def get_date():
    # Read date from naval time server (tax payers only ;^)
    url = requests.get('http://tycho.usno.navy.mil/cgi-bin/timer.pl')
    text = repr(url.content)
    regx = r'([a-z,A-Z,]+)\.\s+(\d+)\,\s+(\d+):(\d+):(\d+)\s+UTC'
    # Parse text to get UTC date strings
    mo, da, hr, mi, se = re.search(regx, text).groups()
    # Compute month number from abbreviation
    mo = month_map[mo]
    # Get the year from our local clock
    yr = get_local_year(mo)
    # Return the proper date format
    return mo + da + hr + mi + yr + '.' + se


month_map = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
    'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
    'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}

if __name__ == '__main__':
    main(sys.argv[1:])
