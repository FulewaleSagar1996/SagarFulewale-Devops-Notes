
## Conditon , vaults and  Roles
'''
condition=
When we have diffnret diffnrent scenario , we put condition accordinlgly to scenario

when statement=someties u want to skip the coomand on perticular node
 vi condition.yml
* --- # condition playbook
-hosts: group name
-user: dansible
-becomes: yes
-connection: ssh
task:
    -name: install apache on debian
     command: apt-get -y install apache2
     when: ansible_os_family== "Debian"
    -name: install apache on redhut
     command: yum -y install httpd
     when: ansible_os_family== "RedHat"
     
     action: yum name: httpd state: installed
     notify: restart HTTPD
     

## Vault
*Apne agar koi playbook likhi hai ar koi banda ake apka kam dekhna chahta ho lkn
koi dekh na paye to fr usko encrypt kar sakte hai wih password
*agar koi nayi fileko encrypt karna chahte hai ar pahle se jo file thi use encrypt karna
hai to dono tarike mai kar sakte hai
*ansible allows keeping sensitive data such as passwords or keys in encrypted files,
rather than a plaintext in your playbooks
** creating new encypted playbook
ansible-vault create vault.yml(playbookname)


** edit the encypted playbook
ansible-vault edit vault.yml(playbookname)


**to change the password
ansible-vault rekey vault.yml(playbookname)

**to encrypt an existing playbook
ansible-vault encrypt target.yml(playbookname)


** To decrypt an encrypted playbook
ansible-vault decrypt  target.yml(playbookname)


## Roles
playbook ke andar hamari multiple chize hoti hai like task,hanlders,conditions,vars etc and aagar 
bht badi playbook hai it hume find out karna mushkil hta hai to hum inke kam define karte hai 

playbook create karo,uske andar ek file create karo master.yml and ek directory ka nam myroles rakhe.
role ki direcory ke andar ar diff diff directory created karnge.fir us direcory mai file create karnge
like main.yml, handlers wali direcory mi main.yml ar variable ke directory ke andar main.yml 

ab playbook run kon karayga...?
master.yml lekin iske andar do files rahnge target and roles ke andar myrole rahega.my role 
mai pure chize jo hai o execute hge.

** We can use two technique for reusing a set of task: include and roles

roles are good for oragansizing task and encapsulating data needed to accomplish those task
ansible roles are:
default, files, meta , vars, template, task

We can organise playbook into a directory structure called roles
adding more and more functinality to the playbook will makeit difficult to mainitain in a single file.

Default: it stores the data about role/application default variables 

files - it contain files need to be transformed to the remote VM (static file)

Handlers - they are triggers or task ,we can segregate all the handlers required in playbook

Meta - this directory certain  contains files that establish role dependencies

task - it contains all the task that is normall y in a playbook.

variables- varibles for the roles can be specified in this directory and used in your config 
files . both vars and default stores varibales


# Steps
* mkdir -p playbook/roles/webserver/task or playbook/roles/webserver/handlers or playbook/roles/webserver/vars
*tree
*cd playbook/ = jo bhi kaarnge playbook ake ad=ndar hi karnge
*tree
*touch roles/webserver/task/main.yml = task ke andar ek file create kar di
*touch master.yml
*$ vi roles/webserver/task/main.yml

 -name: install apache
 yum pkg=httpd state=latest
 esc=wq
 
 vi master.yml
 -host: all
  user: ansible
  become: yes
  connection: ssh
  roles:
      -webserver
      
ansible-playbook master.yml = for execute

'''