# Creating a venv Environment for Scripts and Jupyter Notebooks
python3.9 -m venv venv

## Activating the Environment
source venv/bin/activate

## Installing the Requirements
pip install -r requirements.txt

## Commands
python main.py

### Build image
docker build -t lambda_image .

### Create container
docker run --name lambda_container lambda_image

### Remove container
docker rm -f [container_id]

### Remove image
docker rmi lambda_image

