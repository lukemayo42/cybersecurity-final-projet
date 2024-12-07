# Cybersecurity Final Project Lucas Mayo
## Description
The first screen you will see is the login screen.  If a user does not have an account, press the register button and they will go to a register screen. This screen will prompt the user to enter a username, password, and confirm password. The passwords must match in order to register. The passwords must also meet the follwing requirements:
- length in between 8 and 25 characters
- must contain at least:
    - 1 special character
    - 1 uppercase letter
    - 1 lowercase letter
    - 1 number

If the user does not meet the requirements an error message will appear. A strong password generator exists to give strong passwords to users. If the user meets all the requirements they will be returned to the login screen with a message saying that they have successfully registered as a new user. They will have the `technical` access level. 

The user then can login. the user has 3 attempts to log in before they will be locked out. If the user enters corredct credentials, they will be given access to the Departments page. The user will only be able to see what departments they have access to based on their access level. If a user accesses a department, it will bring them to a page saying that they ahve accessed that department and can return to the directory. 


## Database Description and Decurity

The database is secured against SQL Injection by using paramterized queries. Passwords are secured within the database by hashing passwords and salting them, with a salt length of 40. 

## Testing Instructions

You can test the program by following the setup instructions below, and inputing both valid and invalid data to the forms. Running setup.py will create an empty databse called `users.db`. You will need to register a user in order to login. I have provided a test database called `testing.db`. This database contains users with all three access levels. `technical`, `business`, and `admin`, to test the other roles in the system. To use this database simply change the `DATABASE` constant in `setup.p`y from `'users.db'` to `'testing.db'`. Do not rerun `setup.py`.
These users have the following login information in `testing.db`:   
1. username: ljmayo
    - password: ILikeSkiing42!
    - access level: technical
2. username: TheBoss
    - password: TheBossRocks74!
    - access level: admin
3. username: FinanceGuy
    - password: wal|str33tw0lF
    - access level: business

If you would like more then three login attempts, you can change the constant  `LOGIN_LIMIT` at the top of  `app.py` to a higher number than three. 

## Setup Instructions
in the terminal run: 
```
virtualenv venv
```
then(windows):
```
.\venv\Scripts\activate
```
install flask:
```
pip install flask
```
setup the database:
``` 
python setup.py
```
run the flask app:
```
python app.py
```