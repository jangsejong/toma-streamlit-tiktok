import numpy as np
import streamlit as st
import pandas as pd
from subprocess import call
import plotly.express as px
from st_aggrid import AgGrid
import pickle
import plotly.graph_objects as go

st.set_page_config(layout='wide')
st.sidebar.markdown("<div><img src='https://abcstudio.co/web/season2_skin/skin6/images/logo.png' width=200 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div><img src='https://raw.githubusercontent.com/jangsejong/toma-streamlit-tiktok/main/main/logo.png?token=GHSAT0AAAAAACAHNK2UHWYHHWPXANWXWUIAZBFMTVA' width=100 /></div>", unsafe_allow_html=True)
st.sidebar.markdown("This is a dashboard that analyzes TikTok's big data.")

# title
st.title('TikTok Data Analysis')

#header
st.header(' ')


 # Read the file and start the Viz
data1  = pd.read_csv('main\df_videos_users_focus_0329.csv')
data2  = pd.read_csv('main\df_videos_users_focus_0330.csv')

import time
data1['collection_time'] = (pd.to_datetime(data1['collection_time'],unit='ms'))
#Convert epoch to human-readable date and vice versa

#collected_videos_count,collection_time,id,nickname,followers,hearts


df = pd.DataFrame(data=data1)
df = df[['id', 'nickname', 'followers', 'hearts','collection_time','collected_videos_count']]
st.dataframe(df)


# def user_input_features():

#     followers = st.sidebar.slider('Followers', 0, 10000, 5000)
#     hearts = st.sidebar.slider('Hearts', 22, 100000, 5000)
# #     shareCount = st.sidebar.slider('shareCount', 0, 220100, 1)
# #     video_duration = st.sidebar.slider('video_duration', 4, 60, 4)
#     data = {
#         'ID': 'id',
#         'Followers': 'followers',
#         'Hearts': 'hearts',
#         'Video_count': 'collected_videos_count'}
#     features = pd.DataFrame(data, index=[0])
#     return features
    
# df = user_input_features()

# st.subheader('User Inputs')
# st.write(df)

select_multi_species = st.sidebar.multiselect(
    'Please select the column you want to check. Multiple selections available',
    ['nickname', 'followers', 'hearts']

)

# 원래 dataframe으로 부터 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
tmp_df = df['nickname'].isin(select_multi_species)
# 선택한 칼럼들의 결과표를 나타냅니다.  
st.table(tmp_df)

# 라디오에 선택한 내용을 radio select변수에 담습니다
radio_select =st.sidebar.radio(
    "what is key column?",
    ['followers', 'hearts','collected_videos_count'],
    horizontal=True
    )
# 선택한 컬럼의 값의 범위를 지정할 수 있는 slider를 만듭니다. 
slider_range = st.sidebar.slider(
    "choose range of key column",
     0.0, #시작 값 
     10000.0, #끝 값  
    (500.5, 3000.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
)

# 필터 적용버튼 생성 
start_button = st.sidebar.button(
    "filter apply 📊 "#"버튼에 표시될 내용"
)

# button이 눌리는 경우 start_button의 값이 true로 바뀌게 된다.
# 이를 이용해서 if문으로 버튼이 눌렸을 때를 구현 
if start_button:
    tmp_df = df[df['followers'].isin(select_multi_species)]
    #slider input으로 받은 값에 해당하는 값을 기준으로 데이터를 필터링합니다.
    tmp_df= tmp_df[ (tmp_df[radio_select] >= slider_range[0]) & (tmp_df[radio_select] <= slider_range[1])]
    st.table(tmp_df)
    
    # 방법 1 progress bar 
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.05)
  # 0.05 초 마다 1씩증가
    # 성공문구 + 풍선이 날리는 특수효과 
st.sidebar.success("Filter Applied!")
st.balloons()

















#     # Read the file and start the Viz
# data  = pd.read_csv('main\df_videos_users_focus_0329.csv')
# data['hearts'] = 1
# data = data.groupby(["followers"])["hearts"].count().reset_index()
# data = data.sort_values(by='hearts', ascending=False)[:15]

# fig_2 = go.Figure(data=[go.Pie(
#                             labels=data["followers"], 
#                             values=data["hearts"], 
#                             textinfo='label+percent',
#                             insidetextorientation='radial'
#                     )], 
#                     layout={"colorway": ["#f72585","#b5179e",
#                                         "#7209b7","#560bad",
#                                         "#480ca8","#3a0ca3",
#                                         "#3f37c9","#4361ee",
#                                         "#4895ef","#4cc9f0"]})

# st.plotly_chart(fig_2, use_container_width=True) 

#     # Grid the page
# left_col, right_col = st.columns(2)

#     # Create a Pie Chart with all values
# fig_3 = px.scatter(data, x="hearts", y="followers", animation_frame="hearts", animation_group="followers",size='videoMeta.duration', color="authorMeta.verified", hover_name="shareCount") 
#     # st.plotly_chart(fig_3, use_container_width=True)
# left_col.plotly_chart(fig_3, use_container_width=True)

# fig_4 = px.scatter(data, x="hearts", y="followers", animation_frame="hearts", animation_group="followers",size='videoMeta.duration', color="authorMeta.verified")
# right_col.plotly_chart(fig_4, use_container_width=True)

#     # Show tabular dataframe in streamlit
# st.markdown('Tip: You can groupby or apply filter on the columns!')
# AgGrid(df)