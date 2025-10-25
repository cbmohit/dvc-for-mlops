import pandas as pd
import os


data = {
    'Name':['Alice','Bob','John','Raju'],
    'Age':[25,30,35,36],
    'City':['London','Paris','Delhi','Bombay']
}

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")


