# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:10:06 2020

@author: Elena
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
wall=pd.read_csv(r'C:\Users\Elena\Desktop\wall_distance.csv')

plt.plot(wall.iloc[1], wall.iloc[2])

