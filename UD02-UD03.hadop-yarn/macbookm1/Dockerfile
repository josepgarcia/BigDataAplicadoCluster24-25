# Base image
FROM openjdk:11-jdk

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV HADOOP_VERSION=3.4.1
ENV HADOOP_HOME=/usr/local/hadoop
ENV JAVA_HOME=/usr/local/openjdk-11
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV HOSTNAME=hadoop-cluster

# Install necessary packages
RUN apt-get update && \
    apt-get install -y openssh-server wget rsync sudo vim nano

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

# Install Hadoop
COPY hadoop-${HADOOP_VERSION}.tar.gz /tmp/
RUN tar -xzvf /tmp/hadoop-${HADOOP_VERSION}.tar.gz -C /usr/local/ && \
    mv /usr/local/hadoop-${HADOOP_VERSION} $HADOOP_HOME && \
    rm /tmp/hadoop-${HADOOP_VERSION}.tar.gz && \
    chown -R hadoop:hadoop $HADOOP_HOME

# Configure Hadoop environment variables
RUN echo "export JAVA_HOME=/usr/local/openjdk-11" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh

# Copy configuration files
COPY config/* $HADOOP_HOME/etc/hadoop/
RUN chown -R hadoop:hadoop $HADOOP_HOME/etc/hadoop/

# Switch to hadoop user
USER hadoop

# Format HDFS
RUN $HADOOP_HOME/bin/hdfs namenode -format

# Expose ports
EXPOSE 9870 8088 9000 8042 22

# Switch back to root to copy the start script
USER root

# Copy the start script
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

# Switch to hadoop user
USER hadoop

# Set entry point
CMD ["/startup.sh"]
