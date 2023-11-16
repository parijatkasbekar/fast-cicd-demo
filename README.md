### FAST API Azure DevOps project 


Steps to build the app

```
pip3 install -r requirements.txt
uvicorn main:app --reload # The --reload flag enables automatic reloading of the server when code changes are detected.

docker build . -t fast-api
docker run -p 8000:8000 fast-api

```

- PyTest is used for testing the app

- Registry used is `parijatkasbekar/fast-greeter` hosted in `dockerhub`

- Prometheus based monitoring set up in the cluster

- `kubectl get svc` to see the services are that exposed
