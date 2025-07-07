import streamlit as st
from db import create_table, add_student, view_students, delete_student

st.title("🎓 Student Record Manager")

create_table()

menu = ["Add Student", "View Students", "Delete Student"]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Add Student":
    st.subheader("📥 Add New Student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=35, step=1)
    course = st.text_input("Course")

    if st.button("Add"):
        add_student(name, age, course)
        st.success(f" Successfully Added {name} to the database")

elif choice == "View Students":
    st.subheader("📋 All Students Records")
    data = view_students()
    if data:
        for row in data:
            st.write(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")
    else:
        st.info("No records found.")

elif choice == "Delete Student":
    st.subheader("❌ Delete Student by Name")
    name = st.text_input("Enter the name to delete")
    if st.button("Delete"):
        delete_student(name)
        st.warning(f"Deleted records with name {name} Successfully")
