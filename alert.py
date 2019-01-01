"""
This module is used to send an alert to the admin to tell him when it's time
to refresh the SSL cert on his irc client
"""

from datetime import datetime as date
import time as sleep


def alert():
    current = str(date.now()).split()
    string = ''
    time = []
    for i in current[0]:
        if i == "-":
            time.append(int(string))
            string = ''
        else:
            string = string + i
    time.append(int(string))
    if time[2] == 1 and current[1].find("00:00:00") != -1:
        print(current[1])
        toreturn = "Hey, please run /relay sslcertkey"
        sleep.sleep(1)
    else:
        toreturn = "nope"
    return toreturn
