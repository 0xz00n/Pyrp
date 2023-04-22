# Pyrp
Kind of like Burp for TCP protocols. But worse.

This is really just a script that makes thick app network analysis/modification easy in restrictive environments.  It should work as long as python 3 is installed on the machine.

## How-to
I included demo server/client scripts to make understanding how this works easier.

### Setting up demoserver.py
- Make a vm or use an existing server and take note of its IP address.
- Make sure python3 is installed
- Place demoserver.py on said VM/server
- run `python demoserver.py`
- ???
- Profit! (And just let it run)

### Setting up pyrp.py and democlient.py
We're going to pretend that democlient.py is the thick app you're testing here and that both democlient.py and pyrp.py are on the same machine (Because that's the normal use-case).

- Make sure python3 is installed
- Modify the `tarip` var in pyrp.py to the IP address of your server noted earlier
- run `python pyrp.py`
- In a new terminal, run `python democlient.py`
- ???
- Profit!

You should have noticed that both the client and server show "HACKED!" and exited.

### What happened?
The whole point of this script is to easily modify TCP payloads on the fly.  If you look at the `replacer()` function, its whole purpose is to search for something within a TCP payload and, if it finds that something, send a modified version of it instead.  You, the user, would be changing the `replacer()` function to fit the needs to of the protocol.  By default, `replacer()` is only looking at packets sent from the application.  If you need it to inspect packets from the upstream server, you'll want to move it within the `handler()` function.

### Assumptions
I'm assuming that you can work with/understand python and sockets.

### The Future
I may make this more 'user friendly' in the future, but I have no immediate plans to.  If you'd like to contribute, please do.
