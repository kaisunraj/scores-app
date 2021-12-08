from flask import Flask, render_template, request
import recording_scores
import pandas as pd
import json
import events

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

@app.route('/scores')
def scores():
    with open(r'/Users/kaisunraj/scores_app/data.json', 'r') as f:
        data = f.readlines()
    try:
        data = data[0][:-1]
        df = pd.read_json(data, lines=True)
        df = df.pivot(index='Team',columns='Event',values='Score')
        df['Total'] = df.sum(axis=1)
        df.sort_values(by=['Total'], inplace= True, ascending = False)
        html = df.to_html(classes='table table-striped text-center', justify='center')
    except: 
        html = '''
        <h2> There are no scores yet </h2>
        '''
    return render_template("home_page_top.html") + html + render_template("home_page_bottom.html")
    

@app.route('/workout1')
def workout1():
    return render_template("workout1.html")
    
@app.route('/workout2')
def workout2():
    return render_template("workout2.html")

@app.route('/workout3')
def workout3():
    return render_template("workout3.html")

@app.route('/form')
def form():
    return render_template('form.html')

# @app.route('/data', methods = ['POST','GET'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         recording_scores.data_input.append(dict(form_data))
#         with open('data.json', 'a') as fp:
#             json.dump(dict(form_data), fp)
#             fp.write(',')
#         return render_template('data.html',form_data = form_data)


@app.route('/data', methods = ['POST','GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        if request.form['Event'].lower() not in events.event_names:
            events.event_names.append(request.form['Event'].lower())
        for i in events.event_names:
            if request.form['Event'].lower() == i:
                file_name = i.replace(' ','_') + '.json'
                with open(file_name, 'a') as fp:
                    json.dump(dict(form_data), fp)
                    fp.write(',')
            else:
                pass
        return render_template('data.html',form_data = form_data) + f'<p>{str(events.event_names)}</p>'


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

