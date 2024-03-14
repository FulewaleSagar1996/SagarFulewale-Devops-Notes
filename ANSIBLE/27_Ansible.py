# Ad hoc commands, Modules, and playbook

code ko push karne ke upper ke 3 tarike hote hai
1.ad hoc commands = simple linux commands se hta hai
agar koi chiz ke liye hume nahi malum ki module ar playbook kya hai..to ad hoc use karte hai
here it is no idempotency, bar bar file create krta hai.overwrite karte hai
Module ar plybook ye YAML ke form mai ikhe jate hai
module matlab ek single command
and playbook is more than one module..or combination of modules

# Ad hoc commands
**it is commands which can be individually to perform quick function
**these ad hoc commands are not used for configuration managment and deployment
bcz these commands are of one uses
**the ansible ad hoc commands uses the /usr/bin/ansible commands line tool to auatomate
a single task
**koi sari machine ko start shutdown add karna hai to single command use kar sakye hai

#ad hoc commands
**go to ansible server
-a matlab argument..jo bhi "" mai hai use linux command trat karke execute karwa de
** ansible group name -a "ls"
** ansible group name[] -a "touch filez"
** ansible group name -a "ls -al"
** ansible group name -a "sudo yum install httpd -y" or
** ansible group name -ba "yum install httpd -y" = -b matlab become sudo
** ansible group name -ba "yum remove httpd -y"

# ansible Module
it is like source jo predefined commands hoti hai
ansible ships with a number of modules that can be executed direclty on remote hosts
or through playbook
your library of modules can reside on any machine and there are no servers doemons,or
databased required
the default location of inventory files is /etc/ansible/hosts

#ansible module command
-m matlab module..uske age jo bhi hai o module ki tarah treat karo
** ansible group name -b -m yum -a "pkg=httpd state=present" ----> yum ye module hai
** ansible group name -b -m yum -a "pkg=httpd state=latest"
** ansible group name -b -m yum -a "pkg=httpd state=absent"
intall = present, update = latest , unintsall = remove
** ansible group name -b -m service -a"name=httpd state=started"
** ansible group name -b -m user -a "name=raj"
** ansible group name -b -m copy -a "src=file4 dest=/tmp"
