from flask import Flask, render_template
from pandas_df import return_pandas_as_html
import recording_scores
import pandas as pd

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
    return render_template("workout1.html")
    
@app.route('/workout2')
def workout2():
    return render_template("workout2.html")

@app.route('/workout3')
def workout3():
    return render_template("workout3.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

