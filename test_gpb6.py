import requests
from datetime import datetime
import pandas as pd
from pydantic import BaseModel, validator
from typing import List, Any

now = datetime.now()
start_of_day = datetime(now.year, now.month, now.day)
start_of_day_timestamp = int(start_of_day.timestamp())
endpoint = f"https://api.gazprombank.ru/very/important/docs?documents_date={start_of_day_timestamp}"
response = requests.get(endpoint)
data = response.json()


class BankAPIResponse(BaseModel):
    Columns: List[str]
    Description: str
    RowCount: int
    Rows: List[List[Any]]

    @validator('Rows', each_item=True)
    def check_rows(cls, v, values):
        if 'Columns' in values and len(v) != len(values['Columns']):
            raise ValueError("Length of each row should be equal to the length of Columns")
        return v


validated_data = BankAPIResponse(**data)

df = pd.DataFrame(validated_data.Rows, columns=validated_data.Columns)

column_mapping = {
    "key1": "document_id",
    "key2": "document_dt",
    "key3": "document_name"
}
df.rename(columns=column_mapping, inplace=True)
df['document_id'] = df['document_id'].astype(int)
df['document_dt'] = pd.to_datetime(df['document_dt'])
df['document_name'] = df['document_name'].astype(str)

df['load_dt'] = pd.to_datetime('now')

print(df)
