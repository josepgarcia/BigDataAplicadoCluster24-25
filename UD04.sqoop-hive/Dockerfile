## De la imagen ya creada en local ud02
FROM ud02

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV WORK_DIR=/usr/local
#ENV JAVA_HOME=/opt/openjdk-11
ENV HOSTNAME=hadoop-cluster
ENV HIVE_VERSION=2.3.9-bin
ENV HIVE_HOME=/usr/local/hive
ENV HDFS_NAMENODE_USER=hadoop
ENV HDFS_DATANODE_USER=hadoop
ENV HDFS_SECONDARYNAMENODE_USER=hadoop
ENV YARN_RESOURCEMANAGER_USER=hadoop
ENV YARN_NODEMANAGER_USER=hadoop

WORKDIR ${WORK_DIR}

USER root

# Install HIVE
COPY ./software/apache-hive-${HIVE_VERSION}.tar.gz /tmp/
RUN tar -xzvf /tmp/apache-hive-${HIVE_VERSION}.tar.gz
RUN mv ${WORK_DIR}/apache-hive-${HIVE_VERSION} $HIVE_HOME

# Copy configuration files
COPY ./config/hive/* $HIVE_HOME/conf/
RUN chown -R hadoop:hadoop $HIVE_HOME
# New config
COPY ./config/.bashrc /home/hadoop/


###USER hadoop
# Dará error si ya existe
###RUN hdfs dfs -mkdir /tmp
# Como vamos a trabajar con el usuario hadoop
# damos permisos a /tmp para que no de problemas
###RUN hdfs dfs -chmod g+w /tmp
# Directorio donde trabaja Hive, no cambiar de nombre
###RUN hdfs dfs -mkdir -p /user/hive/warehouse
# Damos permisos para que Hive pueda trabajar aquí.
# Le daremos permisos al grupo hadoop, que es el que usaremos con Hive
###RUN hdfs dfs -chmod g+w /user/hive/warehouse

