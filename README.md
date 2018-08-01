# requirements 
install docker  
# clone the repo
```
git clone
cd 
```
# master 
create a docker image
```
cd master
sudo docker build -t saltmaster-junossyslog .
docker images
```
instanciate a docker container
```
docker run -d -t --rm --name master -p 516:516/udp -p 4505:4505 -p 4506:4506 saltmaster-junossyslog 
docker ps
```
# minion
create a docker image 
```
cd
cd minion
sudo docker build -t saltminion-junosproxy .
docker images
```
instanciate docker containers 
```
docker run -d -t --rm --name minion1 -p 4605:4505 -p 4606:4506 saltminion-junosproxy
docker run -d -t --rm --name minion2 -p 4705:4505 -p 4706:4506 saltminion-junosproxy 
docker ps
```
# to jump in a container 
```
docker exec -it master bash
docker exec -it minion1 bash
docker exec -it minion2 bash
```

