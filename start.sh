
docker build -t myimage .
# docker compose up -d # Check if the container already exists and remove it if so
if [ "$(docker ps -aq -f name=mycontainer)" ]; then
    docker rm -f mycontainer
fi
docker run -d --name mycontainer -p 80:80 myimage

# docker compose up -d