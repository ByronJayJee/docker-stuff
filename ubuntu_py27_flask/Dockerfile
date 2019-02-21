# Use official Ubuntu 16.04 as parent image
FROM ubuntu:16.04

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#RUN apt-get update

# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    vim \
###
    openjdk-8-jdk \
    git \
    curl \
###
 && apt-get clean

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
#ENV NAME World

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash 
ENV PATH=$CONDA_DIR/bin:$PATH 

# Install conda
ENV MINICONDA_VERSION 4.5.11
RUN cd /tmp && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    /bin/bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda config --system --prepend channels conda-forge && \
    $CONDA_DIR/bin/conda config --system --set auto_update_conda false && \
    $CONDA_DIR/bin/conda config --system --set show_channel_urls true && \
    $CONDA_DIR/bin/conda update --all --quiet --yes

RUN conda install --quiet --yes -c pytorch pytorch-nightly-cpu
RUN conda install --quiet --yes -c fastai torchvision-nightly-cpu
RUN conda install --quiet --yes -c fastai fastai

RUN conda install --quiet --yes -c conda-forge flask
RUN conda install --quiet --yes -c conda-forge flask-cors
RUN conda install --quiet --yes -c conda-forge flask-restful

# Run app.py when the container launches
CMD ["echo", "hey!"]
