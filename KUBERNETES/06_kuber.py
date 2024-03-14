###### DEPLOYMENT #########

wE are not deploy a pod..we deploy a deployment


interview que
diffrence between container, pod and deployment 
in container by command like docker run -it image name -p  and all 
but in pod only yaml file is there..it is running specification.in one pod we can 
locate multiple container also which is not recommanded .
deployment as conntainer using pod  offers autoscaling and autohealing
pod is nothing but the container ony it is running specifcation diffent and 
multiple conatainer in pod
do not create pod direclty..but create as a deployment resources.
deployment creats replica set  which is ur kubernetes contoller.

controller ensures desired no of replica set or pod in deployment 
replica set hamesha ensure karta haiki jitne bole hai utne pod hai ya nahi..
replica set yah k8s controller hai...there are lots of controller.
contoller hamesha desired state maintain karta hai as actual controller.

what is diff between depl and replica set 
--- replica set yah ek k8 controller hi hta haijo autohelaing krta hai.
matlab agar koi pod kill ho gya to create jkarta hai.

deployment ---->replicaset------->pods
deployment karte hai toh replica set bnta hai ar whi direclty pod create karta hhau ar yhi recommanded hta hai


#### SERVICEEEEEEEEEE ##### 

once you depoy a deployment..for each deployment u create a service most of the time in production..i means always

If theres is no servicesss

**** agar hum deployment kar rae hai..jisme 3 replica set haai..agr by any reaason koi pod dlt
hta hai toh usme with the help of auto healing uske jagh pe new pod create hta hai q ki 
hum deployment hi kar rahe hai(depoyment.yml)...lkn jo pod dkt hta hai uski ip adress alag hti hai
ar jo create hta hai uski alag hti hai...abbbb agarrrrr service yah concept nahi rhga tohh????/

so top of deploment u create service...servic act as a load balancer (kubeproxy)
we have to access not to ip but by servicess adresss
agar autohelaing ar autoscaling hta fr bhi without service hum k8s nai koi kam nahi kr sakte 
q ki kisi ko access hta ya kisi ko nahi ho pata due to ip adresss..

service benefitsssss------- load balancing karta hai (pod also difficult to track with ip adress)
--------- service discovery (lables and selectors)(service also difficult to track ip adress )
--------- expose to extrnal worldddddd 
(agar hume koi application access karni hai with kops,minikube etc toh hum ssh ip adress karke
 use dekh sakte hai lkn kya hum apne client ko bol sakte hai kya..koi bhi n=hume yah krne k liye 
 nhi kahta in real world also....service can allow to acess ur application outside k8s)

 services typessssss
 1.cluster ip (by default..inside the k8 cluture..jisme srf discovery ar load blncng milega)
 2.nodport(isme application inside organisation mai jo hai o access kar paynge)
 3.load balancer(service will expose to extrnal worlddddddddddddd)

 workfloww------
 ---k8s----- ke andar---------worker nodee1---ke andar-------
 depolyment------->replicaset---->pod<<<------------service watch kar rah hai pod ko 
 
 agar service--as a load balcer mai hai to with the help of public ip adress o bahar ke 
 world ko acess kar oayga puri application....samj lo k8s hmara aws pe haii,,,,eks mai...
 usme ELB rahta hai jo public ip adress dega ar o contoll karega cloud controller manager jo 
 k8s ke master plane ka component hai...ccm ip adress generate karega with the help of aws ELB.
 
 

