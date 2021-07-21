import plotly.express as px
import pandas as pd
from datetime import timedelta, time


def create_graph(df, filename):
    
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="mood", color="mood")
    fig.update_yaxes(autorange="reversed")
    fig.write_html(filename)


if __name__ == '__main__':
    df = pd.DataFrame([
        dict(Task="happy", Start=time(4, 23, 1), Finish=(time(4, 23, 1) + timedelta(minutes=1)), mood="happy"),
        dict(Task="bored", Start=time(4, 40, 1), Finish=time(4, 40, 1) + timedelta(minutes=1), mood="bored"),
        dict(Task="sad", Start=time(4, 3, 45), Finish=time(4, 3, 45) + timedelta(minutes=1), mood="sad"),
        dict(Task="happy", Start=time(4, 23, 1), Finish=time(4, 23, 1) + timedelta(minutes=1), mood="happy"),
    ])
    filename = 'testhistory.html'
    create_graph(df, filename)
