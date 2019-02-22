from app import db

class ZipCode(db.Model):
    __tablename__= 'zip_table'
    id = db.Column('id', db.Integer, primary_key=True)
    zip_code = db.Column('zip_code', db.Integer, unique=True)
    width = db.Column('width', db.Integer, unique=False)
    heigth = db.Column('heigth', db.Integer, unique=False)
    adress = db.Column('adress', db.String(300), unique=False)

    def __init__(self, zip_code, width, heigth, adress):
        self.zip_code = zip_code
        self.width = width
        self.heigth = heigth
        self.adress = adress