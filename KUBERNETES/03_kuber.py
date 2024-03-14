   ## 
Kubernetes Object 

jo kam ap manifest mai likhte hai use hum object kahte hai
its represent ur state of cluster
desired state kya hai check karte rahega k8 
specification mai apko kya chy ye likha hta hai
object ka har ek name nd ID hta hai
k8 POD bhi ek object hi hai
basica objects are
POD, SPECIFIATION , VOLUME,NAMESPACE, REPLICASET, SECRETS, DEPLOYMENT,JOBS, DOCIMENTS

POD manages contsiner
npde ke andar pod hote hai
replica set maneges pod

state = mtlb apke desired dtate or actual kya hai apke pas

### FEATURES OF PODS
Master kahi pe bhi pods create kar sakta hai kisi bhi node pe agar apko chy to mention karna padega
node fail to pod fail
node die ho jati hai fr pod bhi time out period ke bad band ho jati hai
pod delete hua to restart use nhi kar sat lekin create dusra ho jayga with diff IP 
volume tab tak exit karega jab tak pod rahega

feature of YAML file look from video ar notes direclty


## LABLES 
Lable kisi bhi object pe lagaya ja sakta hai ar selectors ap select karke leke ate hai
lble matlb phchan ne ka tarika
kitne bhi lable laga askte hai
it is key value pair 
jaldi se dhudne ke liye use kar sakte hai

yaml manifest file video se lena hai copy paste
kubectl gets pods or node  --show-labels 

labls declarative and imperative se bhi lagta hai 

imperative se direct commands se lagti hai
kubectl labels pods delhipod myname=sagar 

lables selectors two types 
equality based (= ,!=)
set based (in,not in andn exist)
env in (production,dev)
env notin (team1, team2)

kubectl gets pods -l 'env in(development,testing
666)'
