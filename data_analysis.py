import pandas as pd
import numpy as np

column = 'Fwd Packets/s'
origin_file = pd.read_csv('cicddos2019_dataset.csv')

benign_file = pd.read_csv('preprocessed_data_Benign.csv')
attack_file = pd.read_csv('preprocessed_data_UDP_attack.csv')
benign_flow = benign_file[column]
attack_flow = attack_file[column]

print(np.var(benign_flow))
print(np.var(attack_flow))
