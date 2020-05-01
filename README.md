# Dash docker container

This repository contains the code needed to develop dash applications
on docker.

## Development

During the development of the application we will create a docker image base on the
configuration file `Dockerfile`. This Dockerfile does not copy the application code into
the image. It just copy the `requirements.txt`. This means we will 
need to map the folders with the application code.

### Build the image

```
docker build -t dash:1.0 .
```

### Run the image 

```
docker run -d -p 8050:8050 -v $(pwd):/app/ dash:1.0
```

## Production

Once you have your application ready for deployment, you can use the file
`Dockerfile.prod` to bundle your code into a docker image ready to deploy.

```
docker build -t name:version -f Dockerfile.prod
```
