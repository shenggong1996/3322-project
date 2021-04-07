# 3322-project
This is the repo for 3322 project.

First Sheng will post some example codes for reference.

CGCNN source code and documentation: https://github.com/txie-93/cgcnn

Proposal: 
https://docs.google.com/document/d/1OZc1JiTa3cgF5nNISI_90mE4I0GIULuRVza5pm4_Dg0/edit?usp=sharing


New: multitask learning of the ionic and electronic contributions

Note: here all the dataset and running codes are based on CGCNN style. You should convert them into multi-task style.

dataset: containing the split of training data. You should run multitask learning for each ratio with ionic and elec together.

ionic_test.csv and elec_test.csv: containing the test data.

strucutures: contain structures files of all materials.

1.0: my example working file for CGCNN. You should pay attention to the training.py for the working procedure of how I run CGCNN and follow the procedure to run multitask learning. 

Example of multi-task learning can be found at 
