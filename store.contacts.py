import json

# Initial contact information for 10 people
contacts = [
    {"name": "Alice Smith", "phone": "555-1234", "email": "alice@example.com"},
    {"name": "Bob Johnson", "phone": "555-5678", "email": "bob@example.com"},
    {"name": "Carol Williams", "phone": "555-8765", "email": "carol@example.com"},
    {"name": "David Brown", "phone": "555-4321", "email": "david@example.com"},
    {"name": "Eve Davis", "phone": "555-6789", "email": "eve@example.com"},
    {"name": "Frank Miller", "phone": "555-9876", "email": "frank@example.com"},
    {"name": "Grace Wilson", "phone": "555-3456", "email": "grace@example.com"},
    {"name": "Hank Moore", "phone": "555-6543", "email": "hank@example.com"},
    {"name": "Ivy Taylor", "phone": "555-7890", "email": "ivy@example.com"},
    {"name": "Jack Anderson", "phone": "555-0987", "email": "jack@example.com"}
]

# File path where the JSON data will be stored
file_path = 'contacts.json'

# Write the data to a JSON file
with open(file_path, 'w') as file:
    json.dump(contacts, file, indent=4)

print(f"Data successfully written to {file_path}")