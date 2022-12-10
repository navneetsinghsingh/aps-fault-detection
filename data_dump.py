import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/nuerolabDB")
Data_File_PATH="/config/workspace/aps_failure_training_set1.csv"
Database_Name="aps"
Collection_Name="sensor"
 
 
if __name__ == "_main_":
    df =pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:{df.shape}")  
    # convert dataframe to json so that we can dump these record in mango db
    df.reset_index(drop=True,inplace=True)
    json_record =json.loads(df.T.to_json().values())
    print(json_record[0])
    # insert converted json record to mango db
    client[Database_Name][Collection_Name].insert_many(Json_record)