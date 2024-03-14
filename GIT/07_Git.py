# git is simple open source software
# Git hub ar git lab yah ek service hai ya fir ap usko storage bhi bol 
# sakte hai jaha o hamara data store karke rakhti hai as central repository

# ****** stages of git and workflow *********

# sabse pahle ap ec2 machine mai joge..rgion create kroge
# uske bad ek directory create karenge  fir git init command chalaynge
# git init matlab initialize kardo to fr uske bad o dir git or local repository mai 
# convert ho jaygi to fir waha pe 3 logical area ban jate hai
# workspace or working area, staging area, and local space ar ye tino ko milake 
# use hum local repo kahte hai.local repo matlab hmare system ke andar ek
# folder ban jayga git nam ka sab isme hi save hga
# 3 stages hto hai
# working directory, staging area, local repo
# jaha hum editing ya code likhte hai use working dir kahte hai
# fir us code ko hume commit bhi karna padta hai lkn hum direclty commit nai 
# karte..sabse pahle hum usko add karte hai staging area mai..(example shahi paneer)
# add == working space se staging area mai code ko save karna 
# jo chize commit karna chahte hai o hum staging mai rakhte hai..select karte hai
# staging se local repo mai jab bhejte hai use commit kahte hai..snapshot ya save bhi
# kahte hai..commit jab karte hai tab uspe hum tag nhi laga sakte hai.
# Staging area mai ap select karke rakh sakte ho fir jo choose karna hai ya commit
# karna hai use commit kar sakte hai ho.
# uske bad picture mai guthub ayga which is central repo.or storage.agr apka code ho gya complt
# tab ap apne code ko push karenge github mai.apka code ab central repo mai bhi hai ar local
# repo mai bhi hai jaha apka local repo mai ek master branch bana hua hta hai by default
# jb hum staging area se kuch commit karte hai tab o local repo ke branch mai aa jati h
# github mai jo code humne push kia tha o code koi ec2 machine (singapore) pull kar sakti h
# sara code uthake aa jayga first tim mai..fir o apna kam karega  ar github m push krega
# agla banda (mumbai) ka wha se pull karega github se
# jab bhi hum hum code add karte hai github mai to ek har bar nayi commit id ban jati h
# uske alag alg version ban jate hai ar hum koi bhi code use kar skate hai as per our req.
# sab changes ar kisne kya kia tha konsa kam kisne kia tha sab dikh jata hai
# commit jo hte hai o always incremental hte hai matlab jitna change kia h utna hi save hga
# this is the procedure of github

# Repository = local bhi hti hai ar central bhi.it is a place where u have all your codes
# or kind of folders on server.it is a kind of folder related to one product
# changes are personal to that perticular repo.

# server = matlan j humne leke rakha hai like linux machine on aws
# its store all repository.it contains all metadata(commit id and tags)

# working directory = where you see files physically ans do modification
# at a time you can work om perticular branch

# in other cvcs, developers generally makes modification and commmit there changes directly to
# the repo  but git uses a diffrent strategy. git does not track each and evry modified file.
# whenever u do commit an operation ,git looks for the files present in the staging area only
# those files presemt in the staging area are considered for commit and not all modified files.

# WORKING DIRECTORY--->ADD-->STAGING AREA-->COMMIT-->LOCAL REPO-->PUSH/PULL-->GITHUB

# COMMIT = store changes in repo you will get one commit id.it is 40alphabet numeric character.
# it  uses SHA-1 checksum concept.even of u changes one dot , commit id will get change.
# it actually hepls you to track the changes.commit is also known as SHA1 hash.
# checksum concept ek value hti hai.example aagr hum 1000words ka code likh rahe hai to use 
# o binary no mai conver  karta hai jise hum checksum value kahte hai.test karne ka ye tarika hai
# code ke sath kuch chedkhani nahi ki hai o samjme ata hai ar checksum change hta hai.

# commit ID = regfrence to identify each chnges.and to identify who change file

# tags = tags assign to meaningful name  to specify version in the repo.once a tags is created
# a perticular save even if you create a new commit it will not be updated.

# snapshot - represent same data of  perticulaer time. it is alwys  incremental  that is  it 
# store the changes only, not entire file. lkn dikhayga sab kuch

# Push = push operation copies changes from a local repo server to remote or central
# repo . this is used to store the changes permanently into the git repository.

# Pull = pull operation copies the changes from a remote repo to a local machine . the pull 
# operation is used for synchronisation between two repo.

# Branch = hum jo bhi kam karte hai by default master branch mai karte hai
# branch banana bht imp hta hai.agr parallely koi kam krna hia kisiko to hum usko branch
# banake dete hai taki wha kam  kar paye.usse master branch pe koi frk nahi padte hai
# branch hum as a experiment bhi uuse kar skate hai.branch banne par sara code copy hoke
# aa jata hia first time pe srf. uske bad kam acha raha to hum us kam ko merge bhi kar sakte hai
# product is saame, so one repo but diffrent task
# each tosk has one seperate branch.finally merges all branches.it is useful when u have to
# work parralely. it can create one brach on the basis of another branch.changes are persomal
# to that perticulalr branch

# *** ADVANTAGES ****
# FREE and open source
# fast nd small, security ,no need of poerful hardware, eaiser branching 
# use snapshot in mobile




