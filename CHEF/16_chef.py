**** What is Bootstraping *****

ye lecture 3-4 bar dekhna hai'

yad rakhna ki jo bhi hum kam karenge o workstatiom mai hi karnge 
chef server mai hume kam nahi karna padta.usko direct access nahi karenge
 
aj hume apna WS(wrkstation) connect karna hai chef server ke sath.
uske bad chef server ko node ke sath connect karna hai with the bootstrap process.
jo bhi recipe banaynge o chef server mai dalne ke bad automaaticlly node mai
update hgi.. ye kam hai

chef server is a mediator for WS and node
chef server pe ek account banye
then connect youe WS to chef server
now whatever your cookbooks uplod WS to server
node ko connect karnge chef server ke saath with bootstrap
apply cookbook from server to node


*** Chef server ko Connect karne ka tarika WS se ******

login linux
ls
cd cookbooks
ls
apche-cookbook and test-cookbook
open google,manage.chef.io--- create account
then create organization koi bh nam ka..bht sari org bana sakte hai
starter kit --- downoload starter kit..unzip...chef-repo
starter kit hi connect karta hai server ko WS se..jisme chef repo ki default file hti hai
lkn ye chef-repo file muze meri lappy mai ni chy ise server pe bhejni hai linux mai
to fir connection establishe ho jayga
lkn window mai jo file hai usse ap linux mai dirclty nahi bhej asakte hai
uske liye  Winscp download karna padega.ar o file drag and drop karni paddegi

ls
cd .. 
ls
cd chef-repo === pura kam isme hi karna hai tabhi hum connect rah paynge
ls -a 
cd .chef/
ls
config.rb and apki orgnization ki file milegi
config by default rahegi jisme server ka url ar uske conf rahnge
cd ..
chef-repo = knife ssl check ----> isse patta chalge ki hmara server connect hai ya nahi

**** Now hum chef server ko node se connect karnge with bootstrap ******

attaching a node to a chef server is called bootstrap.note that both WS and node
should be in saame availability zone AZ
now onward ap chef-repo mai hi kam karnge
jab hum server to node connect krte hai bootstrap se to automoatically
node mai chef client and ohaii jaisi ppackage install ho jate hai

Process**
Phle hum node baanaynge
create one linux machine..ab hum yaha se chef node chalynge..phle chef workstation chala rahe the
advance detail mai 
#!/bin/bash
sudo su
yum updadte -y

now go to chef- workstation
chef repo mai jaiye

knife bootstrap <private ip of node> --ssh--user ec2-user --sudo -i node-key.pem -N nodename
node-key ye hume create new key pair se download karn hai phle hi
lkn ye to hmare system mai..not in linux toh foir hum Win se drag drop krnge
isko chef-repo ke andar dalna hai linux mai

knife node list = to see bootstrap node

**** delete cookbook ****
hamari cookbook do jagah hai ek WS mai ar ek by default chef repo mai
chef repo wali cookbook kabhi dlt nahi karna hai , Ws wali karne haoi
phle uthake chef repo ke cookbook mai dlange fr dlt krnge 

chef-repo = ls
cd ..
ls
mv cookbook/test-cookbook chef-repo/cookbooks
mv cookbook/apache-cookbook chef-repo/cookbooks

rm -rf cookbooks/
cd chef-repo 
ls
ls cookbooks/
