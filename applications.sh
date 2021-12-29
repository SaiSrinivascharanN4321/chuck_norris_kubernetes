kubectl -n ingress-nginx apply -f deploy.yaml
kubectl -n chuck-norris-api apply -f deploy/mysql/
kubectl -n chuck-norris-api apply -f deploy/api/
