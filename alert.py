"""
This module is used to send an alert to the admin to tell him when it's time
to refresh the SSL cert on his irc client
"""

from datetime import datetime as date


def alert():
    current = str(date.now()).split()
    string = ''
    time = []
    for i in current:
        if i == "-":
            time.append(int(string))
            string = ''
        else:
            string = string + i
    if time[2]==1 and current[1].find("00:00:0"):
        toreturn = "Hey, please run /relay sslcertkey"
    else:
        toreturn = "nope"
    return toreturn
