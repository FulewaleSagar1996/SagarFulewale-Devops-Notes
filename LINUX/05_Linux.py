#  useradd sagar <----- to create user in your syatem..
# all authority to root user only not added user
# cat /etc/passwd ----- sabse niche mai user dikhega jo create hua hai..iise user check karte hai

# groupadd techno <----- too create group
# cat/etc/group <---- issse grp check hote hai..gropu ke andar user bhi nzr ata hai

# gpasswd -a /-M <---- kisi user ko agar grp mai add krna ho toh-- gpasswd -a sagar technogrp
# gpasswd -M <----- mulriple user agar add karna hai grp mai to use kar saktwe hai
# 
# ln <---- hardlink=== ye hta hai backup ke liye == parent file mai agar update kiye humne
# to automatically hardlink file mai update ho jayge..copy nahi karna hai
# ln file2 backupfile2 ==== ls se dono file dikhegi

# ln -s  <---- softlink ==== ye shortcut create karta hai..jaise dekstop pe shortcut hte hai
# shortcut agar dlt kar diya to software ko frk nai padta hai = ln -s file1 softfile1
# ls -l se pata kare

# tar <------  bht sari filesa ko single file mai jodna hai ar single file ki tarah dikhe
# gzip <------- wahi data ko compressed karne ke liye gzip
# tar -cvf dirx.tar dirx(cvf= create verbose forcefully)
# isi file ko compressed karne k liye --- gzip dirx tar
# reciver end mai file ko unzip karne k iye --- gunzip dirx tar gz
# -xvf dirx tar --- file ko extract kar skate hai
# wget <------- kisi url or link se download karna chahte hai ho to use hta hai
# wget <URL>

# last video no 7 dekh le 

# nproc free top command are imp 
node helath---top////special command---process kya hta hai apke machine ye pura batata hai
cpu- nproc
memory- free

ye sab commands ke badle hum shell script likhte hai jo automotaed hti hai
