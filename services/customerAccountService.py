from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from models.customerAccount import CustomerAccount
from circuitbreaker import circuit
from sqlalchemy import select
from utils.util import encode_token

def find_all():
    query = select(CustomerAccount).join(Customer).where(Customer.id == CustomerAccount.customer_id)
    customer_accounts = db.session.execute(query).scalars().all()
    return customer_accounts

def login_customer(username, password): 
    user = (db.session.execute(db.select(CustomerAccount).where(CustomerAccount.username == username, CustomerAccount.password == password)).scalar_one_or_none())
    role_names = [role.role_name for role in user.roles]
    if user:
        auth_token = encode_token(user.id, role_names)
        resp = {
            'status': 'success',
            'message': 'successfully logged in',
            'auth_token': auth_token
        }
        return resp
    else:
        return None