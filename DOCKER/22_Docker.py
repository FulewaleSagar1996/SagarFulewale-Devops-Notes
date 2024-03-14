## DOCKER VOLUME ##

Volume = volumne yah ek directory hai jo hum container ke andar create kr sakate hai ar 
container to container share bhi kar sakte hai.ye dockerfile ke wqt hi baana sakte hai.ar hum
jis bhi container mai volume chnge krnge to jis bhi container ke sath humne volume share kia
hai un sabko changes nzr aynge

volume dlt nahi hta..agr container dlt bhi ho jaye to.
host to container bhi volume sahre kar sakte hai

**Volume is simply directory inside our container.
**Finally , we have to declare the directory as a volume and share volume
**even if we stop container , still we can access volume
**u can declare a directory as a volume only while creating a container
**youo cannot create volume from existing continer
**you can share one volume across any no of container
**volume will not be included when you updates on image
**ypu cam mapped volume in two ways
1.continer to container
2.host to container

Benefits-
decoupling container from storage - 
share volume among diffrent container
attach volume to containers
on deleting containers volume does not delete

## LAB OF VOLUME ###
## how to create  volume with the help of Dockerfile

** Create Dockerfile and write
FROM ubuntu
VOLUME ["/myvolume1"]

** then create image from dockerfile
docker build -t myimage . 

** now create a container from this image and run
docker run -it --name container1 myimage /bin/bash

** Now do ls, you can see myvolume1
**cd myvolume1
** create files = touch filex filey filez
** ls
** exit

** Now share volume with another container so create container2
docker run -it --name container2 --privileged=true --volumes-from container1 ubuntu /bin/bash
 
** Now after creating container2 , myvolume1 is visible whatever you do in one volume,you
can see from other volume

** ls
** cd myvolume1/
** exit

docker start container1
docker attach container1
cd myvolume1
ls
you can see samplefile here


## How to create volume with the help of Command line

docker run -it --name container3 -v /volume2 ubuntu /bin/bash
do ls
cd volume2
now create file and exit

Now create one more container and share one volume2

docker run-it --name container4 --privileged=true --volumes-from container3 ubuntu /bin/bash

Now you are inside container,do ls you can see volume2
cd volume2
Now create one file indside this volume and then check in container3 ,u can see that files

## Volume ( Host <--------> Container)

Verify files in /home/ec2-user ec2 user is directory

Docker run -it --name hostcont -v /home/ec2-user:/rajput --privileged=true ubuntu /bin/bash

: ka matlab host ko container ke directory ke sath jod do, : ke pahle wal part host ar bad wala container
-v = as a volume connect kar do

cd rajput
do ls now you can see all files of host machine

touch rajputfile (in container)
now check in ec2 machine, you can see this files

## SOME OTHER COMMANDS ### INTERVIEW MAI PUCHI JA SKTI HAI

docker volume ls = jitni volume create hgi locally o nazr aynge
docker volume create <volumename> = apne machine pe bhi direclty volume create karsakte hai
docker volume rm <volumename> = for delete
docker volume prune = jo unused h o dlt ho jaynge
docker volume inspect <volumename> = isse volume ki info aygi
docker continer inspect <containername> = container ki info 