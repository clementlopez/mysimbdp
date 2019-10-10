import csv
import uuid
from datetime import datetime
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import argparse
import pandas as pd
from timeit import default_timer as d_timer

def parse_arguments():
    parser = argparse.ArgumentParser(description='Init authentication')
    parser.add_argument('--user', type=str, help='You must fill in a String', default='cassandra')
    parser.add_argument('--password', type=str, help='You must fill in a String',  default='cassandra')
    parser.add_argument('--port', type=int, help='You must fill in a Int',  default=9042)
    parser.add_argument('--adress', type=str, help='You must fill in a String',  default='0.0.0.0')
    parser.add_argument('--id', type=str, help='You must fill in a Int',  default=0)
    return parser.parse_args()

def fill_database(session):
    with open('../data/cassandra/cleanGoogleplaystore.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        timer = [['0','0']]
        debut = d_timer()
        for row in csv_reader:
            if line_count > 0:
                rating = float(row[2])
                rev = int(row[3])
                fr = bool(row[6])
                price = float(row[7])
                session.execute("""
                INSERT INTO Application (id, name, category, rating, reviews, size, installs, free, price_dollar, content_rating, genres, last_update, current_ver, android_ver)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (uuid.uuid1(), row[0], row[1], rating, rev,
                row[4], row[5], fr, price, row[8],
                row[9], row[10], row[11], row[12])
                )
            line_count += 1
            if line_count%10==0:
                timer.append([str(line_count),str(d_timer()-debut)])
    return timer





if __name__ == "__main__":
    args = parse_arguments()
    #Connect cluster
    auth_provider = PlainTextAuthProvider(username=args.user, password=args.password)
    cluster = Cluster([args.adress], auth_provider=auth_provider, port=args.port)
    session = cluster.connect()

    #Enter in the keyspace
    session.execute("USE MyKeyspace;")

    result = fill_database(session)

    headers = ['NbValues','Time']

    f = open('../data/cassandra/Result'+args.id+'.csv', 'w')
    headersLine = ",".join(headers) + "\n"
    f.write(headersLine)
    for val in result:
        line = ",".join(val) + "\n"
        f.write(line)

    f.close()

    #Close cluster
    cluster.shutdown()