from flask import request, jsonify, abort
#import json
from user_info.models import User, Email, PhoneNumber
from user_info import app, db
from user_info.schemas import UserSchema, EmailSchema, PhoneNumberSchema


# testing whether servers run, kind of landing page
@app.route('/')
def home_route():
    return 'This is a user information app!'

# create a user with last and first name, an ID is automatically 
# added and serves as a unique identifier
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json(force=True) # force=True will make sure this works even if a client does not specify application/json
    new_last_name = data['last_name']
    new_first_name = data['first_name']
   
    new_user = User(last_name=new_last_name, first_name=new_first_name)
    db.session.add(new_user)
    db.session.commit()
    user_schema = UserSchema() # use of marshmallow schemas to convert object  to and from native Python datatypes
    response = user_schema.dump(new_user)
    return jsonify(response)


# create an email address/phone number for a specific user
@app.route('/users/<int:user_id>/email', methods=['POST'])
def create_email(user_id):
    data = request.get_json(force=True)
    new_email = data['mail']

    user = User.query.get_or_404(user_id, "User does not exist. Please register first as a user.") # check if user exists, user profile needs to be create first
    add_email = Email(mail=new_email, user_id_mail=user_id)
    db.session.add(add_email)
    db.session.commit()
    email_schema = EmailSchema()
    response = email_schema.dump(add_email)
    return jsonify(response)

@app.route('/users/<int:user_id>/phone', methods=['POST'])
def create_number(user_id):
    data = request.get_json(force=True)
    new_phone = data['number']

    user = User.query.get_or_404(user_id, "User does not exist. Please register first as a user.")
    add_phone = PhoneNumber(number=new_phone, user_id_phone=user_id)
    db.session.add(add_phone)
    db.session.commit()
    phone_schema = PhoneNumberSchema()
    response = phone_schema.dump(add_phone)
    return jsonify(response)


# get all existing users
@app.route('/users', methods=['GET'])
def get_all_users():
    user_schema = UserSchema(many=True) 
    users = User.query.all()
    response = user_schema.dump(users)
    return jsonify(response)

# get specific user by user ID
@app.route('/users/<int:user_id>', methods=['GET'])
def info_specific_user_by_id(user_id):
    user = User.query.get_or_404(user_id)
    user_schema = UserSchema()   
    response = user_schema.dump(user)
    return jsonify(response)

# get specific user by last name
@app.route('/users/<string:user_name>', methods=['GET'])
def info_specific_user_by_last_name(user_name):
    user = User.query.filter(User.last_name == user_name).first()
    user_schema = UserSchema()   
    response = user_schema.dump(user)
    return jsonify(response)


# update a user's email address or phone number
@app.route('/users/<int:user_id>/email/<int:mail_id>', methods=['PUT']) 
def update_email(user_id, mail_id):
    data = request.get_json(force=True)
    new_mail_address = data['mail']
    unique_address = Email.query.filter(Email.mail==new_mail_address).first() # to avoid duplication of any phone number or email address
    if unique_address==None:
        user = User.query.filter(User.id==user_id).first() # checking if user exists by user ID
        right_address = Email.query.filter(Email.user_id_mail==mail_id).first() # checking if mail address belongs to this user
        if user and right_address:
            target_mail_address = Email.query.filter(Email.id==mail_id).first() # querying the right email address among the user's email addresses
            target_mail_address.mail = new_mail_address
            db.session.commit()  
            email_schema = EmailSchema()
            response = email_schema.dump(target_mail_address)
            return jsonify(response)
        else:
            return abort(400, description='User does not exist or email does not belong to you.')
    else:
        return abort(400, "Email address already exists.")


@app.route('/users/<int:user_id>/phone/<int:phone_id>', methods=['PUT']) 
def update_phone(user_id, phone_id):
    data = request.get_json(force=True)
    new_phone_number = data['number']
    user = User.query.filter(User.id==user_id).first()
    unique_number = PhoneNumber.query.filter(PhoneNumber.number==new_phone_number).first()
    if unique_number==None:
        user = User.query.filter(User.id==user_id).first()
        right_number = PhoneNumber.query.filter(PhoneNumber.user_id_phone==phone_id).first()
        if user and right_number:
            target_phone_number = PhoneNumber.query.filter(PhoneNumber.id==phone_id).first()
            target_phone_number.number = new_phone_number
            db.session.commit()
            phone_schema = PhoneNumberSchema()
            response = phone_schema.dump(target_phone_number)
            return jsonify(response)
        else:
            return abort(400, description='User does not exist or phone number does not belong to you.')
    else:
        abort(400, description="Phone number already exists.")

# delete user by ID address, email addresses annd phone numbers of this user ID will also be deleted
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id, "User does not exist!")
    db.session.delete(user)
    db.session.commit()
    return '<h1>We are sad that you are leaving us. Hope to see you soon again!</h1>', {'Content-Type': 'text/html'}
