EMPLOYEES = [
    {
      "name": "kyle",
      "locationId": 1,
      "animalId": 2,
      "id": 1
    },
    {
      "name": "silas",
      "locationId": 2,
      "animalId": 4,
      "id": 2
    },
    {
      "name": "travis",
      "locationId": 1,
      "animalId": 2,
      "id": 3
    },
    {
      "name": "devin",
      "locationId": 2,
      "animalId": 3,
      "id": 4
    },
    {
      "name": "mario",
      "locationId": 1,
      "animalId": 6,
      "id": 5
    }
]


def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee