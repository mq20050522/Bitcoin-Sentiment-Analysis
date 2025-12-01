Welcome to our DS410 Project, below are steps for downloading the dataset into ROAR collab.

1. Launch a terminal session inside of Jupyter Notebook
2. run source activate ds410_f25 in your terminal window
3. run pip install kaggle
4. run pip install kagglehub
5. copy the pasted code below into a cell and run it

import kagglehub

# Download latest version
path = kagglehub.dataset_download("andreapenasmartinez/bitcoin-twitter-sentiment-dataset-20132023")

#print("Path to dataset files:", path)
