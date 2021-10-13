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
    return CUSTOMERS


# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

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
