
# created by rvcgeeks <github.com/rvcgeeks> (linkedin.com/in/rvchavadekar) @ Pune, India

from django.shortcuts import render, redirect
import pandas as pd

time_series_df = pd.read_csv("case_time_series.csv", header = None)
state_wise_df = pd.read_csv("state_wise.csv", header = None)

def make_series(x_values, y_values):
    
    var = '['
    for x, y in zip(x_values, y_values):
        var += '{x:\'' + str(x) + '\', y:' + str(y) + '},'
    var += ']'
    return var


def render_all_charts(request):
    
    try:
        request.session['id']
    except KeyError:
        return redirect('/success') # the success methods will bump to login after a KeyError again
    
    confirmed = make_series(time_series_df[1][1:], time_series_df[3][1:])
    recovered = make_series(time_series_df[1][1:], time_series_df[5][1:])
    reduced = make_series(time_series_df[1][1:], time_series_df[7][1:])
    
    states, statewise_confirmed, statewise_recovered, statewise_reduced = [], [], [], []
    for i, c, r, d in zip(state_wise_df[0][2:], state_wise_df[1][2:], state_wise_df[2][2:], state_wise_df[3][2:]):
        states.append(i); statewise_confirmed.append(c); statewise_recovered.append(r); statewise_reduced.append(d)
        
    latest_confirmed = time_series_df[3].iloc[-1]
    latest_recovered = time_series_df[5].iloc[-1]
    latest_reduced = time_series_df[7].iloc[-1]
    
    table_data = []
    for s, c, r, d, a, u in zip(state_wise_df[0][1:], state_wise_df[1][1:], state_wise_df[2][1:], state_wise_df[3][1:], state_wise_df[4][1:], state_wise_df[5][1:]):
        table_data.append([s, c, r, d, a, u])
    
    return render(request, 'mycharts.html', {
        'confirmed' : confirmed,
        'recovered' : recovered,
        'reduced' : reduced,
        'states' : states,
        'statewise_confirmed' : statewise_confirmed,
        'statewise_recovered' : statewise_recovered,
        'statewise_reduced' : statewise_reduced,
        'pie_data': [latest_confirmed, latest_recovered, latest_reduced],
        'table_data': table_data,
    })
