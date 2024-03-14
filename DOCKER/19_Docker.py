*** Advantages *****
light weight=matlan aisi application jo apki lptop ke kam resources use karti hai
cost kam hti hai
you can reuse the image
no pre allocation of RAM
CI efficiency= docker enables you to build a container image and use that same img
across every steps of the deployment proocess
Container yah ek running stage of image hta hai
container jab stop hta hi tab use hum iamgae karhte hai..deployment mai hum image bhejte 
hai not container,container kabi move nahi krte
it can run on physical hardware or virtual hw or cloud
less time to create container

**** disadvantage *****
cross platform ko support nahi karega
jo application apne window mai banayi hai o linux mai ni chalegi and vice versa
docker is not gud solution for application that requires rich GUI..gud for command line intrfce
difficult to manage large container (ar isko manage karne ke liye fir kubrnetes market m aya)

imp point == docker is suitable when the developement os and testing os are same
if the os is diff we should  use vm
matlab do no trf ubuntu hi rhna chy..ek trf ubuntu ar ek trf cent os nahi rhna chy

///////// Architecture of docker ///////////

developer pahle docker file banyga matlab usko ek aplication banaane ke liye k k 
chy o likht hai..like recipe file im chef
o usme sab apni dependency likhega ki muze chef git githubetc chy krke jise docker file khte h
then us docker fille ko docker engine mai bheja jayga ar o sabhi application
ki ek image create hgi..o image jab run hgi tab use hum container bolege..
ab us image ko hum docker hub mai upload kar denge ar jisko bhi jrurt rhgi o wha se pull
kar lega us img ko..ab o image jaha pe bhi run hgi waha usi tarike ka container create hga,

conatiner hameasha layered mai kam karega(layered file system)
matlab ek ek kam krta rhaga..ek ek download karta hai ek sath nahi hti.o layers mai banata jata h
docker is a ecosystem..malb docker bht sare software ka combination hta hai

/////// DOCKER ECOSYTEM ///////
sare tools banke ek container banata hai===set of sw and tools
it include
docker client = jispe ap kam krte hai,docker file ya code banate hai
docker engine/server/daeman..= ye hamri image se container banata hai
docker hub = it is like register of all image
docker image = jisse conatainer banaya jata hai, its like template
docker compose = 

DOCKER DAEMON = its like a chef server.it is run on host os
it is responsible for running container

DOCKER CLIENT = docker users can interact with docker server through client(cli)
it uses command and rest api to communicate with server/daemon
it is possible for docker client to communicate eith the more than one daemon

DOCKER HOST = it is used to provide enviormnrt to execute and run the application. it 
contains evertyhing

DOCKER HUB = docker registry manages and stores the docker engine
thesee are two types of registries in the docker
publiic registry and private registry.

DOCKER IMAGES = docker images are the read only binary template that create ur container
 OR single file with all dependencies and confuguration req to run a program
 
 WAYS TO CREATE  AN IMAGES / INTRVIEW QUE
 
 1. TAKE IMAGE FROM DOCKER HUB / IMAGE LE SAKTE HAI
 2. CREATE IMAGE FORM DOCKER FILE
 3. CREATE IMAGE FROM EXISTING DOCKER CONTAINER
 
 DoCKER CONTAINER = container hold the all package that run the appliction
 in other words we can say that the image is a template and the conatiner copy of that img
 imageas become container when it runs
 container is a like virtual machine