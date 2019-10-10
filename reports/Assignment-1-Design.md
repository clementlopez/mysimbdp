# This your assignment design report

## 1. Design and explain interactions between main components in your architecture of mysimbdp

I kept the basic structure of the project. I created a server using Cassandra Apache under Docker for which I only created one node (in data/cassandra). I have chosen to use the Dataset of [Google Play Store Apps](https://www.kaggle.com/lava18/google-play-store-apps) for my server. I got the csv files from my Dataset that I put in data/cassandra. From this, I was able to build the structure of my database (Tables creation) whose code, to be executed once, is in code/mysimbdp.py . I realized that some data in Google's csv was corrupted, so I created a Python script to clean this data, so the new csv is in data/cassandra/cleanGoogleplaystore.csv . From there, the script mysimbdp_collect_data_csv.py (in /code) opens the csv and inserts the data into the Cassandra database and the script mysimbdp_multi_threads.py (in /code) runs mysimbdp_collect_data_csv.py several times in parallel.

## 2. Explain how many nodes are needed in the deployment of mysimbdp-coredms so that this component can work property (theoretically based on the selected technology )

I only use one node because considering the use of my Cassandra server I don't think it is necessary to use more nodes on a server like mine right now. Anyway, adding nodes is very easy with Cassandra, if we want to make the server more robust by using Replica (that duplicate data and make the server more reliable in case of corrupted data or node crashes) or make the server more available then we will have to use additional nodes.

## 3. Will you use VMs or containers for mysimbdp and explain the reasons for each component

I use a docker container rather than a virtual machine. It is a stylistic opposition between the totally isolated VM and therefore necessarily safer compared to a container, much lighter and therefore faster. I have focused on the speed and scalability of my platform, which is why I chose Docker.

## 4. Explain how would you scale mysimbdp to allow a lot of users using mysimbdp-dataingest to push data into mysimbdp

For the moment, my server is only used on a local network but when it is on a cloud platform then we will have to look at the question of use by a large number of clients. Locally, the only power I can have on the issue is by vertical scaling (by playing on the CPU and RAM I give) but on a cloud, we can also play on a horizontal scaling (the number of machines) which allows a greater potential. The best solution is therefore a combination of these two possibilities.

## 5. Explain your choice of industrial cloud infrastructure and/or mysimbdp-coredms provider, when you do not have enough infrastructural resources for provisioning mysimbdp

I chose Cassandra for several reasons:
- With the tutorial we were able to get, it was the technology on which I had the most experience.
- It's an open-source technology
- Cassandra is very fast to handle a large volume of data
- There is less latency due to the mechanics of hard disks because Cassandra always privileges sequential access to random access
- Cassandra allows you to have flexible data schemas

The main limitation I could find was the size of the columns, all the data for a key value, must fit on the disk of a single machine (which is not a problem for the data I use)
