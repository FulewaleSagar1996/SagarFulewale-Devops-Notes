## INSTALLATION

sudo su
apt-get update
apt-get install apt-transport-https


apt install docker.io -y
docker --version
systemctl start docker
systemctl enable docker

sudo curl -s https://packages.cloud.google.com/apt... | sudo apt-key add 


nano /etc/apt/sources.list.d/kubernetes.list

deb http://apt.kubernetes.io/ kubernetes-xenial main


apt-get update

apt-get install -y kubelet kubeadm kubectl kubernetes-cni


BOOTSTRAPPING THE MASTER NODE (IN MASTER)

kubeadm init
 

COPY THE COMMAND TO RUN IN NODES & SAVE IN NOTEPAD

mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config


chown $(id -u):$(id -g) $HOME/.kube/config

kubectl apply -f https://raw.githubusercontent.com/cor...

kubectl apply -f https://raw.githubusercontent.com/cor...

CONFIGURE WORKER NODES (IN NODES)

COPY LONG CODE PROVIDED MY MASTER IN NODE NOW LIKE CODE GIVEN BELOW

e.g- kubeadm join 172.31.6.165:6443 --token kl9fhu.co2n90v3rxtqllrs --discovery-token-ca-cert-hash sha256:b0f8003d23dbf445e0132a53d7aa1922bdef8d553d9eca06e65c928322b3e7c0

GO TO MASTER AND RUN THIS COMMAND
kubectl get nodes