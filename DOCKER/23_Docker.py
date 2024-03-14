### Docker Port Expose ####
/// Apne Container ki agar internet se connect karna chahte ho to kya kre////

hum directly container ko internet se nahi connect kar sakte lkn host connect
karta hai q ki uske pas ip address hta hai,to hume host ke sath container connect
karna padega matlab port expose karna padega to connection establish ho jayga

Container ko hum direclty internet ke sath connect nahi ka rasakte hai bcz 
uski koi public ip nahi hti.

** Login EC2 machine
** sudo su---> yum update -y
** yum install docker -y
** service docker start
** docker run -td --name techserver -p 80:80 ubuntu
d= daemon..matlab srf banake rakho container uske andar mat jao
-p = port ..connect karega container to host 
** docker ps
** docker port techserver = jitne port map hte hai uski detail aa jati hai
** docker exec -it techserver /bin/bash = it is like docker attach command lkn
ye apni alag se process start karta hai=ye contAINER ke andar jata hai
humne uppar docker run mai /bin/bash nahi lagaya tab hum exec hi command use krnge

** apt-get update = ubuntu ko update karne ke liye
** apt-get install apache2 -y = apt is in ubuntu like yum in linux
** cd /var/www/html/
** echo "message" >index.html
** service apche2 start

// diffrence between docker attach and docker exec ???

Docker exec creates a new peocess in the container's envirment while docker attach
just connect thee  standard input /output of the main process inside the container 
to correspoding standard input/output error of current terminal.

Docker exec is specially for running new things in a already started container 
jo process chalti hai uski process id ya parent process id hti h (pid,ppid)

// What is diffrence between exposed and publish  docker??

Basically you have 3 option 
* neither specify expose nor -p
*only specify expose
*specify expose and -p(publish)

1.if u specify neither expose nor -p(publsih), the service in the container will only
be accessible from inside the container itself(isme srf aap container mai
jake access kar sakte hai dusra banda intrnet se access nahi kar sakta)

2. if u expose  port,the service in the container not accessible from outside
the continer but from inside the other docker container ,so this is 
gud for inter container communication(matlab inside of host machine mai jitne
container hai o apas mai communicate kar paynge,docker ke bahar intrnet se nahi kar sakte)

expose matlab open karna ar publish matlab dhindora pitna ki open kia hai 
koi bhi aa sakta hai

3.if u expose and publish a port service, the container in the container
is accessible from anywhere, ever outside docker

if u do  -p but do not expose docker does an iplicit expose ,this is beacause
,if a port is open to the public ,it is automatically also open to the other 
containers, hence -p include expose

