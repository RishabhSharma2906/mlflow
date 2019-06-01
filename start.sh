#!/bin/bash
echo "Creating docker image"
docker build -t mlserver:latest .
echo "Image created succesfully"
echo "Stopping the current docker containers"