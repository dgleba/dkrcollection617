#!/usr/bin/env bash

date1=$(date +"__%Y.%m.%d_%H.%M.%S"); echo $date1

cd /ap/dkr/dkrcollection617a

docker-compose -f ./bmark616h-yard/dj616b/docker-compose.prod.yml down  

docker-compose -f ./bmark616h-yard/php605m/docker-compose.yml     down  


docker-compose -f ./bmark616h-yard/vuemarks616/docker-compose.yml down 

docker-compose -f ./bmark616h-yard/php605m/docker-compose.yml    down
docker-compose -f ./bmark616h-yard/dj616b/docker-compose.yml     down

ddsc() { echo 'dsc-v4 -- stop container by name' ; docker ps | grep $1 | awk '{print $1}' | xargs docker stop; }

ddsc sh-dev_vmark616-g-dev_021




devdown() {
# dev

docker-compose -f ./bmark616h-yard/php605m/docker-compose.yml    down
docker-compose -f ./bmark616h-yard/dj616b/docker-compose.yml     down
docker-compose -f ./bmark616h-yard/dj616b/docker-compose.yml     restart

ddsc() { echo 'dsc-v4 -- stop container by name' ; docker ps | grep $1 | awk '{print $1}' | xargs docker stop; }

ddsc sh-dev_vmark616-g-dev_021

}




