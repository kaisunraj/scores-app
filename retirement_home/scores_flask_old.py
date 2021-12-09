from flask import Flask, render_template, request
import recording_scores
import pandas as pd
import json
from pandas_dfs import event_dfs, to_pandas_df

app = Flask(__name__)

#print(recording_scores.scores_database)

@app.route('/')
def table():
    df = pd.DataFrame(recording_scores.scores_database)
    df['Total'] = df.sum(axis=1)
    df.sort_values(by=['Total'], inplace= True, ascending = False)
    df.index += 1
    html = df.to_html(classes='table table-striped text-center', justify='center')
    return render_template("home_page_top.html") + html + render_template("home_page_bottom.html")
    

@app.route('/workout1')
def workout1():
    try:
        df = to_pandas_df('event_1')
        html = df.to_html()
    except:
        html = '<h2>There are no scores for this event yet</h2>'
    return render_template("workout1.html") + '<br>' + html
    
@app.route('/workout2')
def workout2():
    try:
        df = to_pandas_df('event_2')
        html = df.to_html()
    except:
        html = '<h2>There are no scores for this event yet</h2>'
    return render_template("workout2.html") + '<br>' + html

@app.route('/workout3')
def workout3():
    try:
        df = to_pandas_df('event_3')
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
        recording_scores.data_input.append(dict(form_data))
        with open('data.json', 'a') as fp:
            json.dump(dict(form_data), fp)
            fp.write(',')
        return render_template('data.html',form_data = form_data)



if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
