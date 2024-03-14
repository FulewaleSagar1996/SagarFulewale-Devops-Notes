# what is problesm in production with docker 
lets see
what is the problems commes in production when u used docker (interview que)
----hum jab bhi koi simple application banate hai to usme docker file likhte hai'
usme fir from ubuntu then RUN apt apt pip nd all raht hai
matlab agar hume koi python and java application run karna gai to python ke liye alag se binary
files and runtime hta hai arrrr java ke liye laga hta hai.
matlab u only require python runtime to execute this application and java runtime for java app.

but if u see dockerfile..in that ubuntu files also there and other apt files are there for building 
ur application. build is diffrent and running ur app is diffrent 
e.g - for java application ..for build u nneed pom.xml jar war file dependency require but
for running application u need only JRE java runtime and java binaries.

then y u need base image ubuntu to make ur dockerfile high loaded

thats y docker comes up with multistage build

---u can split ur dockerfile into two or multiple partsssss
#################
in first part 
from ubuntu
RUN all dependencies
###################
FROM PYTHON/OR ANY IMAGE/OR DISTROLUS IMAGE
copy /////
ENTRYPOINT
CMD [] ---- FOR EXECUTION/////runtime


##############
concept yah hai ki agar hum without multistage jate hai toh ek hi puri dockerfile
mai dependecies and binaries, runtime like openjdk nd all rahta hai 
to isse o dockerfile heavy ho jati hai like 1-2GB.....
agar is dockerfile ko hum split karte hai in stage...matlab jo bhi dependencies hai
ya fir os image hai like ubuntu nd all..uska ek apla stage rahga and runtime ke liye jo lagta
hai in ENTRYPOINT OR CMD o dusre stage mai rahga.....ar jab dependency puri ho jaygi 
to samj lo ki stage 1 hum dlt kar denge ar srf satge 2 ki dockerfile rahgi jo ki srf 50-200MB rhgi

in stage 2 HUM ISME
FROM Openjdk
copy from build 
ENTRYPOINT OR CMD
AISA likhenge

so in final stage u will get only minimilust image like ditroless image
 
####DISTROLESS IMAGES
it is very minimalist or very light weight docker images that will have onlyyyyyyyyy the runtime env.

one bigggggest advantages from this images is securityyyyy....****************importat for interview

so que is that in interview....WHAT IS PRODUCTION ISSUE IN DOCKER CONTAINER AND HOW U SOLVE IT ???


------PREVeviously we were using ubuntu images or even in final stage we are using ubuntu,python runtime
or any other runtime images....whhich will exposee the some kind of valnaburities for hacker..
people find some kind of issuees with this images so we moved to distroless images..
u can say if u used python then we use only python distroless images which only have python runtime
so it sont have have basic commands like curl find ls so it was provide highest level of security 
so after using ditroless images our appliacation not exposes to any os level valnabirities.

golang app mai to runtime bhinahi hta hai uski ditroless images mai..so no chance for bad security


