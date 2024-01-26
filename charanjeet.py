import streamlit as st
import pandas as pd
data=pd.read_excel(r"Rhimjhim.xlsx")

new_data=st.experimental_data_editor(data,num_rows="dynamic")
upload=st.sidebar.file_uploader("Pleaase Uplaod file here")


final_data=pd.DataFrame(new_data)
final_data["Order Qty(MT)"]=final_data["Order Qty(MT)"]
final_data["Dispatch Qty(MT)"]=final_data["Dispatch Qty(MT)"]

final_data["Pending Qty"]=(final_data["Order Qty(MT)"])-(final_data["Dispatch Qty(MT)"])
st.write(final_data)




