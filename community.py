import streamlit as st
import firebase_admin
from firebase_admin import firestore

def app():

    co1,co2,co3 = st.columns([1,3,1])

    try:
        if 'db' not in st.session_state:
            st.session_state.db = ''

        db = firestore.client()
        st.session_state.db = db

        # Placeholder login functionality (replace with actual authentication logic)
        username = st.session_state.username

        ph = ''
        if username == '':
            ph = 'Login to be able to post!!'
        else:
            ph = 'Post your thought'
        post = co2.text_area(label=' :orange[+ New Post]', placeholder=ph, height=None, max_chars=500)

        if co2.button('Post', use_container_width=True):
            if post != '':
                info = db.collection('Posts').document(username).get()
                if info.exists:
                    info = info.to_dict()
                    if 'Content' in info.keys():
                        pos = db.collection('Posts').document(username)
                        pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(post)])})
                    else:
                        data = {"Content": [post], 'Username': username}
                        db.collection('Posts').document(username).set(data)
                else:
                    data = {"Content": [post], 'Username': username}
                    db.collection('Posts').document(username).set(data)
                co2.success('Post uploaded!!')

        co2.header(' :violet[Latest Posts] ')

        docs = db.collection('Posts').get()

        for doc in docs:
            d = doc.to_dict()
            try:
                co2.text_area(label=':green[Posted by:] ' + ':orange[{}]'.format(d['Username']),
                             value=d['Content'][-1], height=20)
            except KeyError:
                co2.write("Error: Missing 'Username' field in a document.")

    except:
        co2.warning("Operation Failed Check if you have login account")