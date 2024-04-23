import streamlit as st
import pandas as pd
import time 
from datetime import datetime
from add_faces import add_faces_to_dataset
from test import run_face_recognition

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")

# Text input for entering the name
name = st.text_input("Enter Your Name:")

# Add a button to trigger the "Add Faces to Dataset" functionality
if st.button("Add Faces to Dataset"):
    if name:
        add_faces_to_dataset(name)
    else:
        st.warning("Please enter a name before adding faces to the dataset.")

# Add a button to trigger the "Run Face Recognition" functionality
if st.button("Run Face Recognition"):
    run_face_recognition()

# Load and display the attendance DataFrame
df = pd.read_csv("Attendance/Attendance_" + date + ".csv")
st.dataframe(df.style.highlight_max(axis=0))
