Disaster Relief Trials Leaderboard
=================

Dependencies:
-------------
Python 2.7
Ruby 2.0 (dev)
Node (dev)
Bower

Install Options:
--------
1. Follow the commands in vagrant-provision.sh, but use your package manager
    (brew, rpm, etc) instead of apt-get.
2. Use vagrant `vagrant up`.

Database:
---------
Mongo - follow vagrant-provision instructions on mongo and start it
`mongod`

Everything should work as long as it is running.

Running the web server:
-------------------
`python server.py`

Running the socket server:
`python ws_server.py`

*You will need to start the ws_server _first_ before starting the webserver.

Navigate to `localhost:5000`
