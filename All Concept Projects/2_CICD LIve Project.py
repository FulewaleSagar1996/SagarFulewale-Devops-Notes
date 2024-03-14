

CICD CLASSS 1///////////////////////

HERE..COMPARISION BETWEEN JENKIN AND K8..MEANS PAHLE HUM DEPLOY JENKINS KE WORKERNODE MAI HI KARTE THE...
LKN AB K8S MAI KRTE HAI Q KI YE HIGLY SCALABLE HAI...


there arew many env like dev, staging, or qe/qa and preproduction or UAT and then production....
from jenkins firste we have to deploy in dev(1master 1 worker) env if automaticlly approved then QAQE or staging 
(here we can used 3 master 5 node) nd then production (3 master 20 or something else nodes) 

In lEgacy jenkins...what we did,,, there are no of microservices so we cannot run pipeline in  only in jenkis master server
bcz moslty we used master for configured only so we create multiple jenkins slave means ec2 instances and for everychanges 
each ec2 instances have their pipeline...there are team and we give access to each team to each ec2 jenkins server for pipeline

these setup is very humangus....compute is very coslty...and if u keep added ec2 it is cosly and not to managed..so we can 
add autoscaling group but we are talking about real time so it is not good practise
if u want to scale zerooooo...then for zero code changes we dont want any node then what to dooooo....
in such case jenkins nodes /slave/ec2 instances not to use....
so we use k8s for deployment.
matlab agar koi changes commit nahi hua hai to fir utne der tak ke liye mera server band rahna chy lkn jenkins
slave mai jo ec2 instances ke upper hum deloy karte hai usme aisa kuch nahi hta...o chaalte hi rahta hai to fir isse hamari cost,
uaksa maintaninace,configuered karne ka load sa increase hta hai...

hum k8s ke github ka example le sakte hai...see the last pull req.
k8s khud jenkins ke badle github action used karta hai.jisme runner hta hai jo slave or worker node ka kam karta hai
o hamre liye server ready karta hai..jo hume pata bhi nahi hta kaha hai karke...
so 77 repository ke liye hum common server use kar sakte hai ar yaha 77 repo mai jo bhi change hga...so u can create 
k8s pod in k8s cluster..kam krne ke bad o khud dlt hga ar dusre ke liye kam mai ayga 

so in that way...instead of using so many instances or worker node we can use one common github action ..where multiple peope in
ur organisation or multiple project in org saave ur reaources ....this is modern day approach..

it is scalable....


