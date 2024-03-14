### Why used Shell Script

We turne to aws from other platform...aws gives us better service
suppose i n ur company u give access of aws to 100developers and now u want to find that 
how many developers using jow much resources.if theres are lots of ebs volume in aws but no one used 
from many days..so our first goal when we used aws that is cost cutting.
for cost and mainatinace we trand=sfered to aws so that using shel script we can optimised it.

lets take example that..apke boss ne bola ki apko sham ko batye ki aws server pe kitne s3 buckets,kitne
ec2 instances,kitne iam user chal rahe hai to fit ap manually jake nahi kar sakte hai isly
apko shell script se automate karna padta hai.
agar roj apko report chy sham ko 7 baje hi to apko cronejo set karna padta hai jo usi tim pe shell script
ko execute karega ar sari resources ki list apko dega.....

*** shell srcipt ke liye apko ec2 intance ar aws cli chy.aws cli configure karne padega aws ke sath.

hum jab shell script likhneghe tab aws ki jo bhi info chy uske liye apko command chy...
o sab gooogle mai awscli command refrence mai milega.search it.

shell script ke liye bash use karnge.
filename....sagar.sh 
fir permisiion denge chmod 777 filename
and then execute karne ke liye.... (./ sagar.sh)

###################################################################################

TAKE 02 (DAY 08)

U can talk to application with api and cli ...
we integrate github and shell script with api ...bcz it is traditional.with shell script(bash),python, 
