FROM python:3.8-slim

# set python environment
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y libpq-dev python-dev libsqlite3-mod-spatialite binutils gdal-bin

# Create work directory
WORKDIR /rpls-back

# Copy django directory to docker
COPY . /rpls-back

# install dependencies
RUN pip install -r requirements.txt
