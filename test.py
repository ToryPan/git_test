import streamlit as st
import pandas as pd
import codecs
from pandas_profiling import ProfileReport
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report



st.subheader("Automated EDA with Pandas Profile")
data_file = st.file_uploader("Upload CSV",type=['csv'])
if data_file is not None:
    df = pd.read_csv(data_file)
    st.dataframe(df.head())
    Profile = ProfileReport(df)
	st_profile_report(Profile)

