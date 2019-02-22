from flask import Flask, render_template, request, redirect
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_hw12.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import ZipCode

api_url=('https://maps.googleapis.com/maps/api/geocode/json?address={}&mode=json&key={}')
api_key = 'AIzaSyCDKSQdglP_kfxPsZsDfqXxO0T193LJZfs'


def query_api(code):
    try:
        data = requests.get(api_url.format(code, api_key)).json()
    except Exception as exc:
        data = None
    return data


@app.route('/', methods=['GET', 'POST'])
def base_form():
    if request.method == 'POST':
        zip = request.form.get('zip', '')
        if zip:
            full_inf = query_api(zip)
            width = full_inf['results'][0]['geometry']['location']['lat']
            heigth = full_inf['results'][0]['geometry']['location']['lng']
            adress = full_inf['results'][0]['formatted_address']
            zp = ZipCode(zip_code=zip, width=width, heigth=heigth, adress=adress)
            db.session.add(zp)
            db.session.commit()
        return redirect('/result')
    return render_template('index.html')

@app.route('/result')
def result():
    result = ZipCode.query.all()
    return render_template('result.html', full_res = result)



if __name__ == '__main__':
    app.debug = True
    app.run()
