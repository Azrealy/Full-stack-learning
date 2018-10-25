FROM ubuntu:14.04
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl python-pip && \
    pip install requests && \
    apt-get remove -y python-pip curl && \
    rm -rf /var/lib/apt/lists/*

ADD ./my_service.py /my_service.py
ENTRYPOINT ["python", "/my_service.py"]