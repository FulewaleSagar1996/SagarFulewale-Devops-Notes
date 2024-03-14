**** What is Chef Attributes ****
it is a key value pair
jaha hum code likhte hai waha use hta hai
ceo ka example use karo...hmae har jagah uska nam nahi ikhna padega
sirf key mai value likhnge baki sabhi jagh krne ki jarurt naui hai
ceo = sagar
isko hum hard coding nahi krte, usko variable mai likhte hai

check screenshot for below
attribute = is tis key value pair represent a specific detail 
about a node
who use it = chef-client..check karega server se
to determine = current state ky hai, past state kya hai 
jab chef client xhalaya, ar future mai k state rahegi chef cient
run karne ke bad

types of attribute [intervvies mai puacha ja sakta hai]
1.default
2.force default
3.normal
4.override
5.force override
6.automatic
iske priority bhi upper se niche

who defines attributes?
node, cookbook or recipe, roles and enviormnment

log into linux previous
sudo su 
ohai = node mai jo hai machine ka sab nazr ayga
node mai hmaesha automatic wali chizaee jada hti hai
ohai ipaddress
ohai memory/total
ohai cpu/0/mhz
ls
cd cookbook
ls
apache-cookbook
cd apache-cookbook
tree
chef generate recipe recipe-new
cd ..
vi apache-cookbook/recipes/recipe-new.rb
pura code video se copy kar lena
sab code variable ke form mai rahega
chef-client -zr "recipe[apache-cookbook::recipe-new]"
chef client pahle ohai mai jayga puchega, updated hai, instal hai ya
nahi fir o chef server pe jayga ar layga code ar update kerge
ls/
cat /basicinfo

mkachine ko stop kardo
