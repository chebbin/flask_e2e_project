from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')


df = pd.read_csv('/home/chevi_ebbin/flask_e2e_project/data/New_York_City_Leading_Causes_of_Death_20231206.csv')
@app.route('/data')
def data(data=df):
    data = data
    return render_template('data.html', data=data)

# @app.route('/chart')
# def chartpage():
#    df = pd.read_csv ('/home/chevi_ebbin/flask_e2e_project/data/New_York_City_Leading_Causes_of_Death_20231206.csv')
#    return render_template('chart.html', chart = df)



if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )