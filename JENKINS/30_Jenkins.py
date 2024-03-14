# Contionous integration and continous delivery ot deployment
CI/CD is a methodology not tool
metodology yah SDLC ki hai
Before cont integrtion developer pura code hone ke bad hi integrate karte the.ar jab testing jab krte hai
agr kuch error hai to ab use find out karne mai bht taklif hti hai..not possible isly CI aya

After Cont integration, developer chote chote parts mai github pe push krta hai..fr o ci server pe jata 
hai ya fir pull kia jata hai automatically.wha build test ar deplloy hta hai in ci server.internally
deploy karta hai phle yaha pe not on client site
ci server notifiaction dega error or success ka developer ko.to fir developer jaldi check krke ar push krga
isme error ko minimie hta hai,time kam lag raha hai,automation hta hai pura.
continous integration is equl to cont build + cont testing

##### Process ####
plan--->code--->build--->build--->test--->deploy--->operate---->monitor
sabse hum plan karke code likhnge
fir usko build karnge with maven and gradil
fir testng with selenium,junit etc
deploy and operate krne ke liye chef or puppet,ansible
monitor krne ke liye nagios use krte hai

ab ye sara kam automated hta hai eith the help of JENKINs
hume srf code uthake github mai daln hai fir jenkins uthake maven ke pass bhejega build ke liye,fir testing
ke liye selenium and then chef and nagios.ye sab jenkins kart hai.isme sab automated hta hai
agar ap manual bhi karna chahte hai to  kar sakte hai.
jenkins is heart of devops

JENKINS:
** jenkins is an open source project written in java that runs on windows,macos and
other operating system. it is free community supported and might be ur first choice tool for ci

** jenkins automate the entire software deelopemt life cycle
** jenkins was originally deveoped by sir microsystem in 2004 under the name hudson
 
** thr project was later named as jenkins when oracle bught microsystem

** it can run on any major platform wothout any compalibiltity issues
** whenever developer write code, we integrate all that code of all developers at that point of time
and we build,test and deploy to the client this process called as CI/CD
** jenkins helps us to achieve this 
** because of ci bugs wil be reportes fast and get rectified faast

### Workflow of Jenkins

** We can attach git ,maven,selenium,and artifactory plugins  to jenkins
** plugins= matlab port smjo.ki jenkins ko github ke sath communicate karna hai to phle plugin install kro
** Once developers puts code in github , jenkins pull that code and send to maven for build
** once build is done jenkins pull that code and send to selenium for testing
** Once testing is done , then jenkims will pull that code amd send to artifactory
(for archiving purpose) as per requirment and so on
** we can also deploy with jenkins

## Advantages
** lots of plugins
** u can wriye ur own plugins
** u can use community plug in 
** it is not just tool , it is framework means u can do whatever u want 
** we can attach , slaves(nodes) to jenkins master. it instruct other slaves
** to do job.if slaves not available ,jenkins itslef does that job
** it also behave as a crone server replacement that is can do schedule task(peridically kam check karna)
** it can create lables


















