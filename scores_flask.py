from flask import Flask, request, render_template, session, redirect
import recording_scores
import pandas as pd

app = Flask(__name__)

print(recording_scores.scores_database)

@app.route('/')
def table():
    df = pd.DataFrame(recording_scores.scores_database)
    df['Total'] = df.sum(axis=1)
    df.sort_values(by=['Total'], inplace= True, ascending = False)
    df.index += 1
    return df.to_html()

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)


