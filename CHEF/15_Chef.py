*** insert linux command , create user & group , runlist

koii agar recipe banayi hai to usme hum linux command kaise chala 
sakte hai,group  ar ek se jada recipe chalana chahte hai ek cookbook
ki ya diffrent cookbook ki ye sikhnge

** how to execute linux commands **
login into amazon linux 
sudo su
cd cookbook
ls
vi test-cookbook/recipes/test-recipe.rb
yaha pe code likhnge jo ki linux ke help se rhga
execute 'run a script do'
command << EOH {end of here} yaha se linux start hga ar rubi end hga
mkdir /rajputdir
touch /rajputfile
EOH
end
now to run this recipe
chef-client -zr "recipe[test-cookbook::test-recipe]"
ls /

linux command ko hum recipe mai jaddause nahi karnge q ki isme
idempotency nahi rahti .matlab ek hi kam bar bar karta hai
jitne bar run karoge utne bar file create hti jaygi

iske bad add user ar create group ka code vid se dekhna
ya fir mobile mai screenshot dekh le

We run chef client to apply recipe to bring node into desired
state this process kmown as convergence

what is runlist??
To run the recipes in a sequence order that we mention in a run list
matlab jo recipe pahlel likhi hgi o pahle run hagi baki bad mai
lkn ap multiple recipe to run kara sakte hai lkn condition ye hti ki
at a tim ek cookbook ki srf ek recipe run kara sakte hai

chef-client -zr "recipe [test-cookbook::test-recipe],recipe[apache
-cookbook::apache-recipe]"

***how to include multiple recipe from one cookbook*** with include

To call recipes/recipe from another recipe with in some cookbook
kisi bhi ek recipe ko uthaynge jaise most of the tim default recipe
hi uthaynge..koi bhi uth sakte ho
iske bad vi editor mai jynge with the default recipe ar uske andar
code mai include ke help se baki recipe ko add kar dnge
matlab jab bhi default run hgi tab puri recipe uske sath run ho jaygi

cookbook mai jana hai
vi test-cookbook/recipes/default.rb

include_recipe"test-cookbook::test-recipe"
include_recipe"test-cookbook::recipe2"

chef-client -zr "recipe[test-cookbook::default]"

Now we are combining previous two concept 
and run multipe recipe from multipe cookbook at one time

cookbook mai jana hai
chef-client -zr "recipe[test-cookbook::default],recipe[apache-
cookbook::default]"
 

