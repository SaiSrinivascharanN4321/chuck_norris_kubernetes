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




# Wait till Ingress Controller is deployed
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=150s

# Create namespace 
kubectl create namespace $NAMESPACE || true

# Create mysql statefulset
kubectl -n $NAMESPACE apply -f deploy/mysql/

# Wait till statefulset is available
kubectl wait -n $NAMESPACE \
  --for=condition=ready pod \
  --selector=app=mysql \
  --timeout=150s


# Create application resources
kubectl -n $NAMESPACE apply -f deploy/api/

# Wait till deployment is available
kubectl wait -n $NAMESPACE \
  --for=condition=ready pod \
  --selector=app=chuck-norris-api \
  --timeout=150s

echo -e "Application deployed"



