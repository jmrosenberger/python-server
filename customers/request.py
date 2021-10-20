import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "name": "Charisse Lambert",
        "email": "charisse@lambert.com",
        "id": 1,
    },
    {
        "name": "Madi Peper",
        "email": "madi@peper.com",
        "id": 2,
    },
    {
        "name": "Jenna Solis",
        "email": "jenna@solis.com",
        "id": 3,
    },
    {
        "id": 4,
        "name": "Ryan Tanay",
        "email": "ryan@tanay.com",
    },
    {
        "id": 5,
        "name": "Emma Beaton",
        "email": "emma@beaton.com",
    },
    {
        "id": 6,
        "name": "Dani Adkins",
        "email": "dani.adkins.com",
    },
    {
        "id": 7,
        "name": "Adam Oswalt",
        "email": "adam@oswalt.com",
    },
    {
        "id": 8,
        "name": "Fletcher Bangs",
        "email": "flangs@bangs.com",
    },
    {
        "id": 9,
        "name": "Angela Lee",
        "email": "lee@lee.com",
    },
    {
        "name": "mike mike",
        "email": "m@m.com",
        "id": 10
    },
    {
        "name": "Eric \"Macho Man\" Taylor",
        "email": "macho@man.com",
        "id": 11
    },
    {
        "name": "Joshua Rosenberger",
        "email": "joshua@rosenberger.com",
        "id": 12
    }
]


def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        # Initialize an empty list to hold all animal representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)



def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'], data['password'])

        return json.dumps(customer.__dict__)


def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
