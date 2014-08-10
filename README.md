Disaster Relief Trials Leaderboard
=================

Dependencies:
-------------
Python - see requirements.txt file.
Ruby - see Gemfile.
JS - see bower.json and package.json files.  Package.json files are dev only.

* `pip install -r requirements.txt`
* `npm install` (dev only)
* `bower install`

Mongo - follow install instructions on mongo and start it
`mongod`

Everything should work as long as it is running.


Running the web server:
-------------------
`python server.py`

Running the socket server:
`python ws_server.py`

*You will need to start the ws_server _first_ before starting the webserver.

Navigate to `localhost:5000`
