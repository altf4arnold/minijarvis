# Mini Jarvis
## What is this ?
This is a small python irc bot base.
It was initially used to solve a CTF challenge but was created to be adapted
for a little bit any use we want.

## To run it :
```
virtualenv -p python3.7 ve3
source ve3/bin/activate
python bot.py
```

## Tricky part :
Warning, there is a .find in the code that needs to be modified if you are using this bot on something other then a freenode irc server.
It will indicate to the bot when he is connected.
