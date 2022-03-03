import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('retailers.csv')

df = data[['lat', 'lng']]
df.rename(columns = {'lng':'lon'}, inplace = True)
st.map(df)



