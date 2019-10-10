from multiprocessing import Pool, TimeoutError, Process
import time
from timeit import default_timer as d_timer
import os
import matplotlib.pyplot as plt
import csv

def run_process(process):                                                             
    os.system('python {}'.format(process))

if __name__ == '__main__':
    #Multi-threads
    debut = d_timer()
    nbProcess = 10
    processes = []
    for i in range(nbProcess):
        processes.append('mysimbdp_collect_data_csv.py --id '+str(i))
    pool = Pool(processes=nbProcess)
    pool.map(run_process, processes)

    #data display
    for i in range(nbProcess):
        with open('../data/cassandra/Result'+str(i)+'.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            timeCount = []
            numberInsert = []
            for row in csv_reader:
                if line_count > 0:
                    numberInsert.append(int(row[0]))
                    timeCount.append(float(row[1]))
                line_count+=1
            plt.plot(timeCount, numberInsert)
    plt.show()