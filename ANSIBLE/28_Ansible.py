# Playbook
playbook in ansible are written in YAML format
it is human readable data serializationn langauge.it is commonly used
for conf files
pb ls like a file where u write codes consist of vars,task,handlers
files,templates and roles
Each playbook os composed of one or more modules in a list module is
a collection of conf files

playbook are devided into many sectors like 

target section= defines thr host against which playbook task has 
to be executed

variable section = defines variables
task section = list of all modules that need to be run in a order

*For ansible, nearly evry YAML files starts with a list
*each item in the list is a list of key-value pair commonly called dictionary
*all yaml filees havr to begin with "---" and end with "..."
*all members of a list lines must begin with  the same indentation
level starting with  "-"
for eg.-
---# a lsit of fruits
   friuits:
   -mango
   -apple    
...

*a dictonary is represented in a single key value pair
for eg.
---#detail of customer
  customer:
      name: rajput
      job: trainer
      
extenaion of playbook is .yml

# steps

** go to ansible server
** now create one playbook vi target.yml
--- # target playbook
-hosts: group name
-user: ansible
-becomes: yes
-connection: ssh
-gather_facts: yes
esc-:wq
Now, to execute this playbook 
ansible-playbook target.yml(playbookname)

#task
task:
    -name: install httpd on linux
     action: yum name: httpd state: installed
    
# variable
*anible uses varibale which are defined previously to eanable more
flexibility in playbook and roles.they can be used to loop through a set
of given values, access various info like the host name of the system and
replace certain strings in a templates with specific values
* varibale hume task ke pahle rakhna hai.;defined karke

No go to ansible server with asible user
* vi vars.yml
* --- # variable playbook
-hosts: group name
-user: ansible
-becomes: yes
-connection: ssh
vars:
    pkgname: httpd
task:
    -name: install httpd on linux
     action: yum name: httpd state: installed
     
now exceute playbook ansible-playbook vars.yml


#Handlers section (dependency)
maatalab pahla wala kam nahi hga tab tak uske depend mai jo hta hai o nahi krnge'
* a handler is exaclty to same as task but it awill run when called by another task
OR * Handler are just like regular task in an ansible playbook , but are only
run if the task contains a notify direction ans also indicate that it changed something

go to ansible server with asible user

 vi handlers.yml
* --- # handlers playbook
-hosts: group name
-user: dansible
-becomes: yes
-connection: ssh
vars:
    pkgname: httpd
task:
    -name: install httpd on linux
     action: yum name: httpd state: installed
     notify: restart HTTPD
handlers:
    -name: restart HTTPD(same as notify)
    action: service name=httpd state=restarted
     
now exceute playbook ansible-playbook handlers.yml

# dry Run
check whether the playbook is formatted correclty
** ansible-playbook handlers.yml(playbokname) --check

# Loops
Sometimes you want to repeat a task multiple time.in computer programming,this is called
loops. common ansible loops include changing ownership on several files and or 
directories with the file module, creating multiple users with the user module,
and repeating a polling step untilled certain result reached.
matlab jab tak o kam hum sari machine pe nahi karte tab tak o loop ko 
hum stop nahi karnge.

vi loop.yml
* --- # loop playbook
-hosts: group name
-user: dansible
-becomes: yes
-connection: ssh
task:
    -name: add a list of users
     user: name='{{item}}' state=present
     with items
     -sagar
     -ratna
     -tukku
     -pari
and execute 
to varify go inside node: cat /etc/passwd