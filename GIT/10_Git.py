****** Branch ******

by default master branch hti hai git mai and it is very important
for more inform check your screenshot in mobile
master branch se hum parralely kam kar sakate hai ar maaster branch pe koi 
asar ya error nahi hga
har ek task ke liye alag branch hti hai
code hone k bad branch code ko hum master mai merge kar lete hai
jaha se branch nikalti hai whaa se first tim pura copy ho jata hai
working space ka kamm hame tino branches se najar ayga jo branch humne banayi ho 3
jab tak ap workspace ka kam staging area mai add nahi karte ar loacl repo mai 
commit nahi karte hai taab tak hume sabbhi branch se kam nzr ayga
lekin jaise hi add ar commit karega tab o usi branch mai nzr ayga
example of shadi witjh ur gf

***commands****
sudo su
cd mumbaigit or singapuregit
git log --oneline == isse commit nazar aynge in one line
git branch 
output is master eith *= start ka matlab present isme kam kar rhe ho
for new branch = git branch <branchname>
for change ur branch = git checkout <branchname>
fir ap dusre branch mai aa jynge
git branch -d <branchname> = for delete ur branch
git branch -D <branchname>  = for focefully delte

*** MERGE ****
we use pulling mechanism in merge branches.pulling mech mai o kam pull karte hai 
jo kam newly add hota hai.copy paste hta hai merge mai
github mai bhi banches hti hai
ap branchesa diff repo ke merges nahi kar sakte hai.apne hi repo ke branch ko merge kar skate hai
git merge <branch name> = for merging
git log
git push origin master

*** Git Conflict ***
jab hum merge karte hai tab conflict ata hai tab similar chize milti hai 
dono same name ki file hai branch ar master mai
when same name file have different cotent in difff branches if you do merge conflict occurs
conflict occurs when you merge branch
same file diff data

***Git stashing *****
bht sara code ikh liya hai ar bich mai koi ar work aya hai to use chhodna padta hai
lkn apke pas tp workspace ek hi hai to hum kaise kare..hume o file filal ke liye 
stash mai bhej denge ar naya aya hua kam karennge, ar kam hone ke bad stash wala
code laynge ar phle ka kam kar sakte hai
commands =
git stash = stash mai code chala jayga
git stash list = multiple file dekh skte hai
git stash apply stash{0} = konsi stash file pe kam karna hai,choose frm list
git stash clear = dlt ho jygi file from stash














