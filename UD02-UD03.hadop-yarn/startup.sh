#!/bin/bash

# Iniciar el servicio SSH (requiere privilegios de root)
sudo service ssh start

# Set the hostname
#echo "127.0.0.1 hadoop-master" >> /etc/hosts
#echo "hadoop-master" > /etc/hostname

# Iniciar los servicios de Hadoop
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

# Mantener el contenedor en ejecución
tail -f /dev/null
