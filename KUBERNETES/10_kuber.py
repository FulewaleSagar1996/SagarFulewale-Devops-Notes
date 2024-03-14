////// CONFIGMAP & SECREETSSS*************
simple examle of any application ------------

condider u build app and in that backend mai  DB is their and that db there are lots of
infor like db port,user,password etc and this information is not 
hardcoded bcz agar details change ho gyi to user ko bad experience ayga.
ar database ke data ko hum kaha se retrive karte hai----from env variable or any file system 
 
 matlab ye jo db port , pass env variable ya fir file mai store rhta hai
 same in kubernetes there is config map
 
 as a devops emngg u can create config map as a env variable in k8s
 -------------------------------volume mount-----------------------
 
 ////////CONFIG MAP IS ONLY STORE THE INFORMATION THAT CAN BE USED LATER POINT OF TIME///////////
 
 SECRETTTTTTTTTTTTTS (isme RBAC usee karte hai hum)
 ----Same as config map but store only sensitive data.
 if u put data in seccret as a object k8s encrypt it.
 if hacker access etcd he dont have decrypted key..he can read but not use.
 
 user--->config map(yamfile)--->kubectlapply--->configmap created n k8s cluster---->api server saveing info in ----->etcd as well
 so hacker can go to config map as well as  etcd and retrive data 
 ///In etcd k8s have encyption option(secret) so that it will safe data but wt about configmap>????
 so for that we create RBAC or least privalage providing access to Config map so our data will be safe
 
 Configmap baht kam logo ko access hota hai so hacker cannot go to configmap
 
 ///////////////////////////////////////////////
 #*****************Kubernetes Monitoring ****************#
 
 use repo of abhisheck for installaationnnn
 
 why we need??????????///
 
**no of kubernetes cluture rahta hai tab ye monitor ke kam mai ata hai..it is open source
**Garfana visualisation ke liye use karte hai

Architecture---
Prom ke pas http server hta hai wse hi k8s mai Api server hta hai jo lots of matrix expose karta hai jisme info hti
hai ki kon konse resources k8s use kar rha hai...agar hum (api server-matrix) krke dekhe to sab info pata lagegi.

ab promothious ye sab info fetch krta hai ar time series data base mai store krta hai..ye sab promth disk 
mai store krta hai hdd /ssd mai..

then promothius ke sath hum diff diff alert manager connect kar sakte ha =i jo notification bhejta hai
on Email,slack,google meet etc....

----if u create alert manager then promothious push the alert to alert manager and alertmanager configure to 
etc,email,slack
this is default configuration

but u can aalso go to promths UI and u can execute some promptql queries.
with the help of GRFANA, API clients by dashboard

WHY GRAFANA.......????//

agar hum kuch promthois ko query karte hai ar promthious hime uska info deta hai with
other format like JSON ..so it is diffcult to read anyone..s it is easy to read a=or visulise by 
charts and graph with use of grafana


DEMOOOO////////////////// USE VIDEOS





