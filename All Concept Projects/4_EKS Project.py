##### WHYYYY EKS ###

if anyone talk to the access the or deploy site on worker node..to hmae sabse pahle controll
plane se bat karni padti hai fr o data transfer karta haiwroker or data plane mai.

if u r using kubedeam ,,then u have to install all pluging i like cni,kubectl,dns,proxy and all.
apko sab create karna pdata hai.

suppose apne 3 master anf 3 waorker node ready kiye hai with the help of KOPS..if one of the master node,,
scheduler not working,etcd crash,master node down,certificate expired,like that..this is not samall issues..
then  as a devops engg u have to solve it..it is tidious.if there is manual acivities there will be aws.

EKS is manage controll plane but not manage data plane.
sab aws handle karta hai controll plane ka...k8s cluster pura ready karta hai.

EKS mai hume sab kuch milta hai matlan controll plane ka jo bhi configuration hta hai ya fir set up hta hai

lkn AWS hume controll plan ko connect karne ke liye 2 option deta hai...
1.To create EC2..matlab  worker node ke liye instances create kar sakte hai ..ya firrrrr
2.Fargate--it is aws serverless compute just like lamda fumnmction. it is for defining running containers

matlab eks controll plane ka dhyan rakhta hai ar fargate data plane ka.

u can built up robust and highly stable cluster with the help of eks and fargate..they both are
highly available and scalaable.

u can use ec2 instances in worker node also but u have to take care of its high avaialabilty.
u have to configure with auto scaling,monitoring and aallll....

if u are using EKS hten u dont have to worry about
Certifiaction expired
api slowness
etcd getting crashedd..
matlab eks mai apko support milta hai.

In AWS u can create k8s cluter by two ways
1.By creating EC2 instances and top of that u have to install k8s with help of KOPS and Kubedm.
2.By EKS (managed service) 

###########################################################################

CONCEPT OF K8S.

----Suppose we create cluster of 3 master nodes and 2 worker node
Ek worker node mai hmari application hai..with pod.yml (matlab pod rakaha hai)
ab is pod ko by default cluster ip hti hai..

cluster ip mai hta ye hai kii...worker node ar master node hi access kar pate hai application ko
---- to fir hum isme service.yml add karte hau

service hume 3 option deti hai/////1. cluster IP mode 2.Node port mode & 3.Load Balancer
Node port mai whai log access kar pate hai jo logo ke pass baki worker or master node ya fir 
insatnce ko access karne ka ip rahta hai..matlab jo logo ko private subnet ka access
rahega whi log nodeport se access kar paynge..humari app private subnet mai hi rahti hai
for people who are outside they want to access it thennn u have oad balancer

----Load balcer elastic ip provide  karta hai..lkn har ek application ke liye ek ek elastic ip se
cost badh jati hai..aws chrged you for that.

---so for that u can use ingress
ingres will allow to customer to access the application inside the worker node
ingress will do route the traffic inside the cluster
devops emgg ingress resources create karega.ingress.yml file
ingree bolega is user ko access krne do..fir o service ke pas jayga and then pod ke passs
u write in ingress resources and u can use kubectl to deploy ingress resources.

--but only ingreess resources se kam nahi chalega
aisa ko hona chy jo bahar se request ko laye ar andar tak pohchyeee.
matalb user jab access karega bahar se to o request sabse phle public subnet mai jaygi
jaha load balncer rahta hai..fir o load balncer requesst ko andar bhejega
there is ingress controller.typically all load blncer support ingress controller.
sabhi ka khud ka ingress controller hta hai like nginx.

i have deploy ingress controller for aws ALB so as soon as the devops eng create ingress resource
then thise ingress controller watch for ingress resources and it create ALB for u.

matlab-------hume ingresss cotroller deploy karna padta hai fir o ingress resources ko dekhta hau
ar usii hisab se apko apkaa load balcer banake deta hai..matlab apne agr infgress resoucres mai
bola ki aws ka ALB ya fir nginx ka load balcer do...to controller o de dega.
same for all ingress controller...sabhi ki ingress resources hti hai jo likhni padti hai.

ye hume load balcer banake dega fr user load balcer se direct hamari application accessa kar payga

now....Practical start

