# API Documentation | Challenge: User service

> Building the backend of a User Service System using Python and Flask

## Setup

I assume Python 3.x or higher is installed. 

##Tech used

Built in:

    Python 3.x
    Flask 1.0.2
    macOS Mojave Version 10.14.5

##Features

This is the backend for a user information application, which is able to perform the following tasks:

* Create users (last and first name)
* Create (several) email address(es) or phone number(s) for a user
* Retrieve a user's information (last and first name, email addresses, phone numbers) by user ID or last name 
* Update user's phone numbers/mail addresses through their user ID and phone/mail address ID
* Delete users by ID thereby also deleting all their email addresses and phone numbers


##Getting it to run

Before you start, please create a virual environment in the project folder user\_profiles_challenge folder and activate it (example iOS):

    # create virutal environment
    $ python3 -m venv env
    
    # activate virutal env
    $ source env/bin/activate

In order to install all nececsary libraries please:
	
	pip install -r requirements.txt  

Now run the app by using the `FLASK_APP` environment variable:

	$ export FLASK_APP=run.py
	$ flask run
	
The app should now run on your local server. To test the different endpoints, please go to **http://127.0.0.1:5000/swagger/**

###Requirements for different endpoint

* `POST` `/users` creating a user by indicating last_name and first\_name, an ID will automatically be allocated
* `POST` `/users/<int:user_id>/email` adding an email address to a user by using the user's id as an argument and the mail address as value **Restriction:** a user needs to first create a profile with his first and lats name
* `POST` `/users/<int:user_id>/phone` adding a phone number to a user by using the user's id as an argument and the phone number as value **Restriction:** a user needs to first create a profile with his first and lats name
* `GET` `/users` no arguments or values needed
* `GET` `/users/<int:user_id>` using a user's ID as an argument to retrieve her profile
* `GET` `/users/<string:user_name>` using a user's last name as an argument to retrieve her profile
* `PUT` `/users/<int:user_id>/email/<int:mail_id>` using a user's ID to update an email address. **Restriction:** the ID of the mail address must be know to update the address
* `PUT` `/users/<int:user_id>/phone/<int:phone_id>` using a user's ID to update a phone number. **Restriction:** the ID of the phone number must be know to update the number
* `DELETE` `/users/<int:user_id>` using a user's ID to delete all her information including her mail and phone data


##Documentation

For the purpose of documenting and testing the app I used swagger. The json-swagger code can be found in the static folder of the project.



## Limitations

It would be great if the user could add an email address and phone number when s/he creates the profile. For that purpose the mail and number functionality would be to be integrated.