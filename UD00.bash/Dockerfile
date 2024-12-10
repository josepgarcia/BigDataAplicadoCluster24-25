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
# Configure SSH
RUN mkdir /var/run/sshd
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'user:123123' | chpasswd

# Generate SSH host keys
RUN ssh-keygen -A

###################################################
EXPOSE 22

#USER user
USER root

###################################################
# Keep the container running and start ssh
CMD ["/usr/sbin/sshd", "-D"]
