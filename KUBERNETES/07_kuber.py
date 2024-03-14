## INGRESS ### **************

Why Ingress is needed?/

2015 ke phle ingress tha hi nahi...people srf deployment---rs---pod---service tak use karte the

jab log virtuao machine pe app deploy krte the tab waha load balacning kartae the with the use of
nginx,f5 (enterprise based load balancer)

---tab ratio based,sticky session,path,domain,black and white listing load balncer karte the
---lkn jab k8 o log transfer hue tab unhe pata laga ki load balncer hai lkn bht simple hai..round
robin technology...matlab req aye hai to 5 5 mai devide karna....kuch bhi features nahi the jo pahle
use karte the log in vm
---dusra pronlem ye tha ki 100services ke liye 100 load balcning with static ip adress
ar uska charges cloud providing company leti thi

********what is problems
1.Enterprise and TLS load balcncer 
not getting sticky,tLs,path,ratiobased capabilities
2.if u create service type load balncer for each service then cloud providing company charges u 
if there is 1000s of services then cloud provider charges u for 1000s static ip adress load balnce

///// what is diff betn service type load balcing and traditional k8 ingress ??????(interview)

******* HOW INGRESSS SOLVE THIS PROBLEMS

--- k8 finds a solutions on that...they implement ingress
----they told k8s people create ingress resources and also inform to top load balcncer people like
nginx,f5,traffic,ambassador,HA proxy to create ingress controller seperately 

lets consider, agar hume path basese load balncing hona in k8s jo ki by default k8s mai nahi hti
tab hum k8s mai ingress resources create karte hai...lkn isse kuch nahi hga...
ingress controller control krta hai ingress resources ko deploy karne k liye...ingress controller
khud load balcning company banati hai khud ka....
jaise jab hum pod banate hai lkn us pod ko deploy kublet karta hai ya fir whi controll karta hai
jaise koi service.yml file hum banate hai to usme ip table routes update hta hai ar o kubeproxy krta hai
wse hi yaha ingress controller hta hai for ingress resources.

---user will create ingress res and load balcning comp(nginx) write their infgress controller anf 
they places their controller into github anfd they guide or provide u how to install ingress comntroller
using helm charts or any other ways...and also as a we user not only create ingress res but also install
 ingress controller...ingress controller is nothuing but the load balcer...
 
which ingress controller we have to use it is depends on organisation..that which load balcing they used earlier


