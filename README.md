# djangoRestApp

# Step by step instructions to run the microservice

# 1. Command to execute for running the Django rest application in a local machine

## Installing virtual env
python3 -m pip install --user virtualenv

## Create a venv
python -m venv venv

## Activate venv
source venv/bin/activate

## Installing requirements
pip install -r requirements.txt

# 2. Endpoint to call (with request information) to execute the POST operation

## POST type request URL:
0.0.0.0:8000

## Payload:
{
    "requestId": "###",
    "accountName": "###",
    "amount": "###"
}

# 3. docker-compose command to execute to build and run the application inside docker

## Check if docker is installed
sudo docker --version

## Command to build a docker image
sudo docker build -t rest-app-image .

## Check if docker compose is installed
sudo docker-compose --version

## Command to run the docker image(rest-app-image) we just created
sudo docker compose up -d

# 4. Endpoint with ip/port to call (with request information) to execute the POST operation from docker image.

## POST type request URL:
0.0.0.0:8000

## Payload:
{
    "requestId": "###",
    "accountName": "###",
    "amount": "###"
}
