# how to create a directory or folder
# mkdir dir1 enter--make dir
# mkdir -p dir2/dir3/dir4 ---- foldrr ke andar folder
# cd dir2 --- change dir--- dir ke andar aa sakte hai
# cd.. --- double dot parent dir mai jane ke liye hta hai
# cd. --- single dot current dir mai jane k liy
# cd ye bahar ane ke liye kam ata hai dir se.
# pwd --- print working dir-- matlab konse dir mai ho
# cd../../.. ---  se ap direct bahar aa sakte ho dir se

# How to create hidden file
# touch/cat/nano .file1------ name ke age dot lagane se 
# ar agar hidden file ko dekhna hai to --- ls -a--- list all 

# How to copy file
# cp source then destination
# cp file1 file2 ---- file1 se copy hoke file2 mai copy ho jayga

# ----- COMMANDS FOR TODAY -----
# Hostname - choti details check kar sakte hai..kispe kam kar rahe hai karke
# ifconfig - ye apko batatat hai ki apkpi machine ka ip address kya hai..in window it is ipconfig
# hostname -i = isse srf ip adress milga..upper command mai puri details aa jaygi
# cat/etc/os-release ---- ye apko os ka version pata chalta hai

# yum install httpd ----- yum ye pckage hai jo by defaut linux mai install 
# hota hai..yum means yellowdog updator modify..ye use hta hai kisi bhbi
# softwaren ko install,update,download ya remove karna hai to use hta hai
# httpd ye appache ki file ko by default install karta hai
# yum install httpd -y ------ y means yes..jo bhi notifctn ayga usko yes karna
# 
# yum remove httpd -- file ko dlt karna rhta hai tab 
# yum update httpd --- files ko update karna chahte ho toh update krna pdta hai                    
# service httpd start ---- package ko install karne ke bad usko start karne ke 
# liye use hta hai // service ko start karne k liye

# service httpd status --- jo service hai o active hai ya nahi o dekhne k liye
# chkconfig httpd on ---- package apne aap servive chalu ho jaygi machine on 
# karne ke bad..agr hum shut down ke bad open karte hai to

# chkconfig httpd off --- package ki service agr band karni hai toh
# which ----package hai ya nahi system mai o check krne k liye..kisi ek package ko hi
# whoami ---- mai kon hu,,,mtlb mai konsa user hu..root ya ar koi

# echo ----- khud ka hi msg pass karne ke liye use hta hai
# msg ko reflect karne ke liye use hta hai.
# echo se bhi hum file create kar sakte hai like echo "welcome" > filez
# echo  > filez ---- files dlt bhi hti hai

# yum list installed --- pure package install hue ya nahi  check kkarne k liye
# jitne bhi package hai uski list deta hai install hai ya nahi

# grep ----- ye find command ki tarh use hta hai like window
# grep root/etc/passwd
# sort =----- alphabetically arrange hti hai files
# head ---- suru ki 10 line nzar ati hai
# tail ----- last ki 10 line nzr ati hai
