# requirements 

## intall these dependencies 

```
sudo apt-get update
sudo apt-get install python-pip -y
pip install pyyaml jinja2
pip list
``` 


## install docker 

Check if Docker is already installed 
```
$ docker --version
```

If it was not already installed, install it. Here's how to install in on Ubuntu 16.04:  
```
$ sudo apt-get update
```
```
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```
```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```
```
$ sudo apt-get update
```
```
$ sudo apt-get install docker-ce
```
```
$ sudo docker run hello-world
```
```
$ sudo groupadd docker
```
```
$ sudo usermod -aG docker $USER
```

Exit the ssh session to your ubuntu and open an new ssh session to your ubuntu and run these commands to verify you installed Docker properly:  
```
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```
```
$ docker --version
Docker version 18.03.1-ce, build 9ee9f40
```

# clone the repo
```
git clone https://github.com/ksator/saltstack-junos-docker.git
cd saltstack-junos-docker
```
# update the variables 
```
vi variables.yml
```
# Run this script to create saltstack files 
```
python render.py
```

# create a docker image for the master and junos-syslog-engine dependencies
```
cd master
sudo docker build -t saltmaster-junossyslog .
```
```
docker images
```
# instanciate a docker container for the master 
```
docker run -d -t --rm --name master -p 516:516/udp -p 4505:4505 -p 4506:4506 saltmaster-junossyslog 
```
```
docker ps
```
# create a docker image for the minion and junos modules dependencies
```
cd ../minion
sudo docker build -t saltminion-junosproxy .
```
```
docker images
```
# instanciate a a docker container for the minion
```
docker run -d -t --rm --name minion1 -p 4605:4505 -p 4606:4506 saltminion-junosproxy
```
```
docker ps
```
alternatively you can run this command (so the container wont be deleted if you stop it)
```
docker run -d -t --name minion1 -p 4605:4505 -p 4606:4506 saltminion-junosproxy
```
# run these commands to start the salt service
```
docker exec -it master service salt-master start
docker exec -it minion1 service salt-minion start
```
# to connect to a container cli
```
docker exec -it master bash
exit
```
```
docker exec -it minion1 bash
exit
```
# Verify the setup works
```
docker exec -it master salt-key -L
docker exec -it master salt minion1 test.ping
docker exec -it master salt "minion1" cmd.run "pwd"
```
```
docker exec -it minion1 salt-proxy -d --proxyid=dc-vmx-3
docker exec -it master salt dc-vmx-3 junos.cli 'show chassis hardware'
```
```
docker exec -it master salt 'dc-vmx-3' state.apply syslog
```

# Verify the junos syslog engine 
```
docker exec -it master bash
salt-run state.event pretty=True
```
ssh the junos device dc-vmx-3 and commit a configuration change and watch the event bus on the master

