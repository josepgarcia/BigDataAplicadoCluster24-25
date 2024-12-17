# Creación de cluster con Sqoop + Hive

- Necesitamos un contenedor con mysql para poder importar y exportar datos con sqoop

## Descargar hive

https://archive.apache.org/dist/hive/hive-2.3.9/apache-hive-2.3.9-bin.tar.gz

## Crear imagen

docker build -t ud04-imagen .

## Contenedor

Mapeamos también el puerto ssh para poder acceder

docker run -it --name ud04-contenedor -p 9870:9870 -p 8088:8088 -p 9000:9000 -p 8042:8042 -p 2222:22 ud04-imagen

## Entramos

// También podemos entrar por ssh (puerto 2222)
docker exec -it ud04-contenedor /bin/bash

# Error hive al hacer un insert

Query ID = hadoop_20241217154708_680b984a-2d50-48b8-b28f-026baf90ee06
Total jobs = 3
Launching Job 1 out of 3
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1734449714523_0002, Tracking URL = http://1f8b6e9a549a:8088/proxy/application_1734449714523_0002/
Kill Command = /usr/local/hadoop/bin/hadoop job -kill job_1734449714523_0002
Hadoop job information for Stage-1: number of mappers: 0; number of reducers: 0
2024-12-17 15:47:14,774 Stage-1 map = 0%, reduce = 0%
Ended Job = job_1734449714523_0002 with errors
Error during job, obtaining debugging information...
FAILED: Execution Error, return code 2 from org.apache.hadoop.hive.ql.exec.mr.MapRedTask
MapReduce Jobs Launched:
Stage-Stage-1: HDFS Read: 0 HDFS Write: 0 FAIL
Total MapReduce CPU Time Spent: 0 msec
