from flask import Flask, render_template, request
import pandas as pd
import json
from pandas_dfs import event_dfs_max, event_dfs_min, to_pandas_df_min, to_pandas_df_max

app = Flask(__name__)

@app.route('/')
def scores():
    try:
        event_1 = event_dfs_min('event_1')
        event_2 = event_dfs_max('event_2')
        event_3 = event_dfs_min('event_3')
        df = event_1[['Points']].merge(event_2[['Points']], on='Team').merge(event_3[['Points']], on='Team')
        df['Total Points'] = df.sum(axis=1)
        df['Rank'] = df['Total Points'].rank(method='dense', ascending=True)
        df.sort_values(by='Rank', ascending=True)
        df = df.rename(columns={'Points_x':'Event 1', 'Points_y':'Event 2', 'Points':'Event 1',})
        html = df.to_html(classes='table table-striped text-center', justify='center')
    except:
        try:
            event_1 = event_dfs_min('event_1')
            event_2 = event_dfs_max('event_2')
            df = event_1[['Points']].merge(event_2[['Points']], on='Team')
            df['Total Points'] = df.sum(axis=1)
            df['Rank'] = df['Total Points'].rank(method='dense', ascending=True)
            df.sort_values(by='Rank', ascending=True)
            df = df.rename(columns={'Points_x':'Event 1', 'Points_y':'Event 2', 'Points':'Event 1',})
            html = df.to_html(classes='table table-striped text-center', justify='center')
        except:
            try: 
                event_1 = event_dfs_min('event_1')
                df = event_1[['Points']]
                df['Total Points'] = df.sum(axis=1)
                df['Rank'] = df['Total Points'].rank(method='dense', ascending=True)
                df.sort_values(by='Rank', ascending=True)
                df = df.rename(columns={'Points_x':'Event 1', 'Points_y':'Event 2', 'Points':'Event 1',})
                html = df.to_html(classes='table table-striped text-center', justify='center')
            except: 
                html = '''
                <h2> There are no scores yet </h2>
                '''
    return render_template("home_page_top.html") + html + render_template("home_page_bottom.html")
    

@app.route('/workout1')
def workout1():
    try:
        df = to_pandas_df_min('event_1')
        html = df.to_html()
    except:
        html = '<h2>There are no scores for this event yet</h2>'
    return render_template("workout1.html") + '<br>' + html
    
@app.route('/workout2')
def workout2():
    try:
        df = to_pandas_df_max('event_2')
        html = df.to_html()
    except:
        html = '<h2>There are no scores for this event yet</h2>'
    return render_template("workout2.html") + '<br>' + html

@app.route('/workout3')
def workout3():
    try:
        df = to_pandas_df_min('event_3')
        html = df.to_html()
    except:
        html = '<h2>There are no scores for this event yet</h2>'
    return render_template("workout3.html") + html

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data', methods = ['POST','GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        with open('events_list.txt', 'r') as el:
            events_str = str(el.readlines()[0])[:-1]
            event_names = events_str.split(',')
        for i in event_names:
            if request.form['Event'].lower() == i.strip():
                file_name = i.replace(' ','_') + '.json'
                with open(file_name, 'a') as fp:
                    json.dump(dict(form_data), fp)
                    fp.write(',')
            else:
                pass
        return render_template('data.html',form_data = form_data)



if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

