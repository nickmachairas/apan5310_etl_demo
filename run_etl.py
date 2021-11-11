from app import db
from app.models import Customers


customer1 = Customers(
    first_name="John",
    last_name="Doe",
    email="jdoe@email.com",
    cell_phone="123-456-7890")

db.session.add(customer1)
db.session.commit()
