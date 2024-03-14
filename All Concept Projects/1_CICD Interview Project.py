
1...FIRST PROJECT CICD END TO END PIPELINE 


-***We have a setup (we have a git repo) where we have a application source code....
lets takse we have a JAVA based application..now as soon as the devveloper raises  a pull request 
to this git repository we have configuered webhooks using the webhooks we trigerred the
jenkins pipeline (there are many way to trigereed like poll scm and build trigeered but in this 
way jenkins create a lot of api request so it is not that much gooddd.)

***so what we have done..we used declarative jenkins pipeline because it is easy pipeline to write 
and collabrate and as part of declarative jenkins pippeline we run multiple stages and some of these
stages are.......
build stages..in build satge we used maven as a build langauges and in that we do is we build the 
application and if the build is successful or the application built is successfully where we also execute some unit test case.

we perform some stati code analysis and varify that the appliaction is not expose to static code and after that..

we also havs sass and sast tool, sonarqube where we varify the apllicaation security if this new change that developer writing 
introdce any security valnerability..if any of these things fail then we would send email notification or 
slcak notification that we configuered,,,,,and lets say all of these stages are successfully done then we would go forward 
and we would create a docker image...

so we are running a simple shell target to createthe docker image out of the docker file which we have stored in git repo 
itself and as soon as the docker image created again using the shell command we push these docker images to container
registory (like docker hub,ECR etc)

this is our CI proces...

Once ther docker image is pushed to the elasticcontainer or docker hub 

we have k8s cluster, inside the k8s cluster we deploy the two continous delivery tools

one is the argo images updater and second one is argocd..both are k8s controller which we deploy in k8s cluster

what they do.....is the first tool argo image updater
it cont monitor the images registry and as soon as the new images is created it will picked up the new image and it will
update the  image in another git repository that we have and this git repository is purely for the image manifest.


that is our helm chart or customize or pod .ml, deploy.yml......as sooon as this git hub repository is updated with 
the new image then other k8s controller which we have is argo cd it takes the new images and deploy on the k8s clusture.
 
so these our CD process..
so this is our setupppppppppppp

NOTEEEE: in this explaination we taken argo image updater but now it is not in evry organisation it used.

so in place of argo image updator we will take or write shell scripting..it will automatically update the manifest 
----fom here u can continue your discussion 
after sonarqube/////we will move towards building the docker image for this artifact we push the docker image
to docker hub and what will do is using the shell script we will direcltly or automatically update the manifest
repo and then using argo cd we will deploy this manifest automatically to the k8s clusture

(here in this project we have two basically two repo one is for source code anf the other is for manifest to increase the 
 capabilities of Git)
 
 note:
     1. HERE WE USED OPERATOR TO DOWNLOAD ARGOCD..
     2. Sonarqube ke liye dusra server create karna hi pdega q ki ek isme sab ni rakh paynge.like devshack videos
     3. jenkins ke liye ek server,usi server mai maven aa jayga q ki wha hum docker agent use karke container
     run karwa rahe hai.
     4.for installing sonar ....    


# important commands for argo cd intallation using operator hub 

  170  minkube status
  171  minikube status
  172  vi argocd-basic.yml (create argoCd controller..for ex got to argocd operator documant in usage)
  173  kubectl apply -f argocd-basic.yml (usko create kro)
  174  kubectl get pods( see poda are running or not..isme argocd ke application ar services dikhte hai)
  175  kubectl get pods -w
  176  kubectl get svc(check argocd dervice )
  177  kubectl edit svc example-argocd-server(hume isme cluster ip ko nodeport mai convert karne hai to see ui of argocd)
  178  kubectl get svc
  179  minikube service example-argocd-server (ye serveice create krta hai ar url genrate karta hai jo hum browser mai access krnge)
  180  minikube service list
  181  kubectl get pods
  182  kubectl get secret (agrocd stored password in secret in argocd-cluster)
  183  kubectl edit example-argocd-cluster 
  184  kubectl edit secret example-argocd-cluster (copy that password link)
  185  echo  bzVuc0laUXp4dzBHT01ONFhKYldwRGExbThqQkZSQ0s= | base64 -d (its secret encypted in base64 )
  
  ### Hurdles in Project
  1.always check the permission of jenkins with  sudo su - 
usermod -aG docker jenkins ......then restart jenkins and try build.

2. check all credentials properly..specially your instance id shoud be correct in jenkinsfile.

3.give correct docker id, github id username properly .

4. check ur branch main ir master.

5.you can change image name also.

6.before building docker should be login with proepr username and passwrd which we entered in jenkinsfile.

7.after all configuration,u need to restart jenkins and then build




helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system --set clusterName=demo-cluster-three-tier-1 --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller --set region=us-east-1  --set vpcId=vpc-0d38e8518b19b2d34 