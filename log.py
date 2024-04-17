import streamlit as st
import pandas as pd
import numpy as np

# Initialize session state for dynamic data updates
if 'library_data' not in st.session_state:
    st.session_state.library_data = pd.DataFrame({
        'Book ID': [1, 2, 3, 4, 5],
        'Title': ['The Catcher in the Rye', 'To Kill a Mockingbird', 'Pride and Prejudice', 'The Great Gatsby', 'The Hunger Games'],
        'Author': ['J.D. Salinger', 'Harper Lee', 'Jane Austen', 'F. Scott Fitzgerald', 'Suzanne Collins'],
        'Status': ['Available', 'Available', 'Available', 'Available', 'Available']
    })

# Function to check out and return books
def manage_book(book_id, action):
    if action == 'Check Out' and st.session_state.library_data.loc[book_id - 1, 'Status'] == 'Available':
        st.session_state.library_data.loc[book_id - 1, 'Status'] = 'Checked Out'
        st.success(f"Book ID {book_id} checked out successfully.")
    elif action == 'Return' and st.session_state.library_data.loc[book_id - 1, 'Status'] == 'Checked Out':
        st.session_state.library_data.loc[book_id - 1, 'Status'] = 'Available'
        st.success(f"Book ID {book_id} returned successfully.")
    else:
        st.error(f"Book ID {book_id} cannot be processed for {action}.")

st.title('Advanced Library Management System')

# Display the table of books
st.header('Available Books')
st.table(st.session_state.library_data)

# Search functionality
st.header("Search for Books")
search_query = st.text_input("Enter book title or author")
if search_query:
    results = st.session_state.library_data[(st.session_state.library_data['Title'].str.contains(search_query, case=False)) | 
                                            (st.session_state.library_data['Author'].str.contains(search_query, case=False))]
    if not results.empty:
        st.table(results)
    else:
        st.write("No books found.")

# Form to check out books
with st.form("book_management_form"):
    st.header("Manage Books")
    book_id = st.number_input("Enter Book ID", min_value=1, max_value=len(st.session_state.library_data), step=1)
    action = st.radio("Action", ['Check Out', 'Return'])
    submitted = st.form_submit_button("Submit")
    if submitted:
        manage_book(book_id, action)
