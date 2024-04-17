# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:48:47 2024

@author: jperezr
"""

import streamlit as st


import sys


st.title("BASE DE DATOS NACIONAL DE PENSIONES NO RECLAMADAS")

st.header("")

st.subheader("")
st.subheader("")
st.subheader("")


# Create an empty container
placeholder = st.empty()

actual_email = ['TOGP430305MVZTCV03',
               'SAAA411108MVZTCV04',
               'DOFR400401MVZTCV05']

actual_password = ['12345678900',
                  '12345678911',
                  '12345678922']

resultado_busqueda =['Cuenta Activa', 
                    'Cuenta Inactiva',
                    'Cuenta Inactiva']

error1=['CURP o NSS INCORRECTOS','CURP o NSS INCORRECTOS','CURP o NSS INCORRECTOS']


# Insert a form in the container
with placeholder.form("Acceder",clear_on_submit=True):
    st.markdown("#### Intoducir:")
    email = st.text_input("CURP")
    password = st.text_input("NSS", type="password")
    submit = st.form_submit_button("Acceder")
     

if submit:

      for i in range(3): 

          if email == actual_email[i] and password == actual_password[i]:
               placeholder.empty()
               st.success("CURP y NSS CORRECTOS") 
               st.success(resultado_busqueda[i])
               sys.exit(0)
       

if submit:

      for j in range(3): 

          if email != actual_email[j] and password != actual_password[j]:
               placeholder.empty()
               st.success(error1[j])
               sys.exit(0)
      