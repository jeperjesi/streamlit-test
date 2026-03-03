import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
master_fund_list_path = BASE_DIR / "data" / "master_fund_list.csv"

#script parameters (move to csv file?)
df_params = pd.DataFrame({
    "Script": ["Pablo_script_1.py", "Pablo_script_2.py", "Joseph_script_1.py"],
    "Param1": ["File path", "File path", "URL"],
    "Param1 required": ["Yes", "Yes", "Yes"],
    "Param2": ["File path", "File path", "N/A"],
    "Param2 required": ["Yes", "Yes", "No"]
})

df_master_fund_list = pd.read_csv(master_fund_list_path)

#script calls
def run_script_a():
    st.write("Executing Pablo_script_1.py...")
    # do work

def run_script_b():
    st.write("Executing Pablo_script_2.py...")
    # do work

def run_script_c():
    import Joseph_script_1
    st.write("Executing Joseph_script_1.py...")
    result = Joseph_script_1.run_task(param_freetext_1)
    st.success("Script finished")

def run_script_d():
    import nav_get_trading_gain_loss
    st.write("Executing nav_get_trading_gain_loss.py...")
    report_date = param_date_1.strftime("%m-%d-%Y")
    result = nav_get_trading_gain_loss.get_trading_gain_loss(st.secrets["NAV_BASE_URL"], st.secrets["INDURO_API_KEY"], st.secrets["INDURO_API_SECRET"], "175076", report_date)
    st.dataframe(result.iloc[:, :30], hide_index=True)


# UI items
st.title("Leap District script runner")
st.sidebar.write("App pages")
st.write(
    "Select script and enter parameters in input boxes below."
)

script_options = ["Pablo_script_1.py", "Pablo_script_2.py", "Joseph_script_1.py", "nav_get_trading_gain_loss.py"]

script = st.selectbox(
    "Select script to run",
    script_options
)

st.write("") 
st.write("Global parameters")

param_fund_name = st.selectbox("Fund name:", df_master_fund_list["fund_name"].unique())

param_date_1 = st.date_input(
    "Date:",
    value=(pd.Timestamp.today().replace(day=1) - pd.Timedelta(days=1)
).date()
)

st.write("") 
st.write("Other parameters")

param_freetext_1 = st.text_input(
    label="Enter parameter 1 (if applicable):",
    placeholder="/sites/LeapDistrict/Shared Documents/..."
)

param_freetext_2 = st.text_input(
    label="Enter parameter 2 (if applicable):",
    placeholder="/sites/LeapDistrict/Shared Documents/..."
)

param_date_2 = st.date_input(
    "Date:"
)

st.write("")          # gap between input boxes and dataframe
st.write("")          # gap between input boxes and dataframe

st.write("Script parameters") 
st.dataframe(df_params, hide_index=True)
st.write("")
st.write("API call reference") 
st.dataframe(df_master_fund_list, hide_index=True)

st.write("")          # gap between dataframe and output
st.write("")          # gap between dataframe and output

st.write("You selected:", script)


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
    elif script == "nav_get_trading_gain_loss.py":
        st.write("Running script " + script + " ...")
        run_script_d()