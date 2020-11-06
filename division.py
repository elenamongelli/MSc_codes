import os.path
import pandas as pd
from tabulate import tabulate

table=[]

for i in range(1, 48):
    if os.path.exists(r"C:\Users\Elena\Desktop\CFD configuration\monitor_velocities\\" + str(i) + "_mag.csv"):
        velocities= pd.read_csv(r"C:\Users\Elena\Desktop\CFD configuration\monitor_velocities\\" + str(i) + "_mag.csv")
        velocities = velocities.query('Iteration > 9000')
        velocities_mean = []

        for index in range(1, len(velocities.columns)):
            velocities_mean.append((velocities.iloc[:, index].mean()))
        velocities_mean = velocities_mean[0:16]
            
        division = velocities_mean[3]/velocities_mean[15]
        table.append(division)

latex_table = [[i,e] for i, e in zip (range(0,len(table)),table)]
print(tabulate(latex_table, tablefmt="latex_raw"))

