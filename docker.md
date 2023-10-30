# Docker

---

## How to install
#### To avoid sudo:
```bash
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
# Check the user is added to the docker group
$ groups $USER
# Reboot the machine
$ sudo reboot
```
## Main parts
````
Image - readonly not run our program
Container - running program (from the image)
````

# Commands

## Images
#### Build project
```bash
# build from current directory
$ sudo docker build -t registry.big3.ru/oc/default .
# or
$ sudo docker build -t registry.big3.ru/oc/default:latest .
   -t <repository_name (group name)>:<tag_name (name of image inside the group)>
```
```bash
# Observe images
$ docker images
# Just hashes
$ docker images -q

# Delete image
$ docker rmi <image name>

# Delete all unused images
$ docker image prune
```

#### Create docker image
```bash
$ docker build -t <image name> <directory where to get files for the image>
$ docker build -t hello-world .
```

#### Inspect docker image
```bash
$ docker image inspect <image_id or name>
```

## Containers
#### Observe running containers
```bash
# shows running containers
$ docker ps      
# shows all containers
$ docker ps -a   
```

#### Run container (our program) (in attached mode by default - in foreground)
```bash
$ docker run --name <how we will name run container> <name of image>
   -d - option to run container in background (run command into detached mode)
   --rm - removes container itself after it is stopped
   -p 8080:8080 - exposes ports <port on locale machine>:<port in docker container>
   --name <container_name>
$ docker run --name <how we will name run container> <name of image>:<image_tag>
$ docker run --name <how we will name run container> -d --rm <image name>:<image_tag>

# In interactive attached mode
$ docker run -it <container id>
$ docker start -ai <container id>

# Or in detached mode by default (in background):
docker start <name of container>
```

#### Stop container
```bash
$ docker stop <CONTAINER ID or container name>
```

#### Remove container
```bash
$ docker rm <CONTAINER ID or container name> 
$ docker rm $(docker ps -aq)
$ docker rm `docker ps -aq`
```

## Docker volumes
```bash
# Observe volumes
$ docker volume ls
# Remove unused volumes
$ docker volume prune
# Create volume (unnecessary? because if just run 'run' command it will be created automatically)
$ docker volume create <volume name>
$ docker volume create my_web_vol
$ docker run --rm --name web-app -p 8080:8080 -v my_web_vol:/usr/src/app/resources web-app-image
```

## login
```bash
$ sudo docker login --username cadastre -p ZWaQpzSUH58bzyay registry.big3.ru
```

## Copy files into/from containers
```bash
# From local directory to container one
$ docker cp </path/src_file> <container:/path/to>
$ docker cp ./some_file.txt 768051546a1a:/app
# copy whole directory
$ docker cp ./some_dir/. 768051546a1a:/app/some_dir/

# From docker container to local folder
$ docker cp 768051546a1a:/app/some_dir/ some_dir/ 
```


# Docker Compose

---

## Start project
sudo docker compose -f docker-compose-local.yml up

## Commands inside containers
# Via Docker
sudo docker exec -it app-back-main-app-local-1 ./manage.py showmigrations | grep '\[ \]'
sudo docker exec -it app-back-main-app-local-1 ./manage.py migrate
sudo docker exec -it app-back-main-app-local-1 python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'a.dvoeglazov@big3.ru', 'qawsedrf1234');"

# Via docker compose with specified config file
docker-compose -f docker-compose-local.yml run --rm main-app-local sh -c 'python manage.py migrate';
docker-compose -f docker-compose-local.yml run --rm main-app-local sh -c 'python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser("admin", "a.dvoeglazov@big3.ru", "qawsedrf1234")"';
docker-compose -f docker-compose-local.yml run --rm main-app-local sh -c 'python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser("admin", "a.dvoeglazov@big3.ru", "qawsedrf1234");"'


docker-compose -f docker-compose-test.yml run --rm main-app-test python manage.py test --keepdb

## Old docker-compose
sudo mkdir /usr/local/bin/
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


### ps by name
docker ps --format '{{.Names}}'
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Command}}"

### Django debugging in Docker Pycharm
https://testdriven.io/blog/django-debugging-pycharm/


### Database dumps via docker
# Backup your databases
docker exec -t your-db-container pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
docker exec -ti your-db-container pg_dumpall -c -U bot | gzip > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql.gz


# Restore your databases
cat your_dump.sql | docker exec -i your-db-container psql -U postgres

