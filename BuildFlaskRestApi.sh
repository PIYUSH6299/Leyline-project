#!/bin/sh
abort()
{
    echo >&2 '
***************
*** ABORTED buildflaskapi ***
***************
'
    echo "An error occurred buildImageUploadImage . Exiting..." >&2
    exit 1
}

trap 'abort' 0

set -e
#TODO: add check to ensure the user is logged in.
echo "Please ensure you are logged in to docker / docker desktop"

#Kill the process
echo 'Reset Docker to prevent connection error'
unset DOCKER_HOST
unset DOCKER_TLS_VERIFY
unset DOCKER_TLS_PATH
echo "Trying to login. If you are NOT logged in, there will be a prompt"
docker login
docker ps

CURRENT_DATE=`date +%b-%d-%y_%I_%M_%p`
echo "CURRENT_DATE:"+$CURRENT_DATE

# It will print the log folder wise
echo "Building flask-rest-api docker image"
docker build -f Dockerfile -t $DOCKER_USER_ID/flask-rest-api-web:latest .

# Now image building is done 
# So now we will push that image to dockerhub
echo "Pushing flask-rest-api"
docker push $DOCKER_USER_ID/flask-rest-api-web:latest

# docker pull $DOCKER_USER_ID/flask-rest-api

trap : 0

echo >&2 '
************
*** DONE buildflaskapi ***
************'