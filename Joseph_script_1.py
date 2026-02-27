import streamlit as st

def run_task(param1):

    st.markdown(
    f"""
    <a href="{param1}" target="_blank">
        Open in new tab
    </a>
    """,
    unsafe_allow_html=True
)