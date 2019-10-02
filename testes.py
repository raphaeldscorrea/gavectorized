# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:18:12 2019

@author: RAPHAEL
"""

import json
import numpy as np
import pandas as pd

# read file
with open('input_shalyn.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

teste = np.asarray(obj["setups"])
def max_value(i,j):
    return(max(teste[i][j]))

max_setup_values = np.array([max_value(a,b) for a in range(len(teste)) for b in range(len(teste))]).reshape(len(teste),len(teste))


input_data = pd.DataFrame(obj["data"])