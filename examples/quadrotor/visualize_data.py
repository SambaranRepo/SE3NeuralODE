import sys, os, pickle
import matplotlib.pyplot as plt
import numpy as np
from data_collection import to_pickle, from_pickle
PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
THIS_DIR = PARENT_DIR + '/data'

data = from_pickle(f"{THIS_DIR}/jackal-dataset.pkl")
print(f"dataset shape : {data['x'].shape}")

data['x'] = data['x'].reshape(data['x'].shape[0], -1, data['x'].shape[-1])
print(f"new dataset shape : {data['x'].shape}")

for it in range(data['x'].shape[0]):
    temp = data['x'][it]
    # print("x : ")
    # print(temp[:,0])
    # print("y : ")
    # print(temp[:,1])
    fig,axs = plt.subplots(3,1,figsize=(15,8))
    fig.tight_layout()
    axs[0].scatter(temp[:,0], temp[:,1])
    axs[1].scatter(temp[:,12], temp[:,13])
    axs[2].scatter(temp[:,15], temp[:,16])
    plt.show(block = True)