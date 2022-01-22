
# Bmark616 Mark616

Bookmarking and notes system



# Import newer from shaarli

```
albe@racknerd-4f4016:/ap/dkr/dkrcollection617a/bmark616h-yard/php605m$    python3 script/import-shaar-api.py


insert ignore into mark616_bookmk 
( title,url,      body,    created_at,                                                         tagtext, id_shaarli, bhash    ) select
  title,url,description, CONVERT_TZ( CAST(created AS DATETIME), @@session.time_zone, '+00:00' ) ,tags,    id,      "from_imp_shaar_api" 
  from imp_shaar_api  a
  where a.id>10430
-- limit 1

check for duplicates..


SELECT id_shaarli, title, count(id_shaarli)
FROM `mark616_bookmk`
group by (id_shaarli), title
ORDER BY count(id_shaarli) DESC
LIMIT 11


```




# Stop all

```
cd /ap/dkr/dkrcollection617a

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

# dev vue:

        bash shdev.sh

# build for production:

        bash shb.sh; docker-compose down; docker-compose up

# npm install:

        bash shi.sh


bash sh.sh
```

# Change version in ...

BookmkIndexComponent.vue
public/service.worker.js
public/manifest.json


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

