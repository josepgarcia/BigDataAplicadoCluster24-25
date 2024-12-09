FROM debian:stable-slim

###################################################
# Install necessary packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        openssh-server \
        wget \
        sudo \
        vim \
        nano

###################################################
# User configuration
# Create user called "user" and group
RUN groupadd user && \
    useradd -ms /bin/bash -g user user

# Allow hadoop user to use sudo without password
RUN echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

###################################################
# Expose ports
EXPOSE 22

USER user
