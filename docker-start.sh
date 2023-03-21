#!/bin/bash

echo "\033[32;1;45m Docker starts for production \033[0m";
shift;
docker-compose -f docker-compose.yml up --build prod;