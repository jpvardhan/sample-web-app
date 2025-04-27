#!/bin/bash
cd /var/www/html/sample-web-app 
sudo python3 app.py > app.log 2>&1 &