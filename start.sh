#!/bin/bash
echo "Creating docker image"
docker build -t mlserver .
#docker tag mlserver:latest mlserver:thisimage
echo "Image created succesfully"
echo "Stopping the current docker containers"