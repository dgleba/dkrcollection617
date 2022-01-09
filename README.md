
# Bmark616 Mark616

Bookmarking and notes system



# Stop all

```
cd /ap/dkr/dkrcollection617

bash sdownall.sh

cd proxy457h; docker-compose down

```

# Start production

```
bash upprod.sh

cd proxy457h; docker-compose up

```

# development

See upprod.sh for dev section.

```

cd /ap/dkr/dkrcollection617
cd ./bmark616h-yard/vuemarks616/vmark616g/

dev vue:

        bash shdev.sh

build for production:

        bash shb.sh; docker-compose down; docker-compose up

npm install:

        bash shi.sh


bash sh.sh
```


# layout

```
albe@racknerd-4f4016:/ap/dkr/dkrcollection617$ tree -L 3

├── bmark616h-yard

django..
│   ├── dj616b
│   │   ├── docker-compose.prod.yml
│   │   ├── docker-compose.yml

php data (not using it right now)..
│   ├── htmldata605o
│   │   ├── adminer
│   │   ├── html01

mysql db here..
│   ├── php605m
│   │   ├── docker-compose.yml

│   ├── sysdata
│   │   └── mysqldata


│   └── vuemarks616
vue production..
│       ├── docker-compose.yml
│       ├── vmark616g

vue build for production..
│       ├──  ---  shb.sh
vue dev..
│       ├──  ---  shdev.sh

ssl proxy..
├── proxy457h
│   ├── docker-compose.yml

```

