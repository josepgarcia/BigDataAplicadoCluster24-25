# Base image
FROM openjdk:11-jdk

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV HADOOP_VERSION=3.4.1
ENV WORK_DIR=/usr/local
ENV HADOOP_HOME=/usr/local/hadoop
ENV JAVA_HOME=/usr/local/openjdk-11
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV HOSTNAME=hadoop-cluster

WORKDIR ${WORK_DIR}

RUN mkdir -p ${WORK_DIR}
RUN mkdir -p ${JAVA_HOME}

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
# Create hadoop user and group
RUN groupadd hadoop && \
    useradd -ms /bin/bash -g hadoop hadoop

# Allow hadoop user to use sudo without password
RUN echo "hadoop ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Configure SSH for hadoop user
RUN mkdir -p /home/hadoop/.ssh && \
    ssh-keygen -t rsa -f /home/hadoop/.ssh/id_rsa -q -N "" && \
    cat /home/hadoop/.ssh/id_rsa.pub >> /home/hadoop/.ssh/authorized_keys && \
    chown -R hadoop:hadoop /home/hadoop/.ssh && \
    chmod 600 /home/hadoop/.ssh/authorized_keys

COPY "./config/.bashrc" /home/hadoop/

###################################################
# Install Hadoop
COPY hadoop-${HADOOP_VERSION}.tar.gz /tmp/
RUN tar -xzvf /tmp/hadoop-${HADOOP_VERSION}.tar.gz -C /usr/local/ && \
    mv /usr/local/hadoop-${HADOOP_VERSION} $HADOOP_HOME && \
    rm /tmp/hadoop-${HADOOP_VERSION}.tar.gz

# Copy configuration files
COPY config/* $HADOOP_HOME/etc/hadoop/

RUN mkdir $HADOOP_HOME/logs
RUN mkdir -p /datos/datanode
RUN mkdir -p /datos/namenode
RUN chown -R hadoop:hadoop /datos ${HADOOP_HOME}

# Switch to hadoop user
USER hadoop
# Format HDFS
RUN $HADOOP_HOME/bin/hdfs namenode -format


USER root

# Expose ports
EXPOSE 9870 8088 9000 8042 22

# Copy the start script
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

# Switch to hadoop user
USER hadoop

# Set entry point
CMD ["/startup.sh"]
