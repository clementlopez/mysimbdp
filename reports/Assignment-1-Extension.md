# This your assignment extension report

## 1. Assume that each of your tenants/users will need a dedicated mysimbdp-coredms. Design the data schema of service information for mysimbdp-coredms that can be published into an existing registry (like ZooKeeper, consul or etcd) so that you can find information aboutwhich mysimbdp-coredms for which tenants/users.

We assume that each tenant/user will need a dedicated mysimbdp-coredms, a reason could be performance or availability (we saw at the question 2.5 that failures can appear, an other reason could be an upgrade of the DataBase, etc...).

If we dedicate one mysimbdp-coredms to each user, we will need extra infos about the user. The informations of each data that can be published into an existing registry: we will have to modelize how each user data is mapped to storage. 

What we want is to achieve customer isolation. In the key/value list that we will need, the tenant identifier could be something like email adress (or user uuid) + node id (something about the user + something about the platform, this is very important !). Or an other possibility could be to use a schema-bases multitenancy : each customer will use its own database, so in this case the tenant identifier is very easy to find.

What I saw about ZooKeeper is that an application creates a znode which is a file that persists in memory on the server. The znode can be updated by any node in the cluster and each node can register in order to be notified of evry change in that znode. 


## 2. Assume that the service information about mysimbdp-coredms for a tenant/users is in a file, write a program that can be used to publish the service information of mysimbdp- coredms into either etcd, consul or Zookeeper

## 3. Explain how you would change the implementation of mysimbdp-dataingest(in Part 2) to integrate a service discovery feature (no implementation is required)

We can be in 2 different cases :

### As in question 3.1, each tenant/user has a dedicated mysimbdp-coredms

In this case we will run a script that verify if the user already have a session, if yes the session will be re-used, if not we will create a new one and save a record in ZooKeeper register. The script will return the IP address (of the session) that dataingest will use to connect.

### Case in which coredms are shared

We will run a script that verify how no-empty are the nodes and the script will return the IP of the emptiest node (or create a new dedicated node).

## 4. Explain APIs you would design for mysimbdp-daas so that any other developer who wants to implement mysimbdp-dataingest can write his/her own ingestion program to write the data into mysimbdp-coredms by calling mysimbdp-daas

mysimdbp-daas will be an API that will use mysimbdp-dataingest in backend in order to propose functions easy to use to do insertion/programs/applications/etc...

As I code with Python, a Python API will be an option. An other option will be to implement a REST API could be useful to receive queries of data from a web site or an Android App.

Some examples of function of the API could be :
```
connect(<cluster_ip>)
insert_into(<table_name>,<data_in_csv>)
close_connect(<cluster_ip>)
```

## 5. Assume that now only mysimbdp-daas can read and write data into mysimbdp-coredms, how would you change your mysimbdp-dataingest (in Part 2) to work with mysimbdp-daas

For now mysimbdp-dataingest is implemented to only load data from a csv file. In order to work with mysimbdp-daas, mysimbdp-dataingest will have to be able to work with the data that the users give to mysimbdp-daas.
The user will not always wanted to insert an entire csv file in the database, sometime he will only want to insert one line, sometime to change a value, etc...
So, mysimbdp-dataingest will have to be able to deal with python table for example, or python set, etc...
