import pandas as pd
import streamlit as st
import seaborn as sns
import requests
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
from list import columns_list,headers,season_list,p_headers

st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

option = st.selectbox(
    'Season',
    season_list)

if st.button(label='generate') or st.session_state.load_state:
    st.session_state.load_state = True
    url = f'https://stats.nba.com/stats/leaguedashplayerstats?College&Conference&Country&DateFrom&DateTo&Division&DraftPick&DraftYear&GameScope&GameSegment&Height&LastNGames=0&LeagueID=00&Location&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience&PlayerPosition&PlusMinus=N&Rank=N&Season='+option+'&SeasonSegment&SeasonType=Regular%20Season&ShotClockRange&StarterBench&TeamID=0&VsConference&VsDivision&Weight'
    r=requests.get(url=url, headers=headers).json()
    player_info = r['resultSets'][0]['rowSet']
    df=pd.DataFrame(player_info,columns=columns_list)
    url_players='https://stats.nba.com/stats/playerindex?College&Country&DraftPick&DraftRound&DraftYear&Height&Historical=1&LeagueID=00&Season='+option+'&SeasonType=Regular%20Season&TeamID=0&Weight'
    t=requests.get(url=url_players, headers=headers).json()
    players = t['resultSets'][0]['rowSet']
    df_player=pd.DataFrame(players,columns=p_headers)

else:
    st.info(
    "Select Season")
    st.stop()

#show
fil1, fil2 = st.columns(2)
with fil1:
    teams = st.selectbox(
    'Teams',
    (df['TEAM_ABBREVIATION'].unique()))
  
with fil2:
    players = st.selectbox(
        'Name',
    (df['PLAYER_NAME'].loc[df['TEAM_ABBREVIATION'] == teams]))


show = df[df['PLAYER_NAME']==players]
det = df_player[df_player['PERSON_ID']==show['PLAYER_ID'].values[0]]
# st.dataframe(show,use_container_width=True)
col1, col2, col3,col4,col5 = st.columns(5)
with col1:
  wr = round((show["W"].values[0]/show["GP"].values[0])*100,2)
  st.metric(label="WIN RATE", value=str(wr)+'%')
with col2:
  st.metric(label="PPG", value=str(show["PTS"].values[0]))
with col3:
  fg_pct=round(show["FG_PCT"].values[0]*100,2)
  st.metric(label="FG PCT", value=str(fg_pct)+'%')
with col4:
  st.metric(label="FG3 PCT", value=str(round(show["FG3_PCT"].values[0]*100,2))+'%')
with col5:
  st.metric(label="FT PCT", value=str(round(show["FT_PCT"].values[0]*100,2))+'%')
  
   


gr1,gr2,gr3 = st.columns(3)

with gr1:
    st.title(str(show['PLAYER_NAME'].values[0]))
    image_url = 'https://cdn.nba.com/headshots/nba/latest/1040x760/'+str(show['PLAYER_ID'].values[0])+'.png'
    st.image(image_url,use_column_width=True)
    st.markdown(f'Age: '+str(round(show['AGE'].values[0])))
    st.markdown(f'Position: '+det['POSITION'].values[0])
    st.markdown(f'College: '+det['COLLEGE'].values[0])
    try:
        dy = int(det['DRAFT_YEAR'].values[0])
    except:
        dy='-'
    st.markdown(f'Draft Year: '+str(dy))
    st.markdown(f'Jersey Number: '+str(det['JERSEY_NUMBER'].values[0]))
    
with gr2:
    logo_url = 'https://cdn.nba.com/logos/nba/'+str(show['TEAM_ID'].values[0])+'/global/L/logo.svg'
    st.image(logo_url,use_column_width=True)
    st.header(det['TEAM_CITY'].values[0]+' '+det['TEAM_NAME'].values[0])
    st.subheader(f'Game Played: '+ str(show['GP'].values[0]))
    # st.subheader(f'Rank: '+str(show['RANK'].values[0]))
    st.markdown(f'Minutes/Game: '+str(show['MIN'].values[0])+' Minutes')
    st.markdown(f'Points/Game: '+str(show['PTS'].values[0]))
    # st.markdown(f'Efficiency/Game: '+str(show['EFF'].values[0]))

with gr3:
    team_names = det['TEAM_CITY'].values[0]+' '+det['TEAM_NAME'].values[0]
    data = [go.Scatterpolar(
    r = [show['FG3M'].values[0],show["TOV"].values[0],show['OREB'].values[0],show['DREB'].values[0],show['BLK'].values[0],show["AST"].values[0],show["STL"].values[0]],
    theta = ['FG3 MADE','TURN OVER','O.REB','D.REB','BLOCK','ASSIST','STEAL'],
    fill = 'toself',
        line =  dict(
                color = 'orange'
            )
    )]
    layout = go.Layout(
    polar = dict(
        radialaxis = dict(
        visible = True,
        range = [0, 10]
        )
    ),
    showlegend = False,
    title = "{} - {} stats distribution".format(players,team_names)
    )
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig, filename = "Player Stats",use_container_width=True)


