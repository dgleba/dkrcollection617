
FROM python:3.7
WORKDIR /code

# RUN  mkdir -p /pipcache 
# RUN  chown -R "0:33"  /rootzzz
# USER "0:33"

# Install cron
RUN apt-get update && apt-get install -y cron 

ADD requirements.txt /code/
# ADD  --chmod=0755  entrypoint.sh /code/
# ADD  entrypoint.sh /code/

RUN pip install  -r requirements.txt

RUN  chmod -R g+rws  /code

# RUN  chmod -R +x  /code/entrypoint.sh

# use volume in docker-compose..
# COPY . /code/


