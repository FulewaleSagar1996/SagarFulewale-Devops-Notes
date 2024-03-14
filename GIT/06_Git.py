####### Git ######

# why use Git
# jab hum koi software banate hai to developer code karte hai
# IT mai ek wrd use hta hai jises software configuration managent ya fir 
# source code managment..toh jo code developer likh rahe hai use manage karna 
# sorce code managmtn code ke version ko sambhalke rakhta hai
# iske bhi do type hote hai---centralised version control system(cvcs) and distributed version con sys
# git yah distributed hai

# git is a software..linux waale ne hi banaya hai in 2005.
# github ek repository ki tarah kam karta hai jo centralised hoti hai like remote server

# jitne bbi changes hum karte hai sab pata chalata hai ar uska naya version create hta hai
# git mai central repo ke sath sath local repo bhi hti hai jo hum khud ke system mai hi hta hai
# jisse koi bhi intrnet nahi lagata ar kam fast hta hai
# har logo ke pass unke systm mai local repo hone ki wajah se ek extra copy rahti hai jo 
# cvcs mai nahi hta tha..lkn distr mai 2 copy hti hai ek central repo ar local repo
# code completea hone k bad hum apne code ko commit karte hai local repo mai mtb save krte hai
# commit and update karte rhnge,,,ar uske bad hamara kam baki log  dekh sake ya apna code
# baki log use kar sake isly apne kam ko hum centralised repo mai dalte hai (pull push) jo github karta hai
# fir koi dusra pc2 wala dekh saakta hai...loacal pc sakbke alag hte hia isly phle ni dekh skte
# actully main repo mai jo metadata hai files hai o data inke local repo mai bhi 
# pada hta hai..matlab ek copy extra hti hai

# cvcs mai copy nahi hti..cvcs easy hta hai lkn dvcs begiiner ke liye hard hai



####### some usual command from abhishekhhhhhh

 /
 ls
    2  git version
    3  cat example.com
    4  mkdir example.com
    5  ls
    6  cd example.com
    7  ls
    8  vi calculator.sh
    9  ls
   10  apt-get install git
   11  git
   12  git init
   13  ls
   14  git add got commit git push
   15  ls -la
   16  ls
   17  ls -ls
   18  ls -la
   19  ls .git
   20  git status
   21  git add calculator.sh
   22  git status
   23  cd calculator.sh
   24  vi calculator.sh
   25  git status
   26  git diff
   27  ls
   28  vi calculator.sh
   29  git commit -m "this is my frst commit"
   30  git status
   31  git add .
   32  git status
   33  vi calculator.sh
   34  git add .
   35  git status
   36  git add calculator.sh
   37  git status
   38  git diff
   39  vi calculator.sh
   40  git status
   41  git diff
   42  git add calculator.sh
   43  git status
   44  git commit -m "this is my second version"
   45  git log
   46  cat calculator.sh
   47  git log
   48  git reset --hard a0f2f4836ff2b89ea7f7621e23e2d2c96b420296
   49  cat calculator.sh
   50  history

#######  BRANCHING STRATEGYYYYYYY******

agar koi apllication bana gya hai ar kuch functions add karne hai tp us code mau
hame kuch changes add akara padta hai without doing anything in existing applicaition
to hum branch banate hai with updated version
eg.-
uber---they hav car faciltities and they want to add some bike facciloties 
and thats y they create a branch from existing code
this branch name as features branch (in real organisation)

braanch ike main,master,trunk,features,relesase,anda hot fix

we build our application from release branch...
master is for active development branch..waha chalta rahta hai coding

release branch se testing vgere hgi and product shift release branch se hi hoga

take example of k8s github

hotfix branch =  ye srf 2 3 din ke liye rahta hai jab kuch critical problem agar aa gya productionn 
mai ar o fix karna hai to hot fix branch  create karte hai 

hot fix branch ka code master ar release branch mai rhta hai....main/master alwys update rhta hai

master alwys upto date rhta hai..

There are three types of pulling code
https. ssh, and using git cli
https and ssh are common method to use. https mai password ki jarurt hti hai
where as in ssh hume srf public key jarurat hoti hai. joo hume github mai paste krni pdati hai
genereate on linux machine by ssh-keygen....copy public key and paste in github account

# WHAT IS DIFF BETWEEN FORK AND CLONE
CLONE MAI AP CODE DOWNLOAD KRTE HAI AR FORK MAI EXTRA COPY BAN JATI HAI....

WITH BRANCHES U CAN ISOLATE UR DEVELOPMENT ACTIVITIES
command 
git checkout -b branchname ----------making branch
git checkout main --------branch mai jane k liye

# for merging u can use 3 commands
git merge
git rebase
git cherry-pick

lifecycle------git add . && git commit && git push 

GIT COMMANDS WHICH USE MOSTLYYYYY day in day outt


-- git init
git add . ot git add nameoffile
git push 
git log
git log --oneline
git status
git checkout -b branchname----create branch
git branch -- no of branches
git checkout branchname--to going another branch
git merge
git rebase
