import pandas as pd
import csv
from datetime import datetime

if __name__ == "__main__":
    with open('../data/cassandra/googleplaystore.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        col0 = []
        col1 = []
        col2 = []
        col3 = []
        col4 = []
        col5 = []
        col6 = []
        col7 = []
        col8 = []
        col9 = []
        col10 = []
        col11 = []
        col12 = []
        for row in csv_reader:
            if line_count > 0 and len(row)==13:
                rating = float(row[2])
                rating = str(rating)
                if row[3].endswith('.0M'):
                    rev = int(row[3][:-3])*(10**6)
                else:
                    rev = int(row[3])
                rev = str(rev)
                fr = (row[6]=='Free')
                if row[7].startswith('$'):
                    price = float(row[7][1:])
                else:
                    price = float(row[7])
                price = str(price)
                last_up = datetime.strptime(row[10], "%B %d, %Y").date()
                col0.append(row[0])
                col1.append(row[1])
                col2.append(rating)
                col3.append(rev)
                col4.append(row[4])
                col5.append(row[5])
                col6.append(fr)
                col7.append(price)
                col8.append(row[8])
                col9.append(row[9])
                col10.append(last_up)
                col11.append(row[11])
                col12.append(row[12])
            line_count += 1
        d = {'a':col0, 'b' : col1, 'c': col2, 'd': col3, 'e': col4, 'f': col5, 'g': col6, 'h': col7, 'i': col8, 'j': col9, 'k': col10, 'l': col11, 'm': col12}
        df = pd.DataFrame(data=d)
        df.to_csv(r'../data/cassandra/cleanGoogleplaystore.csv', index = None)
