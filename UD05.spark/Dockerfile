## De la imagen ya creada en local ud04
FROM ud04-imagen

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV WORK_DIR=/usr/local
ENV JAVA_HOME=/usr/local/openjdk-11
ENV HOSTNAME=hadoop-cluster
ENV HIVE_VERSION=2.3.9-bin
ENV HIVE_HOME=/usr/local/hive
ENV HADOOP_HOME=/usr/local/hadoop
ENV HDFS_NAMENODE_USER=hadoop
ENV HDFS_DATANODE_USER=hadoop
ENV HDFS_SECONDARYNAMENODE_USER=hadoop
ENV YARN_RESOURCEMANAGER_USER=hadoop
ENV YARN_NODEMANAGER_USER=hadoop
ENV SPARK_VERSION=3.3.0
ENV SPARK_HOME=/usr/local/spark

WORKDIR ${WORK_DIR}

USER root

# Install SPARK
COPY ./spark-${SPARK_VERSION}-bin-without-hadoop.tgz /tmp/
RUN cd /tmp/ && tar -xzvf /tmp/spark-${SPARK_VERSION}-bin-without-hadoop.tgz
RUN mv /tmp/spark-${SPARK_VERSION}-bin-without-hadoop $SPARK_HOME
RUN chown -R hadoop:hadoop $SPARK_HOME

# Add SPARK configuration
RUN echo "export PATH=$PATH:/usr/local/spark/bin:/usr/local/spark/sbin" >> /home/hadoop/.bashrc
RUN echo "export SPARK_DIST_CLASSPATH=$(hadoop classpath)" >> /home/hadoop/.bashrc
