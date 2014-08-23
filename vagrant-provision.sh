#!/usr/bin/env bash

# mongodb install as per http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list

# System installs
apt-get update
apt-get -y install mongodb-org
apt-get -y install python-dev
apt-get -y install python-pip
apt-get -y install nodejs
ln -s /usr/bin/nodejs /usr/bin/node
apt-get -y install npm
npm install -g bower
npm install -g grunt-cli
apt-get -y install ruby2.0
gem install bundler

# Python packages
pip install -r /vagrant/requirements.txt

# Bower packages
cd /vagrant/ && bower install

# npm packages
cd /vagrant/ && npm install

# Ruby packages
cd /vagrant/ && bundle install
