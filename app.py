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

# Header
st.header('TikTok Data Analysis')

# # Just to show how it actualy looks like:
# st.sidebar.slider('followers', 1, 100000, 100)
# st.sidebar.slider('hearts', 1, 100000, 100)
# st.sidebar.slider('shareCount', 0, 220100)
# st.sidebar.slider('video_duration', 4, 60, 4)


 # Read the file and start the Viz
data1  = pd.read_csv('main\df_videos_users_focus_0329.csv')
data2  = pd.read_csv('main\df_videos_users_focus_0330.csv')

def user_input_features():

    followers = st.sidebar.slider('Followers', 0, 10000, 5000)
    hearts = st.sidebar.slider('Hearts', 22, 100000, 5000)
#     shareCount = st.sidebar.slider('shareCount', 0, 220100, 1)
#     video_duration = st.sidebar.slider('video_duration', 4, 60, 4)
    data = {
        'ID': 'id',
        'Followers': 'followers',
        'Hearts': 'hearts',
        'Video_count': 'collected_videos_count'}
    features = pd.DataFrame(data, index=[0])
    return features
    
df = user_input_features()

st.subheader('User Inputs')
st.write(df)




    # Read the file and start the Viz
data  = pd.read_csv('main\df_videos_users_focus_0329.csv')
data['hearts'] = 1
data = data.groupby(["followers"])["hearts"].count().reset_index()
data = data.sort_values(by='hearts', ascending=False)[:15]

fig_2 = go.Figure(data=[go.Pie(
                            labels=data["followers"], 
                            values=data["hearts"], 
                            textinfo='label+percent',
                            insidetextorientation='radial'
                    )], 
                    layout={"colorway": ["#f72585","#b5179e",
                                        "#7209b7","#560bad",
                                        "#480ca8","#3a0ca3",
                                        "#3f37c9","#4361ee",
                                        "#4895ef","#4cc9f0"]})

st.plotly_chart(fig_2, use_container_width=True) 

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