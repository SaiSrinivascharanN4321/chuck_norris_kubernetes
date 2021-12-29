

__Install kubeadm__


__(i)Preparing VM__

- sudo su

- swapoff -a

- vi /etc/fstab

comment out the appropriate line, as in:

#UUID=d0200036-b211-4e6e-a194-ac2e51dfb27d none         swap sw           0    0


- vi /etc/ufw/sysctl.conf

Add the following

net/bridge/bridge-nf-call-ip6tables = 1

net/bridge/bridge-nf-call-iptables = 1

net/bridge/bridge-nf-call-arptables = 1

Reboot the machine so changes takes place


- sudo su

  apt-get install ebtables ethtool

__(ii) Kubeadm install process__

__(a)__ Install docker

-Install docker 

sudo su

apt-get update

apt-get install -y docker.io


- Install https support components and curl

apt-get update 

apt-get install -y apt-transport-https

apt-get install curl

- Retreive key and k8s repo to your system

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

cat <<EOF >/etc/apt/sources.list.d/kubernetes.list

deb http://apt.kubernetes.io/ kubernetes-xenial main

EOF

- and install kubelet , kubeadm and kubectl

apt-get update

apt-get install -y kubelet kubeadm kubectl



__(iii)__ Create a cluster

- kubeadm init --pod-network-cidr=192.168.0.0/16

- open another terminal and run them as a regular user , you can also use sudo su 


  mkdir -p $HOME/.kube

  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

  sudo chown $(id -u): $(id -g) $HOME/.kube/config

 copy the source files to your home directory

- Install Calico plugin 

kubectl create -f https://docs.projectcalico.org/manifests/tigera-operator.yaml


kubectl create -f https://docs.projectcalico.org/manifests/custom-resources.yaml

kubectl get pods --all-namespaces

kubectl taint nodes --all node-role.kubernetes.io/master-





__Create namespace for nginx ingress and chuck norris api__

Run the following bash scripts
 
./deploy.sh

./applications.sh





__Requirements__

golang 1.16



__Execution__

Run 

sudo docker-compose up -d 

to start the local development environment i.e. mysql; the backing service


Run 

SQL_PASSWORD=root make run 

to run the application that serves on port 8080

__Endpoints__

- GET /banter returns a list of jokes

- GET /health/live checks for the liveness of application

- GET /health/ready checks for the readiness of application to accept traffic. 



__Idea of deployment__

The idea of dpeloyment is to have 
- Simple storage server i.e. MYSQL
- REST API server that exposes /banter endpoint to retrieve list of all jokes from the storage server
- Reverse proxy that serves the REST API server



__Additional Ideas added but could not be executed__

There are two files in additional_ideas and are python files. The inital idea was to use stateless api to act as a storage and also idea was to execute this python application with Dockerfile
  

Please clone the repository and enter into it


__References__

- https://github.com/ahmedwaleedmalik/chuck-norris-api

- https://www.mirantis.com/blog/how-install-kubernetes-kubeadm/

- https://itnext.io/bare-metal-kubernetes-with-kubeadm-nginx-ingress-controller-and-haproxy-bb0a7ef29d4e


