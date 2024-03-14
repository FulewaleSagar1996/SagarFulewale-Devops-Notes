# 
# sudo su ==== superuser do switch user..maab ec2 se o root user mai convert hta hai
# 
# How to Create a File
# By Cat touch Vi/vim  and nano
# Cat se hum file banate hai..lkn edit ni kar skate
# Touch mai empty file rhti hai  and vi vim and nano se file edit karte hai
# linux mai sari command small letter mai rkahna ye case sensitive hti hai

# cat command purpose
# cat -file create karta hai
# file ko concatenate kart hai matlab sari files ko ek sath jodke ek file mai rakhta gai
# concatenate- isi word se cat word aya hai
# copy files - copy karna ek file content ko dusre file mai
# tac- ye cat ka ulta hta hai ar ulta kam krta hai

# cat > file1 ---- file create hgi
# cntrl+d se ap command se bahar aoge
# ls(list) se apko pata chalega ki file bani hai ya nahi
# cat file1 --- se content dekhne milega ki file mai k hai
# cat >> fie1--- agar file mai age kuch ar content jodna hai/ya line add karni hai to
# cat file1 file2 > all---- isse nayi file crete hgi all karke..file1 file2 ke content aa jaynge

# Touch command
# can create empty file, multiple empty file, change all timestamps of all file,
# time stamp has three mode
# access time, modify time, metadata or change time
# command == touch file1 and enter, touch file1, stat file1, touch -a file3, touch -m file4

# Vi Editor
# file create ar edit bhi kar skate hai
# Vi is more powerful than nano..
# it is test editor and edit plane text

# vi file1..enter press and then press i (insert) and then likho..press esc..insert se bahar aoge
# :wq likho (w file ko save kro ar q screen se bahar aa jaoge)
# ls se file 1 nazar aygi
# cat file1 karo...jo hai o nazar ayga
# isme navigate karne k liye H J K L use karte hai

# :w--save, :wq---to save and quit, :q----quit

# Nano Command
# nano file2..bahar ane k lie ready cntrl+x, save krne k liye shify+Y..then enter and bahar aa jaoge
# ls se file nazar aygi
# cat file2 and enter

# ls -l ----- file  nazar aygi puri with  long list or detail
# ls -a --- hidden file bhi nazar ati hai
# history ---- sari command jo chalayi hai oo nazar ati hai