## CONTINOUS MONITORING TOOL >>>> NAGIOS 

splunk, promotheus, ELK,Librato, cloudwatch for AWS monitoring tools

Nagios is an open source software for continous monitoring of systems, network, and 
infrastructure. it runs plugins stored on a server which is connected with a host
or another server on your netwrk or the internet. In case of any failure nagios alerts
the issues so that technical team perform recovery process immediately

main buniyadi motto = hamara downtime reduce ho jaye..

ngios uses port number 5666 5667 5668 to maintain its client

## Why nagios 
-- detect all types of network or server issues 
-- hellps u to find the root cause of th problem which allow u to get the permanent solution to the problems
-- reduce downti,e 
-- active monitoring of entire infrastructure
-- allow u to monitor and troubleshoot sserver permormance isues
-- automaticlly fix problems

## fetures of nagios
-- oldest anf latest
-- good log and database system 
-- informative and attractive web interface
-- help u to delt network errors or server crashesh
-- you can monitor the entire business process 
-- monitor netwrk service like https,smtp,snmp,ftp,ssh,pop,LDAP,IPMI,DNS etc.

## phases of continous monitoring
1. define = develope a monitoring strategy
2. establish = how frequently you are goiong to monitor it 
3. Implement 
4. analyze data and report finding
5. Respond 
6. Review and update

## NAGIOS ARCHITECTURE ## 

** ngaios mai hta hia nagios server ar client or nodes jise hume monitor karna hai
** nagios ke andar configuration files hti hai..matlab agar muze server se node
mai jana hai to node k ip adress pata hna chy
** whi sab like ip adress, username,password yeh configuration file mai rahega
** ab hume node pe monitor kya krana hai o dekhna hai
** maltb kitna traffic aa rha hai,kitne respond de ra hai,kitna request le ra h etc
jaise ye https snmp ,ssh pop etc port ko access krta hai matlab dekhta hai ki 
ye log kam sahi se kar rahe ya nahi
** ye sab chize hum configuration file mai dal dete hai jo karawana hai
** iske pas daemon hta hai..yah ek serviceaa hti hai jo nagios ka server ispe hi chalat hai
** nagios ko start krne ke liye daemon hta hai
** daemon sab info collect karta hai config file se ki kaya kya karna hai 
** ab deameon sab kam khud se nahi karta hai..uske pas ek plugin hti hai
** us plugin ko NRPE(NAGIOS REMOTE PLUGIN EXECUTER)
** isko pahle install karna padta hai ar daemon use invoke karta hai
** ab jab nrpe jayga node pe tab node pe bhi koi plugin rahna chy uske liye
** wha check by ssh plugin(nrpe agent) hta hai
** servee ko node ke sath hum ssh ke through jodenge
** ar sari info daemon ko deta hai
** ab daemon ke pas ek local database hta hai jaha o info store karta hai..
us database se o info leke jata hai aplke web page ke upper jo nagios ka webpage hta hai
** use hum nagios ka dashboard kahta hai ar ye apko internet pe dikhega
** ye sab client server architecture haii

## nagios is a client-server architecture usually on a network, a nagios
# sever is running on a host and plugins are running on all the remote host
# which should you monitor

# how does it work?
monitor all details in configuration files
daeman read those detailsinto data to be collected
daemon use NRPE plugins to collect data from nodes and store in its own database
finally show everything in dashboard

