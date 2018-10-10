#!/bin/bash

docker-compose down --remove-orphans --volumes
#docker volume rm $(docker volume list -q)  
