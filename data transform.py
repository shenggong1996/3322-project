import csv, os, json, math, sys
import numpy as np
from shutil import copyfile
Filepath_ionic='/Users/liurunze/PycharmProjects/hello/mt/dataset/ionic_training_0.01.csv'
Filepath_elect='/Users/liurunze/PycharmProjects/hello/mt/dataset/elec_training_0.01.csv'
Filepath_transf_training= "/Users/liurunze/PycharmProjects/hello/multitask learning/data/split 0.01/training_0.01.csv"
Filepath_map_hash_real = "/Users/liurunze/PycharmProjects/hello/multitask learning/data/split 0.01/material_id_hash_0.01.csv"

materials_id_list = []
material_hash_id_list=[]
elct_list=[]
ionc_list=[]
with open(Filepath_ionic, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        materials_id_list.append(str(row[0]))
        ionc_list.append(row[1])
with open(Filepath_elect, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        elct_list.append(row[1])
materials_id_list=np.array(materials_id_list)
ionc_list=np.array(ionc_list)
elct_list=np.array(elct_list)

for i in range(materials_id_list.shape[0]):
    material_hash_id_list.append(i)
material_hash_id_list=np.array(material_hash_id_list)

# bi_prop_list=np.concatenate([material_hash_id_list.reshape(-1,1),ionc_list.reshape(-1,1),elct_list.reshape(-1,1)],axis=1)
# with open(Filepath_transf_training, 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(bi_prop_list)
#
# map_hash_real=np.concatenate([material_hash_id_list.reshape(-1,1),materials_id_list.reshape(-1,1)],axis=1)
# with open(Filepath_map_hash_real, 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(map_hash_real)


for i in range(materials_id_list.shape[0]):
    CIF_str='/Users/liurunze/PycharmProjects/hello/mt/structures/'+ materials_id_list[i]+'.cif'
    CIF_dis='/Users/liurunze/PycharmProjects/hello/multitask learning/data/split 0.01/'+ str(material_hash_id_list[i])+'.cif'
    copyfile(CIF_str,CIF_dis)