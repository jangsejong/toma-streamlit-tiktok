import numpy as np
import streamlit as st
import pandas as pd
from subprocess import call
# import plotly.express as px
# from st_aggrid import AgGrid
import pickle
# import plotly.graph_objects as go
import time

# st.success('Done!')

st.set_page_config(page_title="TIKTOK Dashboard", layout='wide')
with st.spinner('Loading... TIKTOK_dashboard'):
    time.sleep(5)
st.sidebar.markdown("<div><img src='https://abcstudio.co/web/season2_skin/skin6/images/logo.png' width=200 /><h1 style='display:inline-block'></h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This is a dashboard that analyzes TikTok's big data.")

# title
st.title('TikTok Data')

 # Read the file and start the Viz
data1  = pd.read_csv('df_videos_users_focus_0329.csv')
# data2  = pd.read_csv('main\df_videos_users_focus_0330.csv')

data1['collection_time'] = (pd.to_datetime(data1['collection_time'],unit='ms'))
#Convert epoch to human-readable date and vice versa

df = pd.DataFrame(data=data1)
df = df[['id', 'nickname', 'followers', 'hearts','collection_time','collected_videos_count']]
# st.dataframe(df)


Collected_videos_count = st.sidebar.multiselect(
    'Please select the collect_videos_count. Multiple selections available:',
    options=df['collected_videos_count'].unique(),
    default=df['collected_videos_count'].unique()
)

# 라디오에 선택한 내용을 radio select변수에 담습니다
radio_select =st.sidebar.radio(
    "what is key column?",
    ['followers', 'hearts'],
    horizontal=True
    )

if radio_select == 'followers':
        st.sidebar.write('You selected followers.')
else:
        st.sidebar.write('You selected hearts.')
        

# Creates a slider that allows you to specify a range of values for the selected column.
slider_range = st.sidebar.slider(
    "choose range of key column",
     0.0, #시작 값 
     1000010.0, #끝 값  
    (0.5, 1000000.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
)

from datetime import datetime

# start_time = st.slider(
#     "When do you start?",
#     value=datetime(2023, 3, 21, 12, 30),
#     format="MM/DD/YY - hh:mm")
# st.write("Start time:", start_time)
# st.header(' ')
# start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
start_date = st.date_input("When do you start?", datetime(2023, 1, 19))
start_time = st.time_input("Start time", datetime(2023, 3, 1, 12, 30))

start_datetime = datetime.combine(start_date, start_time)
start_datetime_str = start_datetime.strftime('%Y-%m-%d %H:%M:%S')

df_selec = df.query(f"collected_videos_count == @Collected_videos_count & {radio_select} >= {slider_range[0]} & {radio_select} <= {slider_range[1]} & collection_time >= @start_datetime_str")

# print(slider_range) 
# df_selec = df.query(f"collected_videos_count == @Collected_videos_count & {radio_select} >= {slider_range[0]} & {radio_select} <= {slider_range[1]}" )
# df_selec = df.query(f"collected_videos_count == @Collected_videos_count & {radio_select} >= {slider_range[0]} & {radio_select} <= {slider_range[1]} & collection_time == @start_time_str ")
st.dataframe(df_selec)

    # 방법 1 progress bar 
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.

  bar.progress(i + 1)
  time.sleep(0.01)
  latest_iteration.text(f'Completion rate {i+1}')
  # 0.01 초 마다 1씩증가
    # 성공문구 + 풍선이 날리는 특수효과 
st.sidebar.success("completed!")

# st.balloons()


