from user_info import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    emails = db.relationship('Email', backref='user', cascade="all,delete", lazy=True)
    phone_numbers = db.relationship('PhoneNumber', backref='user', cascade="all,delete", lazy=True)

    def __repr__(self):
        return f"User(last_name='{self.last_name}', first_name='{self.first_name}')"
        
class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(20), unique=True, nullable=False)
    user_id_mail = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Email(mail='{self.mail}', owner='{self.user_id_mail}')"

class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(15), unique=True, nullable=False)
    user_id_phone = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"PhoneNumber(number='{self.number}', owner='{self.user_id_phone}')"
