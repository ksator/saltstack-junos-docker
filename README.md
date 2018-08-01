# requirements 
install docker 

```
sudo apt-get update
sudo apt-get install python-pip -y
pip install pyyaml jinja2
pip list
``` 
# clone the repo
```
git clone
cd 
```
```
vi variables.yml
python render.py
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
alternatively you can run this command 
```
docker run -d -t --name minion2 -p 4705:4505 -p 4706:4506 saltminion-junosproxy

```
# to connect to a container cli
```
docker exec -it master bash
docker exec -it minion1 bash
docker exec -it minion2 bash
```
# to run commands in a container
```
docker exec -it master service salt-master start
docker exec -it minion1 service salt-minion start
docker exec -it master salt-key -L

```
```
docker exec -it master salt minion1 test.ping
docker exec -it master salt "minion1" cmd.run "pwd"


```
```
docker exec -it minion1 salt-proxy -d --proxyid=dc-vmx-3
docker exec -it master salt dc-vmx-3 junos.cli 'show chassis hardware'
dc-vmx-3:
    ----------
    message:

        Hardware inventory:
        Item             Version  Part number  Serial number     Description
        Chassis                                VM58A57C7D13      VMX
        Midplane
        Routing Engine 0                                         RE-VMX
        CB 0                                                     VMX SCB
    out:
        True

```
