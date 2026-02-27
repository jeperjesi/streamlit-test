import streamlit as st
import Joseph_script_1
import pandas as pd

df = pd.DataFrame({
    "Script": ["Pablo_script_1.py", "Pablo_script_2.py", "Joseph_script_1.py"],
    "Param1": ["File path", "File path", "URL"],
    "Param1 required": ["Yes", "Yes", "Yes"],
    "Param2": ["File path", "File path", "N/A"],
    "Param2 required": ["Yes", "Yes", "No"]
})

def run_script_a():
    st.write("Executing Pablo_script_1.py...")
    # do work

def run_script_b():
    st.write("Executing Pablo_script_2.py...")
    # do work

def run_script_c():
    st.write("Executing Joseph_script_1.py...")
    result = Joseph_script_1.run_task(param1)
    st.success("Script finished")
    
    # do work


# UI items
st.title("Leap District script runner")
st.write(
    "Select script and enter parameters in input boxes below."
)

script_options = ["Pablo_script_1.py", "Pablo_script_2.py", "Joseph_script_1.py"]

script = st.selectbox(
    "Select script to run",
    script_options
)


param1 = st.text_input(
    label="Enter parameter 1 (if applicable):",
    placeholder="/sites/LeapDistrict/Shared Documents/..."
)

param2 = st.text_input(
    label="Enter parameter 2 (if applicable):",
    placeholder="/sites/LeapDistrict/Shared Documents/..."
)
st.write("")          # gap between input boxes and dataframe
st.write("")          # gap between input boxes and dataframe

st.dataframe(df, hide_index=True)

st.write("")          # gap between dataframe and output
st.write("")          # gap between dataframe and output

st.write("You selected:", script)
st.write("You entered Parameter 1:", param1)
st.write("You entered Parameter 2:", param2)

if st.button("Run"):
    if script == "Pablo_script_1.py":
        st.write("Running script " + script + " ...")
        run_script_a()

    elif script == "Pablo_script_2.py":
        st.write("Running script " + script + " ...")
        run_script_b()

    elif script == "Joseph_script_1.py":
        st.write("Running script " + script + " ...")
        run_script_c()