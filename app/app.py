from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

db_ip = '34.31.55.125'
db_port = '3306'
db_username = 'root'
db_password = 'shlomit1'
db_name = 'chevi'

engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_ip}:{db_port}/{db_name}')

# df = pd.read_csv('/home/chevi_ebbin/flask_e2e_project/data/New_York_City_Leading_Causes_of_Death_20231206.csv')
df = pd.read_sql('SELECT * FROM leading_causes_of_death', engine)

df = df.sort_values(by=['Year', 'Sex', 'Race Ethnicity'], ascending=[False, True, True])

@app.route('/')
def index():
    return render_template('base.html')



@app.route('/data')
def data(data=df):
    data = data
    return render_template('data.html', data=data)

@app.route('/api/data')
def api_data(data=df):
    ## get year from query string
    variable = request.args.get('type_in_year')
    ## filter the dataframe
    data = data[data['Year'] == int(type_in_year)]
    data = data.head(10)
    return data.to_json(orient='records')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )