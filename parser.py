import streamlit as st
from data_preprocessing import preprocessing

df = preprocessing()

keys = [i[1:] for i in list(df.keys())]
option = st.selectbox('Select the type of GPS', (keys))
r_df = df['$' + option]

columns = st.multiselect('Select columns to show', list(r_df.columns))
col_names = [col for col in columns]
r_df = r_df[col_names]

try:
    for i in col_names:
        if float(r_df[i].min()) < float(r_df[i].max()):
            x = st.slider("Choose the range of  " + i, float(r_df[i].min()),
                          float(r_df[i].max()), (float(r_df[i].min()),
                          float(r_df[i].min())), 0.5)
            r_df = r_df[r_df[i].between(x[0], x[1])]
        else:
            st.write("This column is a constant of value `minValueToken`")

except ValueError:
    st.write('You can not choose a range for non-number type')

st.write('You selected:', r_df)
