import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX'
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('local_file', 'bucket_name', 's3_file_name')

s3= boto3.client('s3',aws_access_Key_id = None, aws_secret_key=None)
s3.upload_file(localfile, bucketname,s3file)

'''
curl -sSL https://get.docker.com/ | sh
sudo systemctl start docker
sudo gpasswd -a "${USER}" docker
docker search mariadb
docker pull mariadb:10.4
docker images
docker-compose -f stack.yml up
docker ps

/// stac.yml
# Use root/example as user/password credentials
version: '3.1'

services:

  db:
    image: mariadb
    restart: always
    environment:
      MARIADB_ROOT_PASSWORD: example

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
'''