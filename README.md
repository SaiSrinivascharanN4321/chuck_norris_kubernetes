---
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

- 
Install Calico plugin 

kubectl create -f https://docs.projectcalico.org/manifests/tigera-operator.yaml


kubectl create -f https://docs.projectcalico.org/manifests/custom-resources.yaml

kubectl get pods --all-namespaces

kubectl taint nodes --all node-role.kubernetes.io/master-
