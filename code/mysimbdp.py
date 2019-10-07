from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Init authentication')
    parser.add_argument('--user', type=str, help='You must fill in a String', default='cassandra')
    parser.add_argument('--password', type=str, help='You must fill in a String',  default='cassandra')
    parser.add_argument('--port', type=int, help='You must fill in a Int',  default=9042)
    parser.add_argument('--adress', type=str, help='You must fill in a Int',  default='0.0.0.0')
    return parser.parse_args()



if __name__ == "__main__":
    args = parse_arguments()
    #Connect cluster
    auth_provider = PlainTextAuthProvider(username=args.user, password=args.password)
    cluster = Cluster([args.adress], auth_provider=auth_provider, port=args.port)
    session = cluster.connect()

    #Create Keyspace
    session.execute("""CREATE KEYSPACE IF NOT EXISTS MyKeyspace
        WITH REPLICATION = {
            'class' : 'SimpleStrategy',
            'replication_factor' : 1
        };
    """)

    #Enter in the keyspace
    session.execute("USE MyKeyspace;")

    #Create ColumFamilies (Tables)
    session.execute("""
    CREATE TABLE Application
    (
        id UUID PRIMARY KEY,
        name text,
        category text,
        rating float,
        size int,
        install int,
        type text,
        price float,
        content_rating text, 
        genres text,
        last_update date,
        current_ver text,
        android_ver text
    );
    """)
    session.execute("""
    CREATE TABLE Review
    (
        id UUID PRIMARY KEY,
        app_name text,
        translated_review text,
        sentiment text,
        sentiment_polarity float,
        sentiment_subjectivity float
    );

    """)

    #Close cluster
    cluster.shutdown()

