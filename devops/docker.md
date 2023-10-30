# Docker

---

## How to install
#### To avoid sudo:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
# Check the user is added to the docker group
groups $USER
# Reboot the machine
sudo reboot
```
## Main parts
```
Image - readonly not run our program
Container - running program (from the image)
```

# Commands

## Images
#### Build project
```bash
# build from current directory
docker build -t registry.big3.ru/oc/default .
# or
docker build -t registry.big3.ru/oc/default:latest . -t <repository_name (group name)>:<tag_name (name of image inside the group)>
```
```bash
# Observe images
docker images
# Just hashes
docker images -q

# Delete image
docker rmi <image name>

# Delete all unused images
docker image prune
```

#### Create docker image
```bash
docker build -t <image name> <directory where to get files for the image>
docker build -t hello-world .
```

#### Inspect docker image
```bash
docker image inspect <image_id or name>
```

## Containers
#### ps by name
```bash
docker ps --format '{{.Names}}'
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Command}}"
```

#### Observe running containers
```bash
# shows running containers
docker ps      
# shows all containers
docker ps -a   
```

#### Run container (our program) (in attached mode by default - in foreground)
```bash
docker run --name <how we will name run container> <name of image>
   -d - option to run container in background (run command into detached mode)
   --rm - removes container itself after it is stopped
   -p 8080:8080 - exposes ports <port on locale machine>:<port in docker container>
   --name <container_name>
docker run --name <how we will name run container> <name of image>:<image_tag>
docker run --name <how we will name run container> -d --rm <image name>:<image_tag>

# In interactive attached mode
docker run -it <container id>
docker start -ai <container id>

# Or in detached mode by default (in background):
docker start <name of container>
```

#### Stop container
```bash
docker stop <CONTAINER ID or container name>
```

#### Remove container
```bash
docker rm <CONTAINER ID or container name> 
docker rm $(docker ps -aq)
docker rm `docker ps -aq`
```

## Docker volumes
```bash
# Observe volumes
docker volume ls
# Remove unused volumes
docker volume prune
# Create volume (unnecessary? because if just run 'run' command it will be created automatically)
docker volume create <volume name>
docker volume create my_web_vol
docker run --rm --name web-app -p 8080:8080 -v my_web_vol:/usr/src/app/resources web-app-image
```

## login
```bash
sudo docker login --username cadastre -p ZWaQpzSUH58bzyay registry.big3.ru
```

## Copy files into/from containers
```bash
# From local directory to container one
docker cp </path/src_file> <container:/path/to>
docker cp ./some_file.txt 768051546a1a:/app
# copy whole directory
docker cp ./some_dir/. 768051546a1a:/app/some_dir/

# From docker container to local folder
docker cp 768051546a1a:/app/some_dir/ some_dir/ 
```


# Docker Compose


### Start project
```bash
sudo docker compose -f docker-compose-local.yml up
```

### Commands inside containers
#### Via Docker
```bash
sudo docker exec -it app-back-main-app-local-1 ./manage.py showmigrations | grep '\[ \]'
sudo docker exec -it app-back-main-app-local-1 ./manage.py migrate
sudo docker exec -it app-back-main-app-local-1 python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'a.dvoeglazov@big3.ru', 'qawsedrf1234');"
```

#### Via docker compose with specified config file
```bash
docker-compose -f docker-compose-local.yml run --rm main-app-local sh -c 'python manage.py migrate';
docker-compose -f docker-compose-local.yml run --rm main-app-local sh -c 'python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser("admin", "a.dvoeglazov@big3.ru", "qawsedrf1234")"';
docker-compose -f docker-compose-local.yml run --rm main-app-local sh -c 'python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser("admin", "a.dvoeglazov@big3.ru", "qawsedrf1234");"'

docker-compose -f docker-compose-test.yml run --rm main-app-test python manage.py test --keepdb
```

#### Old docker-compose
```bash
sudo mkdir /usr/local/bin/
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

#### ps by name
```bash
docker ps --format '{{.Names}}'
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Command}}"
```

### Django debugging in Docker Pycharm
https://testdriven.io/blog/django-debugging-pycharm/


### Docker release unused memory
```bash
docker system prune
```

### Restart all containers
```bash
systemctl restart docker.service
```

### Update container
```bash
docker service update --publish-add 5433:5432 dev_primary_postgis

docker service update --force constructor_edo-bus-listener && docker service update --force constructor_main-bus
```

### Create image from container
```bash
docker commit <container_name> <image_name>
docker commit db-test local-db-test
```

### Statistic
```bash
docker stats
# or for specific containers
docker stats container1 container2 etc
```

### logs
```bash
docker logs 2>&1 | less
```

# SWARM 
#### to fix unit tests
```bash
docker stack rm teststack
# if it is not possible to remove
docker service restart

docker service scale <service>=<number> # 0 - means all containers turned off
```

#### logs from service
```bash
docker service logs <service>
docker service logs constructor_main-app
```

```bash
docker service update --force <service_name>
docker service update --force constructor_main-bus
docker service update --force celery_celery
```

#### Dockerfile - a-la docker config
```bash
# Commands:
FROM - setup image (* python:3.9 - image includes python3.9)
RUN - runs command which should be executed (* mkdir -p /usr/src/app/)
WORKDIR - changes directory (* WORKDIR /usr/src/app/)
COPY - copies from out local machine into container (* COPY . /usr/src/app/)
CMD - tells what conainer has to do when it is started (* CMD ["python", "my_app.py"] ) - runs through shell
ENTRYPOINT - tells what conainer has to do when it is started (* CMD ["python", "my_app.py"] ) - runs without shell
EXPOSE 8080 - exposes the port which the app is run on
ENV - environment variable (* ENV TZ Europe/Moscow) or via "docker run -e " command

# each above command create a layer, so any image consists of many layers
```


# Database dumps via docker
### Backup your databases
```bash
docker exec -t your-db-container pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
docker exec -ti your-db-container pg_dumpall -c -U bot | gzip > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql.gz

docker exec -t test_primary_postgis.1.4l08d0p4l4p3op2q3bdo4lzos pg_dump bot -cCbx -U bot | gzip > dum_`date +%d-%m-%Y"_"%H_%M_%S`.sql.gz
```

#### OR
```bash
env PGPASSWORD=7AZ2tWVApnJRbNUFoj4s pg_dump -h 127.0.0.1 -p 5432 -U bot -d bot > my_db_dump.sql
env PGPASSWORD=7AZ2tWVApnJRbNUFoj4s pg_dump -h 127.0.0.1 -p 5432 -U bot -Fc -d bot > my_local_dump.dump

env PGPASSWORD=7AZ2tWVApnJRbNUFoj4s pg_dump -h 127.0.0.1 -p 5432 -U bot -d bot > my_db_dump.sql

env PGPASSWORD=7AZ2tWVApnJRbNUFoj4s psql -h 127.0.0.1 -p 5432 -U bot -d bot

#### Then restore
pg_restore -U bot -d bot my_local_dump.dump
```

### Restore your databases
```bash
cat your_dump.sql | docker exec -i your-db-container psql -U postgres
```

#### Another way
```bash
docker exec -it db bash
dropdb -U bot bot
createdb -U bot bot
psql -h 127.0.0.1 -p 5432 -U bot -d bot < ../data/dump_20_09_2022/data.sql


#### Restore your databases
cat your_dump.sql | docker exec -i your-db-container psql -U postgres
```
