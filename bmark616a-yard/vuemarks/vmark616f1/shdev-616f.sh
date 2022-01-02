

# see .env for vars..
    # export nodeimg='node:14.15-slim'
    # export proj=vue-eg-552cfab
    # export devport=14331

source ./.env

# run developmet (dev) server:

  docker run --name sh-dev_vmark616fdev_021 --rm -v "${PWD}:/$(basename `pwd`)" -w "/$(basename `pwd`)" -p $devport:8080  \
      -e     "VIRTUAL_HOST=vmark616fdev.198.23.238.244.nip.io" \
      -e "LETSENCRYPT_HOST=vmark616fdev.198.23.238.244.nip.io" \
      -e "VIRTUAL_PORT=8080" \
      -e "LETSENCRYPT_EMAIL=dgleba@gmail.com" \
    --network=sister \
    -it  $nodeimg sh -c "npm run serve --public 198.23.238.244:8080"



