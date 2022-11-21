import streamlit as st
from joblib import dump,load
import numpy as np
model=load('Laptop_Price.joblib')
st.title("Laptop Price Pridiction")
var1=st.selectbox("Company",['Dell' ,'Lenovo','HP','Asus','Acer','MSI','Toshiba','Apple','Samsung','Razer','Mediacom','Microsoft','Xiaomi','Vero', 
'Google','Fujitsu','LG','Huawei'])

var2=st.selectbox("TypeName",['Ultabook','Notebook','Gaming','Workstation','Netbook','2 in 1 Convertible'])
var3=st.selectbox("Ram",[2,4,6,8,16,24,32,64])
var4=st.selectbox("Inches",[10,12,14,16.18])
var5=st.number_input("Weight",2.20,2.34)
var6=st.selectbox("X_res",[1366,1440,1600,1920,2160,2256,2304,2400,2560,2736,2880,3200,3840,])  
var7=st.selectbox("Y_res",[768,900,1080,1200,1440,1504,1600,1800,1824,2160])
var9=st.selectbox("Cpu Brand",['Intel Core i7','Intel Core i5','Other Intel Processor','Intel Core i3','AMD Processor'])
var14=st.selectbox("Gpu Brand",['Intel','Nvidia','AMD'])
var10=st.selectbox("HDD",[0,32,128,500,1000,2000])
var11=st.selectbox("SSD",[0,8,16,32,64,128,180,240,256,512,1000,1024])
var12=st.selectbox("OP",['Mac','Windows','No Os/Other'])
var8=st.selectbox("Touchscreen",['True','False'])
var13=st.selectbox("lps",['True','False'])

select=st.button("Submit")
var15=(((var6)**2+(var7)**2)**0.5)/var4

if select:
    input= np.array([[f"Company:{var1}",f"TypeName:{var2}",f"Ram:{var3}",f"Weight:{var5}",f"Touchscreen:{var8}",f"lps:{var13}",f"ppi:{var15}",f"Cpu Brand:{var9}",f"HDD:{var10}",f"SSD:{var11}",f"Gpu brand:{var14}",f"OP:{var12}"]])
    
    pred = model.predict(input)

    st.write("The Price :-")
    st.write(pred.predictions)




