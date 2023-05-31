
# http://192.168.88.55:8080
# https://djbuilder17dev.198.144.183.160.nip.io



# see .env for vars..
    # export nodeimg='node:14.15-slim'
    # export proj=vue-eg-552cfab
    # export devport=14331

source ./.env.development.local

# run developmet (dev) server:

  docker run --name sh-dev_djbuilder17 --rm -v "${PWD}:/$(basename `pwd`)" -w "/$(basename `pwd`)" -p $devport:8080  \
      -e     "VIRTUAL_HOST=djbuilder17dev.198.144.183.160.nip.io" \
      -e "LETSENCRYPT_HOST=djbuilder17dev.198.144.183.160.nip.io" \
      -e "VIRTUAL_PORT=8080" \
      -e "LETSENCRYPT_EMAIL=dgleba@gmail.com" \
    --network=sister \
    -it  $nodeimg sh -c "yarn  dev --host 0.0.0.0 "


# notes..
    # see vue.config.js instead..    
    # -it  $nodeimg sh -c "npm run serve --allowed-hosts all --host 0.0.0.0 --public host211220-1121.enwebhost.net:8081 "
    # -it  $nodeimg sh -c "npx webpack serve --allowed-hosts all --port 8081 "
    # -it  $nodeimg sh -c "npm run serve --host 198.144.183.160 --port 8081"


