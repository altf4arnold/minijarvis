"""
This bot is a IRCbot base and was first used to solver a challenge on a CTF.
It was inspired by some internet posts and then adapted here.
I tried to make a base bot that basicaly could be adapted to be used in other
situations
"""

import socket
import ctf


def connecttoserv(server, port, botnick):
    """
    This connects the bot to the server. The code is prety straight forward.
    If you want more info, it's basicaly filling in a form for the irc server
    """
    ircsock.connect((server, port))
    ircsock.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " " + botnick + "\n", "UTF-8"))
    ircsock.send(bytes("NICK " + botnick + "\n", "UTF-8"))


def joinchan(chan):
    """
    Pretty straight forward. This function joins you to a chan.
    It's a part of the initial connection procedure.
    (the print(ircmsg) will also show the connecttoserv debug info)
    """
    ircsock.send(bytes("JOIN " + chan + "\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find("End of /NAMES list.") == -1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        # This print is usefull to debug.
        # It shows the entire reply/motd of the server.
        print(ircmsg)


def ping():
    """
    respond to ping
    """
    ircsock.send(bytes("PONG :pingis\n", "UTF-8"))


def sendmsg(msg, target):
    """
    This function sends messages.
    """
    ircsock.send(bytes("PRIVMSG " + target + " :" + msg + "\n", "UTF-8"))


def messageanalyser(botnick, ctfmode):
    """
    This function receive the messages and analyse them
    It can call other functions in reaction.
    """
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    # Usefull to debug
    print(ircmsg)

    if ircmsg.find("PRIVMSG") != -1:
        name = ircmsg.split('!', 1)[0][1:]
        message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]

    # Fun function to see the syntax and how it works.
    if message.find('Hi ' + botnick) != -1:
        # debug test because what the hell is this condition ???
        print("We are in for some reason ¯\_(ツ)_/¯")
        sendmsg("Hello " + name + "!", name)

    # Required. If not implemented, might be kicked from the server
    if ircmsg.find("PING :") != -1:
        """
        this one responds to ping \o/
        (Still need to figure out why != -1)
        """
        ping()


def main():
    """
    Contains some basic info usefull for use and launches everything
    """
    server = "chat.freenode.net"  # Server
    port = 6667  # The port is 6667 on most servers
    channel = "#amasingchannel"  # Channel
    botnick = "Mini-Jarvis"  # Your bots nick
    adminname = "Me"  # Your IRC nickname.
    exitcode = "bye " + botnick
    ctfmode = False

    connecttoserv(server, port, botnick)
    joinchan(channel)

    if ctfmode is True:
        ctf.ctftrigger()
    # I know, while True is not clean. But it works.
    while True:
        messageanalyser(botnick, ctfmode)


# Yikes, global vars
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    main()
