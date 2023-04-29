#!/bin/bash

# Run Flask app in the background
nohup flask run &

# Wait for Flask app to start
sleep 5

# Execute initdb script
python init_db.py
