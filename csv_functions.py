# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:13:08 2021

@author: alexd
"""

import pandas as pd
import csv

def load(csv_file):
    """Loads 2D arrays"""
    columns = ['tiempo', 'valor']
    file = pd.read_csv(csv_file, delimiter=';', usecols = columns)
    file1 = file['tiempo'].tolist()
    file2 = file['valor'].tolist()
    return file1, file2

def save(csv_filename, time_signal, signal):
    
    pass


tiempo, senyal = load('t_5.csv')

f = open("t_4.csv", mode="a")
headers = ['tiempo','valor']
f.write((headers[0] + ";" + headers[1] + ";\n"))
for i in range(len(tiempo)):
    f.write(str(tiempo[i]))
    f.write(";")
    f.write(str(senyal[i]))
    f.write(";\n")
    
f.close()