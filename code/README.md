# This directory is about the code.
>Note: we must be able to compile and/or run the code. No BINARY files are within the code. External libraries should be automatically downloaded (e.g., via Maven, npm, pip, docker pull)

## Prerequisites

You need Python installed in your machine,
then run """pip install -r requirements.txt"""

## Run Cassandra

Run """docker pull cassandra""" to download the official Cassandra image

In the file """docker-compose.yaml""" change the volumes location in order to match with your local machine
"""
    volumes:
      - /home/clement/WKS/AALTO/BigData/assignment-1-784795/data/cassandra/node1
"""
"""/home/clement/WKS/AALTO/BigData""" have to be changed


Then run """docker-compose up -d""" to run the cassandra server in detached mode

## Initialize DataBase

"""python mysimbdp.py"""

## Clean data

In order to clean the data contained in the csv file downloads from the google dataset you have to launch :
"""python clean_csv.py"""
this script will create the file cleanGoogleplaystore.csv in data/cassandra if this file already exists, this step is not necessary

## Insert Data in DataBase

"""python mysimbdp_multi_threads.py""" will launch several concurrent scripts which will each insert all the data, contained in the cleanGoogleplaystore.csv file, into the database and will plot the insertion per time result.

The number of concurrent scripts launched can be changed in mysimbdp_multi_threads.py in the line  : """ nbProcess = 10 """

