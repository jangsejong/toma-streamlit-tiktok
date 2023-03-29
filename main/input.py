import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st

DATA_PATH = 'C:\streamlit-tiktok\toma-streamlit-tiktok\toma-streamlit-tiktok\csv\bq-results-20230329-085959-1680080406863.csv'
tiktok_dataset = pd.read_csv(f'{DATA_PATH}train.csv')

df= pd.DataFrame(data=tiktok_dataset.data,columns= tiktok_dataset.feature_names)
# df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= tiktok_dataset.target 


species_dict = {0 :'collected_videos_count', 1 :'collection_time', 2 :'influencer_id',
                3 :'profile_pic_url_hd', 4 : 'id', 5 : 'nickname', 6 : 'followers', 7 : 'hearts', 8 : 'videos_count'} 

def mapp_species(x):
  return species_dict[x]


df['species'] = df['species'].apply(mapp_species)
print(df)