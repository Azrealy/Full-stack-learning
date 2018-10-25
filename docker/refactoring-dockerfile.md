# Refactoring Dockerfile for image size

Docker images are built from a [layered filesystem](https://en.wikipedia.org/wiki/Aufs). Each layer only contain the differences between it and the one below it. At the top, you see a unified view, but the **history of how it was built is maintained**. Each line in a Dockerfile creates a new layer on top of the existing stack.

For example, like the `Dockerfile` following:
```bash
COPY /my_requirements /tmp/my_requirements

# install the requirements text.

RUN rm -rf /tmp/my_requirements
```
This dockerfile may look good for us, which copy the requirements directory and install the package based on the requirements. At last, run the remove directory command. But the layer copy the directory is still part of the image. Even if you remove it at the last. Every time you based this image to create a container will copy this directory.

It's better to write it all on one line so it's not committed to the images as separate layers. For example, you can rewrite the Dockerfile like following:
```bash
RUN cp -r /my_requirements /tmp/my_requirements \

# install the requirements text.

    && rm -rf /tmp/my_requirements
```
It's may be not look pretty, but it results a much more efficient image size. If that line annoys you, write it in a bash script, then `ADD` and `RUN` it in the Dockerfile.

# In practice, see an example

Here create a simple Dockerfile, which run a python service.
```bash
FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y curl python-pip

RUN pip install requests

ADD ./my_service.py /my_service.py

ENTRYPOINT [ "python", "/my_service.py" ]
```
`my_service.py` is a python script that simply print 'hello world' string.
```python
# -*- coding: utf-8 -*-

print('hello world')
```
Then build the image and check the size:
```bash
$ sudo docker build --build-arg https_proxy=$HTTPS_PROXY --build-arg http_proxy=$HTTP_PROXY -t size .

$ sudo docker images
REPOSITORY                               TAG                 IMAGE ID            CREATED             SIZE
size                                     latest              fcbf0a0cf86e        12 seconds ago      355.4 MB
docker.io/ubuntu                         14.04               f216cfb59484        6 days ago          188 MB
```
We noticed our image size is doubled to the original ubuntu image size to run the 'hello world' python script. What exactly is being reported in the 355.4 MB number? It’s the total of the “visible” layer (the top one, da8… in my example) and all layers that were used to create this top layer.

# Adding a cleanup layer

We should probably clean up after ourselves. So rewrite this Dockerfile like this:
```bash
FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y curl python-pip

RUN pip install requests

## Clean up
RUN apt-get remove -y python-pip curl
RUN rm -rf /var/lib/apt/lists/*

ADD ./my_service.py /my_service.py
ENTRYPOINT ["python", "/my_service.py"]
```
Building and checking on that yields:
```bash
$ sudo docker build --build-arg https_proxy=$HTTPS_PROXY --build-arg http_proxy=$HTTP_PROXY -t size .
$ sudo docker images
REPOSITORY      TAG           IMAGE ID            CREATED           VIRTUAL SIZE
size            latest        c6dacdd00660        2 seconds ago     361.3 MB
ubuntu          14.04         6cc0fc2a5ee3        2 weeks ago       187.9 MB
```
It grew larger. In this way look like our image size does not decreased by our package cleanup.

# Cleaning up in the same layer

Try collapsing the install and remove command into a single line:
```bash
FROM ubuntu:14.04
RUN apt-get update && \
    apt-get install -y curl python-pip && \
    pip install requests && \
    apt-get remove -y python-pip curl && \
    rm -rf /var/lib/apt/lists/*

ADD ./my_service.py /my_service.py
ENTRYPOINT ["python", "/my_service.py"]
```
Building and running this version yields:
```bash
$ sudo docker build --build-arg https_proxy=$HTTPS_PROXY --build-arg http_proxy=$HTTP_PROXY -t size .

$ sudo docker images
REPOSITORY      TAG           IMAGE ID            CREATED           VIRTUAL SIZE
size            latest        e531f8674f33        9 seconds ago     338 MB
ubuntu          14.04         6cc0fc2a5ee3        2 weeks ago       187.9 MB
```
That look like smaller than the pervious one, But why is it still so huge?

The answer is the "recommended" package has been installed from the `apt-get install` command, we can use the option `--no-install-recommends` to optimize our Dockerfile look like this:
```bash
FROM ubuntu:14.04
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl python-pip && \
    pip install requests && \
    apt-get remove -y python-pip curl && \
    rm -rf /var/lib/apt/lists/*

ADD ./my_service.py /my_service.py
ENTRYPOINT ["python", "/my_service.py"]
```
Building and running this version yields:
```bash
REPOSITORY      TAG           IMAGE ID            CREATED           VIRTUAL SIZE
size            latest        fddc30aee4dc        6 seconds ago     229.2 MB
ubuntu          14.04         6cc0fc2a5ee3        2 weeks ago       187.9 MB
```
This time the size of image is dropped significantly.