### FAST API Azure DevOps project 


```
Steps
-------
pip3 install -r requirements.txt
uvicorn main:app --reload # The --reload flag enables automatic reloading of the server when code changes are detected.

docker build . -t fast-api
docker run -p 8000:8000 fast-api



```
