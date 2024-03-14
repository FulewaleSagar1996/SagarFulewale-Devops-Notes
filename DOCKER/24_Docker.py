///How to push docker image to docker hub ///

hume ek host pe container banana hai,us container pe 100 software dalna
hai ar uski image create karna hai.uske bad o image docker hub pe push karna hai
ab wahi kam kisi ar ko bhi karna hai toh hum use apni docker id and image name
bata denge.to o docker hub se pull kar lega us image ko ar jab us image
se container bnayaga to use sabhi 100 software dikh jaynge jo humne install kia tha

hum jo image ko docker hub mai dalte hai use priavte bhi karnge

--- login aws account
--- sudo du
--- yum update -y
--- yum insatll docker -y
--- service docker start 
--- docker run -it ubuntu  /bin/bash
now, create some files inside container and now create image from this container
--- docker commit container1 image1 = contaier ki image bana rahe hai
Now, create account on hub.docker.com

now go to ec2 insatnce
--- docker login = enter ur username and password
now give tag to ur image
--- docker tag imahge1 dockerid/newimage
---docker push dockerid/newimage

now u can see this image in docker hub account 
now create one insatnce in tokyo region and pull image from hub\\

---docker pull dockerid/newimage
---docker run -it --name mycont dockerid/newimage /bin/bash

//// Some important commands///

docker stop $(docker ps -a -q) = stop all running conainers
docker all stopped containers = docker rm $ (docker ps -a -q)
docker rmi -f $(docker images -q) = delete all images


version of docker i used = 20.10.17