import csv
import uuid
from datetime import datetime
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import argparse
import pandas as pd

def parse_arguments():
    parser = argparse.ArgumentParser(description='Init authentication')
    parser.add_argument('--user', type=str, help='You must fill in a String', default='cassandra')
    parser.add_argument('--password', type=str, help='You must fill in a String',  default='cassandra')
    parser.add_argument('--port', type=int, help='You must fill in a Int',  default=9042)
    parser.add_argument('--adress', type=str, help='You must fill in a Int',  default='0.0.0.0')
    return parser.parse_args()

def fill_database(session):
    #df = pd.read_csv('../data/cassandra/cleanGoogleplaystore.csv', dtype)
    with open('../data/cassandra/cleanGoogleplaystore.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                rating = float(row[2])
                rev = int(row[3])
                fr = bool(row[6])
                price = float(row[7])
                #last_up = datetime.strptime(row[10], "%B %d, %Y").date()
                session.execute("""
                INSERT INTO Application (id, name, category, rating, reviews, size, installs, free, price_dollar, content_rating, genres, last_update, current_ver, android_ver)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (uuid.uuid1(), row[0], row[1], rating, rev,
                row[4], row[5], fr, price, row[8],
                row[9], row[10], row[11], row[12])
                )
            line_count += 1





if __name__ == "__main__":
    args = parse_arguments()
    #Connect cluster
    auth_provider = PlainTextAuthProvider(username=args.user, password=args.password)
    cluster = Cluster([args.adress], auth_provider=auth_provider, port=args.port)
    session = cluster.connect()

    #Enter in the keyspace
    session.execute("USE MyKeyspace;")

    fill_database(session)

    #Close cluster
    cluster.shutdown()