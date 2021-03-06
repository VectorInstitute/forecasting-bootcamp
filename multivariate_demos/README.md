# Multivariate Forecasting Demo Notebooks

This directory contains a number of Jupyter notebooks designed to help you experiment with methods for Multivariate Time Series Forecasting. Multivariate Time Series Forecasting involves predicting the future values of a set of related time series given historical observations. These related time series may have temporal correlation that can be leveraged to collectively enhancy the accuracy of each forecast. Two recent methods that have performormed strongly in the multivariate forecast setting are NBEATS [NBEATS](https://arxiv.org/abs/1905.10437) and [DeepAR](https://arxiv.org/abs/1704.04110). We will be exploring each of these methods in this series of demos. 

## Running on Cluster 
The demos in this directory are easily run on the Vector cluster. First, download the provided datasets locally from [Google Drive Link](https://drive.google.com/drive/folders/1X-CgvkQKpatdPPrAYnWaeGmhA-daLJGr?usp=sharing) and extract the electricity dataset folder. Using JupyterHub (or sftp/rsync), upload the electricity dataset to the cluster in the `forecasting-bootcamp/datasets` folder of your home directory. fOpen the notebook you wish to run by navigating to the file in JupyterHub and selecting it. Once the notebook is open select `forecasting` in the *Change Kernel* dropdown under the **Kernel** tab. Finally, select *Restart and Run All* under **Kernel Tab** to run the entire notebook. 

## Demos

### DeepAR
DeepAR, a recently proposed probabilistic forecasting method, is applied to forecast hourly energy consumption accross a set of households. First, the demo outlines how to load the data and split it into train, validation and test sets. An autoformer model is subsequently initialized with an appropriate set of hyperparmeters given the dataset. The model is trained using the training data and evaluated at regular intervals using the validation data. Once the model is finished training, the model is evaluated on the test set and the predicitons are visualized. 

### NBEATS
NBEATS, a recently proposed interpretable forecasting method, is applied to forecast hourly energy consumption accross a set of households. First, the demo outlines how to load the data and split it into train, validation and test sets. An autoformer model is subsequently initialized with an appropriate set of hyperparmeters given the dataset. The model is trained using the training data and evaluated at regular intervals using the validation data. Once the model is finished training, the model is evaluated on the test set and the predicitons are visualized. 




