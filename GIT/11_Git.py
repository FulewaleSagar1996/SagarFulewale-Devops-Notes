

***git reset****
agar apne galti se file add kia ho staging area mai ar use dlt karna ho 
toh hum reset karte hai matlab file staging area se reset ho jaygi

***** Git revert *****
agar apne galat code ko commit kar diya hai to fir revert karna hai
berfore commit use reset
revery jo hai public file pe kia jata hai ar reset hai o private file pe
public matlab central repo ar private matlb local repo r staging area wali file
revert mai apko jo kam glt hua hai o namhi milega uske phle ka kam milega
like agar apne xyz code likha hai uske bad xyz abc likha hai ar ye file galat h
hai jise hum commit kar chuke hai to revert ke bad xyz wali file milegi
purane kam ko age lake rakh dete hai,kam dlt nahi karte.undo ho jata hai
git revert mai default nayi commit jati hai.apka kam piche ka mil raha
hai lekin commit id age badte jati hai.
version control system moves forward but your file move backword

Command ***
sudo su
cd mumbaigit 
ls
git status
cat > newfile
git add .
git commit -m ""
git log --oneline
git revert <commit id>

*****
delete untracke file = git clean -n (isme puchta hai)
git clean -f = isme forcefully hta hai dlt

Tags****
commit id se hum pata nahi laga sakte hai agr usme hume future mai kam karna hai toh
hum use tag de sakte hai to tack karna jada easy hta hai
 
to apply tag
git tag -a<tagname> -m <message><commit id>
to see perticular commit content by using tag
git show <tag name>
git tag -d <tagname> = to dlt tag
git tag = list of tags.

***** Github Cloning ********
jaise se hum add karte hai push pull karte hia data from central repo wse hi clone 
se data le sakte hai..isme hume direclty milta hai data clone hoke
git clone <url of central repo>
git hub mai no nam se hga repo usi name se clone hga

****similarities in git and github ******
github ar git ma master branch hti hai byb default
github mai bhi branches bana sakte hai like git
frk srf command line git mai ar github mai GUI hta hai
dono mai merge bhi kar sakte hia apne branch
pulling req ka m purpose ye hai i koi branch merge kaar rahe hai to kuch conflict n=to nahi 
hga n ye check karta hai



