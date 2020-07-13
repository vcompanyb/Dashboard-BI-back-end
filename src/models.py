from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Enterprise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CIF_number = db.Column(db.String(10), unique=True, nullable=True)
    name = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(120), nullable=True) #preguntar como encriptar contraseña a la hora de crearla
    address = db.Column(db.String(120),nullable=True)
    phone = db.Column(db.String(80),nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, unique=False, nullable=False)
    brand_id = db.relationship('Brand', backref='enterprise', lazy=True)

    # def __init__(self, CIF_number, name, password, address, phone, email, is_active):
    #     self.CIF_number = CIF_number
    #     self.name = name
    #     self.password = password
    #     self.address = address
    #     self.phone = phone
    #     self.email = email
    #     self.is_active = is_active

    # def __repr__(self):
    #     return '<Enterprise %r>' % self.name
    def save(self):
        db.session.add(self)
        db.session.commit
        return self

    def serialize(self):
        return {
            "id": self.id,
            "CIF_number": self.CIF_number,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "is_active": self.is_active,
            "brand_id": list(map(lambda x: x.serialize(), self.brand_id)),
            # linea nueva insertada debajo !
            # do not serialize the password, its a security breach
        }

class Brand(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(120), unique=True, nullable=True)
    logo= db.Column(db.String(120), nullable=True)
    enterprise_to_id = db.Column(db.Integer, db.ForeignKey('enterprise.id'), nullable=False)
    relation_integration = db.relationship('Integration', backref='brand', lazy=True)
    relation_mi_data = db.relationship('Mydata', backref='brand', lazy=True)

    # def __init__(self, name, logo):
    #     self.name = name
    #     self.logo = logo

    # def __ref__(self):
    #     return f'<Brand {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "logo": self.logo,
            "relation_integration": list(map(lambda x: x.serialize(), self.relation_integration)),
            "relation_mi_data": list(map(lambda x: x.serialize(), self.relation_mi_data)),
        }
    # def save(self):
    #     db.session.add(self)
    #     db.session.commit
    #     return self

class Integration(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    API_key= db.Column(db.String(120), nullable=True)
    # deleted = db.Column(db.Boolean(), default=False) #¿Esto está bien? hay que incluirlo en serialize y cómo
    platform_id = db.relationship('Platform', backref='integration', lazy=True)
    brand_to_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    
    # def __ref__(self):
    #     return f'<Integration {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "API_key": self.API_key,
            "platform_id": list(map(lambda x: x.serialize(), self.platform_id))
            # "deleted": self.deleted,
            # "relation_data": list(map(lambda x: x.serialize(), self.relation_data))
            # if not self.user.deleted else None
        }    

class Platform(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    relation_integration = db.Column(db.Integer, db.ForeignKey('integration.id'), nullable=False)

    # def __ref__(self):
    #     return f'<Platform {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # ¿hay que meter las relaciones?
        }  

class Mydata(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(250))
    brand_to_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    integration_to_id = db.Column(db.Integer, db.ForeignKey('integration.id'), nullable=False)

    def __ref__(self):
        return f'<Mydata {self.id}>'
    def serialize(self):
        return {
            "id": self.id,
            "detail": self.detail,
            # ¿hay que meter las relaciones?
        }
