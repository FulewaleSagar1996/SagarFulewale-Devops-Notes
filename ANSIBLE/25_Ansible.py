### ANSIBLE INTRODUCTION #####

'''1.Ansible is configuration managment tool like a Chef only the diff 
is thet ansible is push based process and chef is pull based

2.ansible is very easy tool and not complicated like chef.in chef 
ruby languged we used and in ansible YAML lang(yet another markup langauge)

3.push based mai server jata hai node ke pas jo update hai o batatta hai
lkn chef mai hume jana padta tha server ke pas kuch update hai ya nahi krke

4.jise chef mai recipe hti hai wse hi ansible mai playbook hti hai jaha hum
apna code ikht hai..ansible bhi infrastructure as a code pe work karta hai IAC.

5.ansible mai agent nahi hta jaise chef mai chef client hta hai
6.michall dehaan ne banaya tha 2012 mai..ye abi itna popular nahi hai lkn hga
7.yaha hum direclty node ko server ke sath  connected rahta hai,koi workstation nahi hta
8.server node ke sath direct bat karega with the help of SSH which is very easy

### ADVATAGES ####
1.ansible is free to use by evryone
2.it is very consistent and light weight
3.no constraint ragarding the os or dunderlying hardware are presend
4.it is very secure due to agentless capabilities and open ssh security features
5.ansible does not need any special system administrator skills and used it yaml
6.push based

### DIADVANTAGES ###
1.insufficient use intrface, though ansible tower is GUI , BUT STILL IN DEVELOPMENT STAGE
2.cannot acheive full automation by ansible
3.new to the market therfore limited support adn documnet is available

# ansible server
the machine where the ansible is installed and from which all task and playbook will be run

# module
basicalyy module is a command or set of command meant to be executed on a client side

# task
it consit of a single procedure to be complited

# role
a way of oganising task and related files to be later called in a playbook

# Fact
information fetched from the cleint system from the global varibles with the 
gather faced operation

#inventory
files containing data about the ansible client server

# play
execution of playbook

# playbook
it consist of code on yaml format which descibe task to be executed

# Notifier
section attributed to a task which calls to handler if the output is changed

# handler
task which is called only if a notifier is present

# host
nodes, which are automated by ansible
'''