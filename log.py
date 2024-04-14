import streamlit as st
import pandas as pd

# Sample data for the library system
data = {
    'Book ID': [1, 2, 3, 4, 5],
    'Title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E'],
    'Author': ['Author A', 'Author B', 'Author C', 'Author D', 'Author E'],
    'Status': ['Available', 'Checked Out', 'Available', 'Checked Out', 'Available']
}
df = pd.DataFrame(data)

# Title of the app
st.title('Library Management System')

# Display the table of books
st.header('Available Books')
st.table(df)

# Form to check out books
with st.form("check_out_form"):
    st.header("Check Out a Book")
    book_id = st.number_input("Enter Book ID to check out", min_value=1, max_value=len(df), step=1)
    submitted = st.form_submit_button("Check Out")
    if submitted:
        if df.loc[df['Book ID'] == book_id, 'Status'].values[0] == 'Available':
            df.loc[df['Book ID'] == book_id, 'Status'] = 'Checked Out'
            st.success(f"Book ID {book_id} checked out successfully.")
        else:
            st.error(f"Book ID {book_id} is already checked out.")

# Form to return books
with st.form("return_form"):
    st.header("Return a Book")
    book_id = st.number_input("Enter Book ID to return", min_value=1, max_value=len(df), step=1, key='return')
    submitted = st.form_submit_button("Return")
    if submitted:
        if df.loc[df['Book ID'] == book_id, 'Status'].values[0] == 'Checked Out':
            df.loc[df['Book ID'] == book_id, 'Status'] = 'Available'
            st.success(f"Book ID {book_id} returned successfully.")
        else:
            st.error(f"Book ID {book_id} is not checked out.")
