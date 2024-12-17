FROM debian:stable-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV WORK_DIR=/usr/local
ENV JAVA_HOME=/usr/local/openjdk-11
ENV HADOOP_VERSION=3.4.1
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV HOSTNAME=hadoop-cluster

WORKDIR ${WORK_DIR}

RUN mkdir -p ${WORK_DIR}
RUN mkdir -p ${JAVA_HOME}

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
# Install Java
COPY openjdk-11.0.1_linux-x64_bin.tar.gz /tmp/
RUN tar -zxvf /tmp/openjdk-11.0.1_linux-x64_bin.tar.gz -C ${JAVA_HOME} --strip-components=1


###################################################
# Install Hadoop
COPY hadoop-${HADOOP_VERSION}.tar.gz ${WORK_DIR}
RUN tar -xzvf ${WORK_DIR}/hadoop-${HADOOP_VERSION}.tar.gz && \
    mv ${WORK_DIR}/hadoop-${HADOOP_VERSION} ${HADOOP_HOME} && \
    rm ${WORK_DIR}/hadoop-${HADOOP_VERSION}.tar.gz

# Copy configuration files
COPY config/hadoop/* ${HADOOP_HOME}/etc/hadoop/

RUN mkdir -p ${HADOOP_HOME}/logs
RUN mkdir -p /datos/{datanode,namenode}
RUN chown -R hadoop:hadoop /datos ${HADOOP_HOME}

USER hadoop
RUN $HADOOP_HOME/bin/hdfs namenode -format

###################################################
# Startup system
# Expose ports
USER root
EXPOSE 9870 8088 9000 8042 22

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

USER hadoop

CMD ["/startup.sh"]
