# This concept from abhishekh and rajput i.e mixing together

#### k8's Production System 

minikube,k3's, k3d etc all are development env jo hum production mai use 
nahi karte hai.should not be use on production
agar hum devps engg hai so company expected from u that u will create a infra
of k8 or managae the life cycle
People use another platform in their organisation for production
soooooooo how org manages k8 clusture in production ????//

k8 distribution kya hai???
koi bhi open soarce platform ko log unke use ke hisab se update karaate hai 
ar use karte hai...like linux ke liye amzon lin,refhat and centos yah distribution hai
sAME K8  bhi open source hai..jiske distribution hai..like eks from amazon,openshift from redhat.
tanserfow,ranchet etc. jispe hum deploy karte hai production mai ya fir life cycle manage karte hai pura
aur yah isly jarurui hai q ki yah dist support krta hai hame agr koi problem hui toh..
wase to k8 bhi support karta hai lkn uski kuch time line hti hai..agar apke org mai time ka issue
nahi hai to k8 direct use kar sakte hai...dist ki jrurt nahi hai.
u should tell to ur interviewr from above distruibution ki isme se ek par hum prodctoion mai usee karte
hai agr minikube bata diya toh  reject ho jaoge

where we handles our cluture in production
k8's itslef
openshift
Rantier
Tanzu
eks
gks
aks

Kubernates hum production mai use kar sakte hai awith the help of KOPS(k8 operation)
kuberanetes and eks mai yhi frk hai ki jab hum ec2 instance ke upper k8 chalate hai toh hume koi
support nahi deta hai amazon agar kuch misconfigure ho gya toh wheres as eks support us bcz we paid to them

#### HOW THE DEVOPS ENGG MANAGES 100'S OF CLUTURE IN PRODUCTION *****
KOPS AND KUBEADM are the tools..kubedm iis old now
devops engg ko srf install hi nahi karna padta hai k8's uske sath lifecycle bhi
manage karna padata hai 
-- lifecycle matlab---upgrades,modification,deletionof pods like that

Jaise hum cluture manage karne ke liye k8 , ooenshift,eks use karte hai..toh ise 
install krne ke alag tarike hai..jaise openshift ko install karna ho toh ansible playbook hti
hai usi ke site pe jaha se um install kar sakte hai..wse hi k8 pe hume chaklana hhai toh
hume with the help of KOPS sab kuch install karna paega

just understand the installation process bcz it is chargable

installation github repo se dekhna
abhishek veeramalla kubernetes zero to hero---all step there

only note that agar intervier puchega konsa domain use karte hai and all..
toh jo project ka domain hta hai org mai o domain use karte hai ar usko route
53 se direct connect connect karte hai with the commands.
hum k8.local domain bhi use kar sakte hai lkn yah srf tabhi use kaarte hai jab hum
staging aare mai ya developer env mai testing kar rhau hte hai.toh ye ap bata 
sakte hai.
