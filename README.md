# Dash docker container

This repository contains the code needed to develop dash applications
on docker.

## Development

### Pull the image from Docker Hub

For development you can directly pull the image from 
Docker Hub and start coding your Dash application in a 
file called `dash_app.py`. 

```
docker run -d -p 8050:8050 -v $(pwd):/app/ vioquedu/dash-dev:latest
```

### Build and run from Dockerfile

You can clone this repository and build the image from the code in it using the following command:

```
docker build -t image_name:tag .
```

```
docker run -d -p 8050:8050 -v $(pwd):/app/ image_name:tag
```

## Production

Once your application is ready for deployment, you can use the file `Dockerfile.prod` to bundle your code into a docker image ready to deploy.

```
docker build -t prod_image_name:version -f Dockerfile.prod .
```

Once build you can run your image with the following command:

```
docker run -p 80:80 prod_image_name:version 
```
