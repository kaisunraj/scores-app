import recording_scores 
import pandas as pd

print(recording_scores.scores_database)

def return_pandas_as_html():
    df = pd.DataFrame(recording_scores.scores_database)
    df['Total'] = df.sum(axis=1)
    df.sort_values(by=['Total'], inplace= True, ascending = False)
    df.index += 1
    return df.to_html()

html = return_pandas_as_html()

# write html to a file
text_file = open("templates/dataframe.html", "w")
text_file.write(html)
text_file.close()