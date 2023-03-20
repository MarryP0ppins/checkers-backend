#!/bin/bash

if [ "$1" = "prod" ]
  then
    echo "\033[32;1;45m Docker starts for production \033[0m";
    shift;
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build "$@";
else
    echo "\033[32;1;45m Docker starts for development \033[0m";
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build "$@";
fi
