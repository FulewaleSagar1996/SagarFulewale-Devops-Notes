# node ke andar pod
pod manages conataier
replicate sets manages pod

state = object ki state kya hota hai ya fir kitni replica hai,konse port
map kiye hai,volume konsa map kia hai,image konsi hai

imperative method = matlab direclty command se karwana
declarative = matalb manifest mai sab likhte hai like recipe in chef
isme hum reuse kar sakte hai..json or yml mai hti hai

# ### Features of pods
1.master apni pasand se pod create karega koi bhi node mai agar 
hga to manifesst mai mention karna padega
2.pod apke node mai tabtak rahega jab tak koi process fail na ho jaye
ya pod dlt na ho jaye,ya fir node na rahe otherwise apka pod rahta hai
3.node fail to pod fail 
4. pod agar fail ho gaya to dusra banaega with diff id but o pod hum start
ni kar sakte agar khrb ho gya hai toh 
5.

# KUBERNETES CONFIGURATION 

1.All in one single node installation
--- master aur worker ek hi instances pe kam karte hai..ek hi jagah pe 
--- this is not in real time enviormenmt 
--- very useful for learning 
--- minicube is example
 
2.Single master and multiworker installation 
---ek master and 3 worker mtalba 4 instances
--- real time env 

3.multimaster and multiworker intsallation 
---real time env 

yaml file -----

pod1.yml or yaml --- file name

see form videos
 
 ## how to install kubectl and minicube all in videos just copy and paste
 
 ## some k8 commands
 -- kubectl get node === kitne node hai pata lagega
 -- kubectl describe node nodename or nodeprivate id
 -- kubectl apply -f yamlfilename == isse pod run bhi hga ar create hga
 -- kubectl get pods == kitne pod hai bataygea
 -- kubectl get pods -o wide == pod kis node mai exaclty create hua hai pata lagega
 -- kubectl descibe pod podname == pod ka pura details
 -- kubectl logs -f podname == container mai kya kam chal raha hai pata chalega
 -- kubectl delete pod podname