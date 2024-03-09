import streamlit as st
from firebase_admin import firestore

def app():

    co1,co2,co3 = st.columns([1,3,1])
    db = firestore.client()

    co2.title('Alumini Events And:violet[ Latest Announcement] :sunglasses:')

    doc_ref = db.collection('Events').document('admin')
    doc = doc_ref.get()

    if doc.exists:
        d = doc.to_dict()

        if 'Content' in d.keys():
            # Reverse order using slicing
            events = d['Content'][::-1]

            # Iterate through events in reverse order
            for content in events:
                co2.text_area(label='Admin', value=content, height=20)  # Remove label
        else:
            co2.write("No 'Content' field found in the 'admin' document.")
    else:
        co2.write("The 'admin' document does not exist in the 'Events' collection.")
