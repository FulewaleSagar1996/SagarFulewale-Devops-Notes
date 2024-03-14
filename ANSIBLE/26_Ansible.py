# hum is lecture mai apne ansible server ko node ke sath kaise connect karnge ye hai

'''
**Go to aws account create 3 EC2 instances in some AZ
take access of all machine through putty and now go to inside ansible server
and download ansible package

** wget <ansible link copy from video>

** ls= isme o package ka nam ayga

** yum install <package ka name paste karna hai> = yha epel rhta hai extra package of enterprises linux)
lelin ye package hta hai epel, is package mai download to kia h lkn isme jo chote chote
software hte hai o bhi hume chy,,like shahi panner mai paneer ke alawa bht imp hta hai baki)

** yum update -y
now we have to update all packages one by one

** yum install git python level-python python-pip ansible openssl -y

ab humne server pe sab kuch to update kar liye hai,insatall kr liye hai matlba apka 
ansinle server ab perfet ban gya hai lkn..server ko kaise pata cahalega ki mere se konsi 
node connect hui hai jo waha pe bhi update kar paye

ab ansible server ke andar host nam ki file hti hai by default to us file mai 
hume jitne bhi node hai uski private ip dalni padegi matlab server ko pata chalega
ki kon kon si node mere sath connect huh hai.host file ko inventory file bhi kahte hai

** Now go to host file inside ansible service and paste private ip of node1 and node2
vi /etc/ansible/host
is host mai jake ek demo group create kare ar dono node ke ip adress paste kar de

lekin ye jo host file hti hai o khud activate nahi ho pati hai..hmare server mau ar ek 
file hti hai jise hum config bolte hai.us configuration file mai already commands hote hai
jo commented hte hai.

** Now this host file only working after updating ansible.cfg.file 
vi /etc/ansible/ansible.cfg
uncommented karne hai do comment ko below
inventory = /etc/ansible/hosts
sudo-user = root 

isses mera server samjh paygea ki host ke andar kitni ip add hai ar konsi node connected hai

abhi tak connection established nahi hai..kuch push nahi kar sakte hai
example like phie no to hai lkn call nahi lagaya hai

// real world mai root user passaword kabhi nahi dete ye yad rakhna..uske alaaawa
hum ek ar user create kar dete hai..use sabhi rights de dete hai..ar uska id pass 
hum employee ke sath share karte hai
hum ansible mai alwys ek ansible user kam karte hai not like root user

** adduser ansible
Now set password for this user
** passwd ansible<username>

Now switch as ansible user
** su - ansible = abhi tak root user the ab ansible user mai convert ho gye..important hai

ab humne isko ansible user to kar diya lkn hta ye hai ki o pure kam nahi kar sakta
jaise hum root user mai rahke kar sakte hai. koi bhi yum install se 
kuch install kare o nahi hga yaha..isly hume use sare rights dene ke liye 
niche ka kam karna padega

** visudo
now go inside this file,
root ALL = (ALL)   ALL
(ansible ALL = (ALL)  NOPASSWD: ALL) --> ye likhna hai matlb ansible ko saab rights de do
:wq

** ye sabhi kam apko node 1 ar node 2 mai bhi karna hai,,,matla unko bhi
ansible ki rigts mil jaynge
iske bad hum jo bhi package install karnge o sab ho jaynge lkn age sudo lagna hai

** sudo yum install httpd -y = q ki humne sudo privileged di hai,ap root user nahi ho
example like company mai eployee ar malik dono aa sakte hai,lkn malik ka icard nahi 
puchega koi lkn employee ka jarur puchega.rootuser = malik ansible sudo user = employee

abhi tak humen connection established nahi kia hai node ar server ke bich
ho ki ssh ke through hone wal hai

Now,establish connection between node and server.Go to ansible server
** ssh <privateip of node1>= connection between node1 and server
lkn connection denied bolega woh(permission denied), q ki humne o buniyadi kam nahi kia jisse hamara ansible
node se connect kar sake. hume kuch changes karne padenge

** Now, we have to do some changes in sshd-config file. go to ansible server
** root@ip = vi /etc/ssh/sshf-config

Do some changes and saved the file.. and do this changes in node1 and node2.
now varify in ansible server

** su - ansible
** ssh <privateip of node1 or node2>
now,it ask for password , enter the pass after that you will be inside node1
 ab jo file hum server mai banaynge o direlty node pe bhi banegi..bcz hum
 ssh se server se direct node pe kam karte hai
 
 # password permission remove ##
 
 hum actually ye karnge ki.ansible server mai do key generate karnge ek public ar 
 ek private,ar jo public key hgi o node pe bhi paste kar denge..matlab dono ko
 ek dusre ko pahchan paye...like u saved phone number in mobile
 ise trust relationship bhi kahte hai..jo root root pe kar saakta hai ar user 
 user pe trust kar sakta hai
 matlab in short ap jab ye process karnge apko teno jagah ansbile user hi rahna hai
 ..aisa nahi ki ek jagah root ar ek jagh ansible to nahi ho payga authontication
 (su - ansible karna padega tino ko)
 Now go to ansible server and create keys,run this command as ansible user
 ** [asnible@ip] = ssh-keygen
 ** ls -a = to see hidden files
 o/p = .ssh
 ** cd .ssh
 ** ls
 do key nazr aygi pubilc and private
 Now i nedd to copy public key in both nodes
 
 ** ssh-copy-id ansible<username>@ <private ip node1> = isse o public key copy kar lega
 ** ssh-copy-id ansible<username>@ <private ip node2>
 
 ask for passward and add last time pass here,iske bad nahi puchega
 
 now, varify goto ansible server
 ** cd ..
 ** ssh <private ip of node1or2> = ab direclty enter hga ar pass nahi puchega
 
'''