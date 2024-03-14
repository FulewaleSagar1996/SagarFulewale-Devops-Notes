##### DEPLOY YOUR FIRST APP ##

Sabse phle hum q docker se k8 mai shift hue for deployment 
---- k8 hume 4 main chize provide  karta hai jo docker ke pas nahi hti.
1.clusture(doccker has only one host)
2.aatohealing
3.autoscaling
4.enetrprise level behaviour

always compare to docker 

why we usee pod..
pod is actually to define running a conatiner
jaise hum docker mai image banate the ..fir usko image ko build karte the ar 
container mai chalate the with the helpof commands..
pod yah bolta hai ki sab chize ek isme dalo like pod.yml jaha bunch rahegapura
pod is like a ec=xact docker container but only in yaml.file 

****we are going to deploy our first application as a pod 
kubectl for commandline for k8 like in docker there is docker commands
kubectl ineract with direclty pods

isme hum kubectl install karnge
uske bad hum pod or cluture minikube mai karnge..bcz we dont have money
//many option are there like minikube,k3s,kind, mico8s etc.
then how to deploy on pod

demo***********
installation search from google direclty no need to remenber
for theese u ca refer rajput videossssssss

in production generally there is 3 master nodes and many worker nodes

in minikube only single node bcz for practise

kubctl gets pods
kubectl create -f pod.yml

importsant coomadns to see logs of pods
kubectl describe pods
kubectl logs nginx


how to add autoscaling and healing concept 
---by deployment 
all are same only kind is change..pod to deploy 


