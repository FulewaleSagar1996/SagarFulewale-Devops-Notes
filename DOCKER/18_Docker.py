*********** DOCKER ***********

Container is like a virtual machine
docker is a tool which create this virtual machine
ye opertion ke part mai ataa hai

jab development team koi code likhti hai ar chalati hai lkn whi code
testing team ke pas jate hi nahi chalta hai q ki uske pas o set up nahi hai jo devl team 
ke pas tha,o software nahi tha,supported component nahi the isly
ye comflict dur karne ke liye hum docker use karte hai

hum kuch softeare de skte hai usko lkn ppura OS nahi de sakte hai

hypervisor - jiski help se hum apni virtual mahine banate hai
virtaul machine ko share kar sakte hai uski image banake,o img testing team run karge

virtualization = ek Workstation se multiple virtual machine create karna with the help of 
hypervisor.isme jitna storage WS ke hardware mai hga utna distribute ho  jayga

Docker  = it is a advanced level of virtualization.ye containerization karta hai
hardware-->hypervisor-->multiple virtal machine  (type 1 or bare meatal )
isme har machine pe os install krna padega ar yaha pe apki limit hai ..jitni resources hai utni
isi problem ko solve kia hai docker ne

Hardware -->Operating system--->Docker engine(like hupervisor) --->> Container(VM)
Container ka koi OS nahi hta..hta hai lkn na ke barabar (5%)
Container sab dusro se lega ar jitna use karna hai utna hi lega ar wapas kar dega ar container
band ho jyga..

Container mai sari dependency hti hai jo docker hub se uthata hai

application chalane ke liye jo bhi backend mai lagta hai o puru dependency container
dockoer hub se lata hai ar puri karta hai

***** O.S level Virtualization in docker ******

docker 2013 mai  aya hai and open source
centralised platform designed to create deploy and run application
matlab hum ise kahi bhi chala sakte hai jaha deploy karna ho wha

docker uses container at host os and run application.khud ka os nahi hta lkn host ka hi use karta hai
docker khud ko chalane ke liye linux ka usee karta hai lkn hum ise kisi bhi os mai run kr skte h
ye GO lang mai likha gya hai

docker ye os level virtaulisation karta hai insated of hardware levl virtulisation

Docker is a set of platform as a service that uses os level virtualization whereas vmware uses 
hardware level virtualization

vmware virt.
hardware-->hypervisor-->OS--->VM
sare rsourceas hardware se lega with the help of hypervisor
ye sab hardware se leta hai isly ise hardware virt kahte hai

OS level virt
Hardware-->OS-->docker engine--->container
ye sab chize os se leta hai not from hardware .os mai already 95% filesa hti hai ar baki
files ye docker hub se uthat hai
container is a light weight hti hai
container mai os nahi hta lkn 5% hi hta hai matlab negligible hti hai as a img form 