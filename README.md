# dvc-for-mlops
Sample DVC project


Create Virtual Environment:
1. python3 -m venv [your virtual env name]
2. source [your virtual env name]/bin/activate


DVC
1. pip3 install dvc
2. dvc init
3. dvc remote add remote_storage ../data_folder(path of your data storage by dvc)
4. dvc add data/
5. dvc commit
6. dvc push

Any change in data will be tracked by dvc
1. dvc status
2. dvc commit
3. dvc push