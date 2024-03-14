***** Docker components and diffrent commands ****

** login into aws acoount and start ur ec2 instance 

//now we have to create container from our own image,therefore create one container first 
** docker run -it --name sagar(containername) ubuntu /bin/bash

** cd tmp/ = ye bu defailt file hai jo creeate ho jati hai
** now create one file inside this tmp directory = touch myfile

//Now if u want to see the diff between the base image and changes on it then
docker diff sagar (containername) = hum apni base image or container create karne ke bad jo 
bhi chnge add delete karnge o isse nzr ayga

// Now create image of this container 
** docker commit newcontainer(containername) updateimage(imagename) = jab bbhi ap 
commit likhte hia matlab ap container  ki image bana rahe ho

//docker images
now create container from the image
** docker run -it --name rajconatiner updateimage /bin/bash

@@@@ isme actualy ho aisa raha hai ki , pahle hum apna container bana rahe hai..us container
ke default folder or directory mai apni new files create kar rahe hai.ab us container
ko hum image bana rahe hai with commit command..ab ye image hum docker hub mai push kar sakte
taki dusro ko ye kam firse na karna pade.to fir hum push kar te hai dockerhub mai
waha se koi pull karke usi image ka container banata hai waith diffrent name (container)
ar us container mai o nazr ayga jo file humne already pahle bana rakhi hai @@@@@@

#### DOCKERFILE ######
Dockerfle is basically a text file it contains some set of instruction
Automation of docker image creation
odcker file ko create karne ka nam b default Docker file hi hga and D capital
it is important commands for interviews

# DOCKER COMPONENTS 

FROM = for base image. this command must be on the top of dockerfile
matlab hame apne conatiner mai konsa os chy ubuntu or something else.ye hamesha first command h

RUN = to execute the command, it will create a layer in image
matlab layer se kam karega,,layered mai doenload karega kisi bhi software ko

MAINTAINER = Author/owner description..info dee skati hai kisne banai hai krke

COPY = is command se ap apni local machine se kuch bhi copy kar sakte hai
copy files from local system.but cannot download from the intrnet

ADD = similar to copy but it provides a feature to download files from intrnet,also we
etract or unzip file at docker imaige side

EXPOSE = to export port suchas port 8080 for tomcat

WORKDIR = to set working directory for a conatiner..agar ap workdirectory set kar denge to
container open karne ke bad ap direcly waha hi poahoch jaynge

CMD = execute command but during conatiner creation..

ENTRYPOINT = similar to CMD,but has higher priority over CMD ,first command will be
executed by ENTRYPPOINT only

ENV = Enviornment variables  jaise key value pair jaise

ARG = 

### LAB OF DOCKERFILE ####
1.create a file with Dockerfile name
2.add instruction in dockerfile like workstation in chef
3.build dockerfile to create image
4.Run image to create container

vi Dockerfile 
FROM ubuntu 
RUN echo "Technical guftugu" >/tmp/testfile

**To create image out of dockerfile 
docker build -t(tag) myimg .  = dockerfile se image bana sakte ho. (.) current file
docker ps -a 
docker images = images dekhne ke liye
now create container from the images = docker run -it --name mycontainer myimg /bin/bash

cat /tmp/testfile = check karne ke liye



