# *****k8s RBAC *******************(Roll based access controller)

it is actaully on security  issuesa
(here service acc , role and role binding concepts)

//// k8 RBAC broadly devides into two parts
1. USers managent

----organisation mai sabhi hte hai developer ar QA team..to koi bhi ake hmare k8s cluster pe
kuch bhi kar sakta hai like delete pod,delte etcd etc. so we have to create RBAC..matlab roll create 
karnge ki kon kya kya kar payga nd allll
---depending upon role give aacess 

2. Service account
it is actully similar to user maangment but u can also manage the aceess to the services or 
application that r running on cluster using RBAc

--matlab jaise pod resources chal raha hai..ar whi accidentally config file , secrets, api services
ko dlt kar raha hai....that is not gud...to fir jo resources hum chala rahe hai unhe bhi hum
kuch role dete hai ya fir RBAC lagate hai takii aisa naa ho..matlab service acc ko RBAC krte hai

(matalb manages the the access of services which is running on cluster)

threeeeeeee majorrrrrrr things in big pictures in RBAC (broad level)
1. services account or usersss
2.roles or cluster roles
3.role binding or cluster binding 

-------now th thing is k8s does not provided the creation of user or user managment...
matlab jaise hum kahi pe bhi platform mai usercreate karte hai wse k8s mai user create nahi kr sakte
(service acc create kar sakte hai k8 mai but not user)

----to k8s actually off loadd the user managment krta haiiii-----matlab for example kjab hum koi site
open krte hai tab hume direclty login to insta or google aa jata hai without creating idddd....

in k8s, there is api server we can give flags...
in EKS,there is IAM for create user...means external iddentity provider

Identity provider..LDAP,OKTA,SSO

IDENTITY BROKER..KEYCLOCKK...POPULAR IT IS
KEYCLOCK IDENTITY MANAGEMENT KARTA HAI

by default k8s mai service account create rhta hai ,,,ya fir hum bhi kar sakte hai...

k8s support two services....
role - how and what to grand access to user.(kya kya role dena hai..yaml file rhati hai jaha likhna
padta hai ki..configmap,secret, ko access karega and all..)
role binding----attaching or assigning ke liye rol binding use krte hau
matla ek trf user hai ar uske roles hai ar in dono ko attached karna hai to role binding use hta hai






