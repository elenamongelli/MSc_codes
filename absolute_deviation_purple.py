### Monitor probes###
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#
def importing_deviation(path):
    middle= pd.read_csv(path + os.path.sep + "middle.csv")
    first_boulevard= pd.read_csv(path + os.path.sep + "neg.csv")
    second_boulevard= pd.read_csv(path + os.path.sep + "pos.csv")
    squares= pd.read_csv(path + os.path.sep + "squares.csv")
    
    #Import Velocity: Magnitude for 1st configuration:
    
    middle_1= pd.read_csv(r'C:\Users\Elena\Desktop\CFD configuration\9_new_configuration\Monitor_probes\middle.csv')
    first_boulevard_1= pd.read_csv(r'C:\Users\Elena\Desktop\CFD configuration\9_new_configuration\Monitor_probes\neg.csv')
    second_boulevard_1= pd.read_csv(r'C:\Users\Elena\Desktop\CFD configuration\9_new_configuration\Monitor_probes\pos.csv')
    squares_1= pd.read_csv(r'C:\Users\Elena\Desktop\CFD configuration\9_new_configuration\Monitor_probes\squares.csv')
   
    #Cleaning:
    
    middle = middle.query('Time > 800')
    first_boulevard =first_boulevard.query('Time > 800')
    second_boulevard = second_boulevard.query('Time > 800')
    squares = squares.query('Time > 800')
    
    middle_1 = middle_1.query('Time > 800')
    first_boulevard_1 =first_boulevard_1.query('Time > 800')
    second_boulevard_1 = second_boulevard_1.query('Time > 800')
    squares_1 = squares_1.query('Time > 800')
    
    # Averaging #
    
    middle_mean = []
    
    for index in range(1, len(middle.columns)):
        middle_mean.append((middle.iloc[:, index].mean()))
    
    first_boulevard_mean = []
    
    for index in range(1, len(first_boulevard.columns)):
        first_boulevard_mean.append((first_boulevard.iloc[:, index].mean()))
        
    second_boulevard_mean = []
    
    for index in range(1, len(second_boulevard.columns)):
        second_boulevard_mean.append((second_boulevard.iloc[:, index].mean()))
        
    squares_mean = []
    
    for index in range(1, len(squares.columns)):
        squares_mean.append((squares.iloc[:, index].mean()))
        
    middle_1_mean = []
    
    for index in range(1, len(middle_1.columns)):
        middle_1_mean.append((middle_1.iloc[:, index].mean()))
    
    first_boulevard_1_mean = []
    
    for index in range(1, len(first_boulevard_1.columns)):
        first_boulevard_1_mean.append((first_boulevard_1.iloc[:, index].mean()))
        
    second_boulevard_1_mean = []
    
    for index in range(1, len(second_boulevard_1.columns)):
        second_boulevard_1_mean.append((second_boulevard_1.iloc[:, index].mean()))
        
    squares_1_mean = []
    
    for index in range(1, len(squares_1.columns)):
        squares_1_mean.append((squares_1.iloc[:, index].mean()))
    
    for index in range(1, len(squares_1.columns)):
        squares_1_mean.append((squares_1.iloc[:, index].mean()))
    def deviation(lis1, lis2, indices):
        sub_lis1 = [lis1[k] for k in indices]
        sub_lis2 = [lis2[k] for k in indices]
        return [abs(i - j) for i,j in zip(sub_lis1, sub_lis2)]
        
    flow_development = deviation(middle_mean, middle_1_mean, [0, 1, 3, 5, 6, 8, 9, 10])
    first_boulevard = deviation(first_boulevard_mean, first_boulevard_1_mean, [0, 1, 2, 3, 4, 5, 6, 7])
    second_boulevard = deviation(second_boulevard_mean, second_boulevard_1_mean, [0, 1, 2, 3, 4, 5, 6])
    corridor = deviation(squares_mean, squares_1_mean, [14,12,11,9])
    courtyards = deviation(squares_mean, squares_1_mean,[1,2,3,4,16,14,0,5,6,8,7,10])
    corridor_1 = deviation(middle_mean, middle_1_mean, [2,4,7])
    
    return flow_development, first_boulevard, second_boulevard, corridor, courtyards, corridor_1, middle_1_mean, first_boulevard_1_mean, second_boulevard_1_mean, squares_1_mean

length = 11

path_index = [str(i) for i in range(1,12)]

markers = ['$B1$', '$B2$', '$C1$', '$C2$', '$1$', '$2$', '$3$', '$4$', '$5$', '$6$', '$7$']
plt.style.use('classic')
fig = plt.figure(1, figsize=(10, 12))
ax = fig.gca()

for i in range(0, length):
    flow_development, first_boulevard, second_boulevard, corridor, courtyards, corridor_1, middle_1_mean, first_boulevard_1_mean, second_boulevard_1_mean, squares_1_mean = importing_deviation(r"C:" + os.path.sep + "Users" + os.path.sep + "Elena" + os.path.sep + "Desktop" + os.path.sep + "CFD configuration" + os.path.sep + path_index[i] + "_configuration" + os.path.sep + "Monitor_probes")


    plt.scatter(list(range(1, 5)), corridor, s=280, label="Corridors",  marker=markers[i], color= "tab:purple" )
    plt.scatter(list(range(5, 8)), corridor_1, s=280, marker=markers[i], color= "tab:purple" )
#    plt.scatter(list(range(1, 9)), flow_development, s=140, label="Flow development", marker=markers[i], color= "lime")
#    plt.scatter(list(range(9, 17)), first_boulevard, s=140, label="First boulevard", marker=markers[i], color="green" )
#    plt.scatter(list(range(17, 24)), second_boulevard, s=140, label="Second boulevard", marker=markers[i], color= "lightgreen")
#    plt.scatter(list(range(24, 36)), courtyards, s=140, label="Courtyards", marker=markers[i], color="lime" )
#    plt.scatter(list(range(36, 40)), corridor, s=140, label="Corridors",  marker=markers[i], color= "yellowgreen")
#    plt.scatter(list(range(40, 43)), corridor_1, s=140, marker=markers[i], color= "yellowgreen" )

flow_development_1 = [middle_1_mean[i] for i in [0, 1, 3, 5, 6, 8, 9, 10]]
courtyards_1 = [squares_1_mean[i] for i in [1,2,3,4,16,14,0,5,6,8,7,10]]
corridor_b = [squares_1_mean[i] for i in [14,12,11,9]]
corridor_b_1 = [middle_1_mean[i] for i in [2,4,7]]

plt.scatter(list(range(1, 5)), corridor_b, s=1000, label="RC Corridors", color="black",  marker="_", linewidth=3 )
plt.scatter(list(range(5, 8)), corridor_b_1, s=1000, color = "black" ,  marker="_", linewidth=3)         

plt.xticks(np.arange(1, 8, step=1), fontsize=18)
plt.yticks(np.arange(0, 7, step=1), fontsize=18)

ax.set_xticks(np.arange(1, 8, 1))
ax.set_yticks(np.arange(0, 7, 1))
ax.set_xticklabels(list(range(1,8)))

plt.ylim(bottom=0)
plt.xlim(left=0, right=8)

plt.grid(linestyle='dotted', linewidth=1)
# Bigger current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 2, box.height])

# Put a legend to the right of the current axis
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#Axis names
plt.ylabel('Absolute deviation [m/s]/ Velocity magnitude RC [m/s]', fontsize=18)
plt.xlabel('Monitor probes')
plt.title("Deviation")

plt.savefig('absolute_deviation_corridors.png', bbox_inches='tight', dpi=500)
                                                                                                                               