#!/bin/bash

CHROME_VERSION=$(google-chrome --version | sed -n "s/^Google Chrome \([0-9]*\).\([0-9]*\).\([0-9]*\).*/\1/p")
CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}`

wget -N http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip -P ~/
unzip -o ~/chromedriver_linux64.zip -d /usr/local/bin/
rm ~/chromedriver_linux64.zip
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver
