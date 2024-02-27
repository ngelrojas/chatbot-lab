# Use an official Debian runtime as a parent image
FROM debian:buster-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install required packages
RUN apt-get update && apt-get install -y curl build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev uuid-dev

# Download and install Python 3.11
RUN curl -O https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz \
  && tar -xvf Python-3.11.0.tgz \
  && cd Python-3.11.0 \
  && ./configure --enable-optimizations \
  && make altinstall

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python3.11 get-pip.py

# Install Poetry
RUN pip install --no-cache-dir poetry

# Use Poetry to install dependencies
RUN poetry config virtualenvs.create false \
  && poetry add llama-cpp-python==0.2.44 \
  && poetry install --no-interaction --no-ansi

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run app.py when the container launches
CMD ["python3", "app.py"]
