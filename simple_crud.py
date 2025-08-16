# Simple CRUD operations using a Python dictionary

# Initial data store
data_store = {}

# CREATE
def create_item(key, value):
    if key in data_store:
        print(f"Create: Key '{key}' already exists.")
    else:
        data_store[key] = value
        print(f"Create: Added '{key}': '{value}'")

# READ
def read_item(key):
    value = data_store.get(key)
    if value is not None:
        print(f"Read: '{key}' = '{value}'")
    else:
        print(f"Read: Key '{key}' not found.")

# UPDATE
def update_item(key, value):
    if key in data_store:
        data_store[key] = value
        print(f"Update: '{key}' updated to '{value}'")
    else:
        print(f"Update: Key '{key}' not found.")

# DELETE
def delete_item(key):
    if key in data_store:
        del data_store[key]
        print(f"Delete: '{key}' removed.")
    else:
        print(f"Delete: Key '{key}' not found.")

# Example usage for each operation
create_item('username', 'alice')      # Create
read_item('username')                 # Read
update_item('username', 'bob')        # Update
read_item('username')                 # Read after update
delete_item('username')               # Delete
read_item('username')                 # Read after delete