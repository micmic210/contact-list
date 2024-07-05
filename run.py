import streamlit as st
import json

# Path to the JSON file where contacts are stored
FILE_PATH = 'contacts.json'

# Function to load contacts from the JSON file
def load_contacts(file_path):
    try:
        with open(file_path, 'r') as file:
            contacts = json.load(file)  # Load the contacts from the file
    except FileNotFoundError:  # If the file does not exist, initialize an empty list
        contacts = []
    return contacts  # Return the list of contacts

# Function to save contacts to the JSON file
def save_contacts(file_path, contacts):
    with open(file_path, 'w') as file:
        json.dump(contacts, file, indent=4)  # Write the contacts to the file with indentation

# Function to list all contacts
def list_contacts(contacts):
    st.write("## Contact List")
    if not contacts:  # If there are no contacts, display a message
        st.write("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, 1):
            try:
                st.write(f"{idx}. **Name**: {contact['name']} - **Phone**: {contact['phone']} - **Email**: {contact['email']}")
            except KeyError as e:
                st.error(f"Error displaying contact {idx}: Missing key {e}")

# Function to add a new contact
def add_contact(contacts):
    # Get input from the user for name, phone, and email
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    if st.button("Add Contact"):  # If the user clicks the "Add Contact" button
        contacts.append({"name": name, "phone": phone, "email": email})  # Add the new contact to the list
        save_contacts(FILE_PATH, contacts)  # Save the updated contacts list to the file
        st.success("Contact added successfully.")  # Display a success message

# Function to update an existing contact
def update_contact(contacts):
    list_contacts(contacts)  # List all contacts
    # Get the index of the contact to update
    idx = st.number_input("Enter the number of the contact to update", min_value=1, max_value=len(contacts))
    if idx:
        contact = contacts[idx - 1]  # Get the contact details
        # Get new details from the user with pre-filled values
        name = st.text_input("New name", value=contact['name'])
        phone = st.text_input("New phone", value=contact['phone'])
        email = st.text_input("New email", value=contact['email'])
        if st.button("Update Contact"):  # If the user clicks the "Update Contact" button
            contacts[idx - 1] = {"name": name, "phone": phone, "email": email}  # Update the contact details
            save_contacts(FILE_PATH, contacts)  # Save the updated contacts list to the file
            st.success("Contact updated successfully.")  # Display a success message

# Function to delete a contact
def delete_contact(contacts):
    list_contacts(contacts)  # List all contacts
    # Get the index of the contact to delete
    idx = st.number_input("Enter the number of the contact to delete", min_value=1, max_value=len(contacts))
    if idx:
        if st.button("Delete Contact"):  # If the user clicks the "Delete Contact" button
            contacts.pop(idx - 1)  # Remove the contact from the list
            save_contacts(FILE_PATH, contacts)  # Save the updated contacts list to the file
            st.success("Contact deleted successfully.")  # Display a success message

# Function to search for contacts
def search_contact(contacts):
    search_term = st.text_input("Enter name, phone, or email to search")  # Get the search term from the user
    if search_term:
        # Find contacts that match the search term
        found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone'] or search_term in contact['email']]
        if found_contacts:
            st.write("## Search Results")
            # Display each matching contact with its details
            for contact in found_contacts:
                st.write(f"**Name**: {contact['name']} - **Phone**: {contact['phone']} - **Email**: {contact['email']}")
        else:
            st.write("No matching contacts found.")  # If no contacts match, display a message

# Main function to control the application flow
def main():
    st.title("Contact Book")  # Display the title
    contacts = load_contacts(FILE_PATH)  # Load the contacts from the file

    # Create a menu in the sidebar
    menu = ["Add Contact", "List Contacts", "Update Contact", "Delete Contact", "Search Contact"]
    choice = st.sidebar.selectbox("Menu", menu)  # Get the user's choice from the menu

    # Based on the user's choice, call the corresponding function
    if choice == "Add Contact":
        st.subheader("Add Contact")
        add_contact(contacts)
    elif choice == "List Contacts":
        st.subheader("List Contacts")
        list_contacts(contacts)
    elif choice == "Update Contact":
        st.subheader("Update Contact")
        update_contact(contacts)
    elif choice == "Delete Contact":
        st.subheader("Delete Contact")
        delete_contact(contacts)
    elif choice == "Search Contact":
        st.subheader("Search Contact")
        search_contact(contacts)

# Entry point of the application
if __name__ == "__main__":
    main()  # Run the main function