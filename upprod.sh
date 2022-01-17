#!/usr/bin/env bash

date1=$(date +"__%Y.%m.%d_%H.%M.%S"); echo $date1

cd /ap/dkr/dkrcollection617a

docker-compose -f ./bmark616h-yard/dj616b/docker-compose.prod.yml up -d djprod 

docker-compose -f ./bmark616h-yard/php605m/docker-compose.yml     up -d dbm 

docker-compose -f ./bmark616h-yard/vuemarks616/docker-compose.yml up -d vmg



devup() {

# dev

docker-compose -f ./bmark616h-yard/php605m/docker-compose.yml     up -d adminer php

#django dev

docker-compose -f ./bmark616h-yard/dj616b/docker-compose.yml      up -d 


# dev vue

cd /ap/dkr/dkrcollection617
cd ./bmark616h-yard/vuemarks616/vmark616g
bash shdev.sh

}

