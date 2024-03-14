#######
 # 3 TIER  artc.

Every application has 3 layer
presentation , logic and data layer//frontend backend nd data base

user kahi pe click karta hai ar data fetch hta hai us data ko apke pas lane ka kam 
backend karta hai jo bich mai hta hai...jo hume dikhta hai o frontend ar jaha data store rhta hai o databse layer
Most of the app is 3 tier application

## Highh level design of Robot Project applicable to all

---user jab jata h tab doo option hte hai ...regidter and login 
--after use switch to catalogue page
we have two catalagoue 
--artificial int and robot product
if user select one robot...then user shows a rating page
--rating and sselect then 
---add in cart---
---then payment
--shipping details
----order completed and get order id..

---there is multiple microservices like
USER, CATALOGUE, RATING, CART, PAYMENT , SHIPPING , ORDER ID
IT SHOULD BE written by developer..fr isko ek hi binary mai likhna hai ya multiple binary mai 
ye developer ka decision hta hai...single binary matalba monolithic. 
but in microservice arcitecture all app should be in single binary or code with diff diff langauges
as per the uses and developer convinience
--each of the component has their own API, and indepedletly deploy.
apko sabhi application ke liye seperate pipeline banani padegi ar dploy karana padta hai.

is project mai sabhi application ke liye ek hi repository use kua hai in github 
but in real scenario, sabhi application ki khud ki diffrent repo hoti hai 

har langauge ke liye alag alag dockerfile hti hai.

##### DATABASESSSS

///UI--AB Is project mai ....frontend or presentation layer mai Angular use kia hai (in UI)
/// LOGIC--then diffrent microservices hai with diffrent langauges 
/// DB--- for catalogue,user data,shipping u need database for storage, then u have cart, cart mai apki 
info save rahne chy jo bhi ap order dalte hai cart mai to uske liye in memory data store hona to hum REDIS use krte hai
and we created as stateful data 

for user mongodb used
for catalogue we used mysql db. 

there are 6 microservices 2 database and 1 in memory data store.

 
