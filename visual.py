import plotly.express as px
import pandas as pd
from datetime import timedelta, datetime


def create_timeline(df, filename):
    hover_dict = {'Task': False,'time': True,
                  'Finish': False, 'mood': False,
                  'content': True
                 }
    fig = px.timeline(
      df, x_start="time", x_end="Finish", y="mood", color="mood",
      hover_name="mood", hover_data=hover_dict,
      color_discrete_sequence=px.colors.qualitative.Pastel1,
      title="recent history"
    )
    return fig
#     fig.update_yaxes(autorange="reversed")
#     fig.write_html(filename)


def create_pie(df, filename):
    hover_dict = {'num_logs': True,
                  'mood': True
                 }
    fig = px.pie(
      df, values="num_logs", names="mood",
      hover_name="mood", hover_data=hover_dict,
      color_discrete_sequence=px.colors.qualitative.Pastel1,
      title="overall history"
    )
    print("plotly express hovertemplate:", fig.data[0].hovertemplate)
    fig.update_traces(hovertemplate='<b>%{customdata[0][1]}</b> <br><br> number of logs: %{customdata[0][0]}')
    return fig

if __name__ == '__main__':
    time1 = datetime.now()
    time2 = time1 + timedelta(minutes=7)
    time3 = time1 - timedelta(minutes=-15)
    df = pd.DataFrame([
        dict(Task="happy",
             time=time1, Finish=(time1 + timedelta(minutes=1)), mood="happy", content="happy days"),
        dict(Task="bored",
             time=time2, Finish=time2 + timedelta(minutes=1), mood="bored", content="bored af"),
        dict(Task="sad",
             time=time3, Finish=time3 + timedelta(minutes=1), mood="sad", content="sad boi hours"),
        dict(Task="happy",
             time=time3, Finish=time3 + timedelta(minutes=1), mood="happy", content="YAY"),
    ])
    filename = 'testtestmoodhistorytl.html'
    fig = create_timeline(df, filename)
    fig.update_yaxes(autorange="reversed")
    fig.write_html(filename)
    
    df = pd.DataFrame([
        dict(num_logs=15, mood="happy"),
        dict(num_logs=7, mood="bored"),
        dict(num_logs=3, mood="sad")
    ])
    filename = 'testtestmoodhistorypie.html'
    fig = create_pie(df, filename)
    fig.write_html(filename)
