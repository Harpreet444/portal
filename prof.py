import streamlit as st
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth


def app(username):
       db = firestore.client()
       co1,co2,co3 = st.columns([1,3,1])
       co2.header("Alumini data updater :")
       fn = co2.text_input(label="Full name")
       co = co2.text_input(label="Course")
       br = co2.text_input(label="Branch")
       ba = co2.text_input(label="Batch")
       up = co2.button("Update")



       if up:
            data = {'Full name': fn, 'Course': co,'Branch':br,'Batch':ba}
            db.collection('Profile').document(username).set(data)
            st.toast("Change saved")
