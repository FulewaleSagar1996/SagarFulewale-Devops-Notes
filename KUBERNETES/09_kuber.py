********CUSTOM RESOURCES 

1.CRD-CUSTOM RES DEFINATION
2.CR..CUSTOM RES
3.CUSTOM CONTROLLER

WHY?????
AGAR HUME NEW RESOURCES INTRODUCE KARNEA HAI K8S MAI LIKE ARGOCD,FLUX OR KEYCLOCK
ISLY CR,crd,cc USE KARTE HAI
there are so many resources

IF u want to extend the api of k8s to introduce resources we used this

yaha 2 actor hote hai....
devops engg( he deploy CRD AND CC,CR ALSO)
user (CR )

agr koi bolta hai ki k8s explore karye hai to usme 
ISTIO--which add service based capabilitiees add karta hai
agrocd-- gitops add karta hai
keyclock--provide tight identity acess mangment

thise allll....which enhances behaviour of k8s clusture

so many resources are there in market so how we add in k8s.
ab in sabhi resources ka logic k8s handle nahi karta hai...jaise 
deployment,service,ingress,,configmap,secretes etc in sabhi ka logic by default 
k8s ke pass hai lkn baki resources ka nahi hai or possible bhi nahi hta...

toh fir in sabi extrnal resources ko add karna hai toh fir k8s kahta hai ki
with the help of user managment...we can extend our capabilities or extend
api server in k8s.so ye sab k8s nahi karega...uske liye k8s ne 
resources ready kia hai....cr,crd,cc........

CRD---- DEFINING NEW TYPE OF API TO K8S...SO U HAVE TO SUBMIT CRD(USING YAML FILE) TO K8S.
MATLAB AGAR ISTIO company ko resources add karna hai k8s mai..to usee custom resources 
defination file ko submit karna padega in k8s.

lets take example of deployment.yml file

hum deplyment.yml file jab likhte hai
usme jo bhi syntex hta hai uske hisab se hum field ko fill krte hai like kind,metadata,spec
etc. lkn humne jo ikha hai iss format mai..yeh validate kaise hta hai ki right hai ya wrong
..toh api server mai already k8s resources defination hta hai deployment ka..jo 
validate krta hai k8s resources (depolyment.yml) file ko.
same in crd cr also 
Custome respurcesa defination only validate to ur custom resources(file whi
which is in yaml format that istio company writes) which is right or wrong

CR---->CRD------------>CC 
1. U HAVE TO DEPLOY THE CRD TO EXTRND THE CAPABILITES OF K8S CLUSTER
2.THEN U HAVE TO DEPLOY THE CC
3.THEN USER WHO WANTS TO USE THISE FEATURES IN K8S CLUSTURE THEN DEPLOY CR  

U CAN write custom controller by GOlang.....

there is HELM chart which taking care of deploymtn of crd cc 

koi bhi custom res add karna hai ya fir deploy karna hai to HELM jaada popular hai

As a devops engg  apko srf docmentation follow karna hai for installing CRD and CC using
HELM chart...ar agar kuch probem ata hai like ISTIO mai to fir usko debugg karna that will 
be ur duty as devops engg.
