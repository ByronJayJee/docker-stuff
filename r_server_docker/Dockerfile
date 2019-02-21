# Use official Ubuntu 16.04 as parent image
FROM conda/miniconda3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
#COPY . /app

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

# Make port 5443 available to the world outside this container
EXPOSE 5443

# Define environment variable
#ENV NAME World

RUN conda install --quiet --yes -c r r
RUN conda install --quiet --yes -c r r-plumber

# Set the working directory to /app/bind
WORKDIR /app/bind

# Run app.py when the container launches
#CMD ["echo", "hey!"]
CMD ["./run_script_r_server"]
