#!/bin/bash

# exit when any command fails
set -e


KUBECTL_VERSION_COMMAND="kubectl version"
NAMESPACE=chuck-norris-api
DEPLOYMENT=chuck-norris-api
STATEFULSET=mysql

#################################################
################ Start of script ################
#################################################

echo -e "\n========= Application deployment started ==========\n"


kubectl create ns ingress-nginx

#adding nginx ingress
#kubectl -n ingress-nginx apply -f scripts/deploy.yaml

# Wait till Ingress Controller is deployed
sleep 30

# Create namespace 
kubectl create namespace $NAMESPACE || true

# Create mysql statefulset
#kubectl -n $NAMESPACE apply -f deploy/mysql/

# Wait till statefulset is available

sleep 20

# Create application resources
#kubectl -n $NAMESPACE apply -f deploy/api/

# Wait till deployment is available
sleep 4

echo -e "namespace created and now its time to deploy applications"



