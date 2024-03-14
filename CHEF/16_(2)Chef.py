
ab tak humne apnea workstation ko chef server ke sath connect kia fir 
uske bad chef server ko node ke sath connect kia with the help of bootstraping

ab hamare WS mai jo cook book padi hai o server mai upload karna hai tbahi chize
apply hgi node par

upload apche-cookbook into chef server*****

knife cookbook upload cookbook name
knife cookbook list= jo chiz upload hui hai o dikhega

Now we will attach recipe, which we would like to run on node
matlab hum usi recipe ko attach karnhe jo hume kam karna hai,sabhi recipe ko akrnge
to samj nahi ayoga ky update and install hua hhai toh

knife node run_list set nodename "recipe[apache-cookbook::apache-recipe]"
jo recipe apply kanri hai node mai o sab run list mai daloge

knife node show node1= node1 ke ssath k konsi recipe connect kia hai o dikhayga

*** Ab Node ko access karenge ****
chef- client = srf client ko call karnhe baki nahi likhn hai bcz already node
server ke sath connected hai
now all files will be updated, go to browser,paste public ip of node u will get webpage

vi cookbook/apache-cookbook/recipes/apache-recipe.rb
kuch upadate karlo and save file

ab ye humne WS pe update kia lkn server pe nahi gaya to use upload karlo
knife cookbook upload apache-cookbook = cookbook upload hgi
node ka chef-client run karo..changes nazr ayga

**** ab isi kam ko automated karna hai, chef client likhne ki jarurt nahi rhni chy *****
hum jo bhi update kare o kam hume direclty dikhna chy,,bar bar WS mai jake cookbook 
upload karo fir node mai ake chef client ko run karo..iss process ko automate karna hai

///// command for automation ////
go to node1
vi/etc/crontab
* * * * * root chef-client {min hr day month week}
go to WS
Chef repo mai jao = ar vi editor se content update karo ar server pe upload karo
2 kam apko hamesha karne padege,ek upadate karna padega recipe ko ar cookook ko 
server pe upload karna padega.. warna node uthayga kaise (pull type ise hi kahte hai)

thats the main thing in Chef ki ye pull type mechanism hai
matlab khud hoke server pe jata hai (node jata hai) ar jo bhi daata update hta hai 
o khud ko update karta rhta hai in every min and hours
matlab as devops hamara kam recipe update karna ar server pe upload karna us recipe or
cookbook ko itna hi rhta hai, baak autoomation to alreaady companies mai hta hi hai

// now create one more node ///
avance detail likhe 
#/bin/bash
sudo su
yum update -y
echo "* * * * * root chef-client">>/etc/crontab

go to WS and node ko bootstrap ko connect kare
run list add kare
and check in browser
