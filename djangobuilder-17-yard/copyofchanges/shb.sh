
# see django_builder readme.md


# see .env for vars..
    # export nodeimg='node:14.15-slim'
    # export proj=vue-eg-552cfab
    # export devport=14331

set -vx

source ./.env.development.local

# install..

#docker run --rm -v "${PWD}:/$(basename `pwd`)" -w "/$(basename `pwd`)" -p $devport:8080 -it  $nodeimg sh -c " npm install --save /vmark616f1/198.23.238.244:8080"

# docker run --rm -v "${PWD}:/$(basename `pwd`)" -w "/$(basename `pwd`)"  -it  $nodeimg sh -c "yarn build --mode=production"

docker run --rm -v "${PWD}:/$(basename `pwd`)" -w "/$(basename `pwd`)"  -it  $nodeimg sh -c "yarn build --mode=development"

