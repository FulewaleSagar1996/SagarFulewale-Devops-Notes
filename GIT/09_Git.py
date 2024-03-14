# ****** HOW TO COMMIT PUSH AND PULL FROM GITHUB.

# login into mumbai ec2 instpances
# create ome directory amd go inside it
# git init = issr directory git ke local repo mai aa jaygi
# touch myfile= and put some data into that file
# git status = isse paata chalega ki file mai kya hai ya empty hai
# git add . = workspace se staging area mai jayga code
# git commit -m "message for your commit"
# git status = ab o working area khali dikhayga q k sara code uthake staging area m tha
# ar uske bad commit kia tha
# git log = ye commit kisne kia tha ye smaj mai ata hai.email id tim sab etc
# git show <commit id>= kya code commmit kia hai o dikhta hai
# ab sare kam ko apko central repo mai dalna hai to uski command hai niche
# git remote add origin <centralrepo url> = phle hum add karke local repo ar central
# repositiory matlab github ko connect karte hai ek dusre ke sath tbhi to code push 
# kar payenge
# git push -u origin master/main
# uske bad o username ar passs puchega github ka o enter karna hai
# apka pura code local repo se central repo mai uthake chala jayga
# ab code dono jagah hai

# now go to singapore ec2 instance create one dir and go inside it 
# git init
# git remote add origin url
# git pull -u origin master/main
# git log 
# git show <commit id>
# git status 
# git add . 
# git commit -m "singapore update"
# git status
# git log
# git pull origin master or main

# git ignore
# agar diff diff file hai ar unpe pe igonore karna chata hu
]# tab ignore use kr sakte hai
# create ignore file .gitignore alwys
# git add .gitignore
# git commit -m "latest update excluded css"
# git status
# 





















