FROM ubuntu:22.04
RUN apt update -y && apt install -y python3 python3-pip 
WORKDIR / 
COPY . .  
RUN pip3 install -r requirements.txt 
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

