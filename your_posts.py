import streamlit as st
from firebase_admin import firestore

  
def app():

    co1,co2,co3 = st.columns([1,3,1])

    db=firestore.client()


    try:
        co2.title('Posted by: '+st.session_state['username'] )

            
        result = db.collection('Posts').document(st.session_state['username']).get()
        r=result.to_dict()
        content = r['Content']
            
        
        def delete_post(k):
            c=int(k)
            h=content[c]
            try:
                db.collection('Posts').document(st.session_state['username']).update({"Content": firestore.ArrayRemove([h])})
                co2.warning('Post deleted')
            except:
                st.write('Something went wrong..')
                
        for c in range(len(content)-1,-1,-1):
            # co2.text_area(label='',value=content[c])
            # co2.markdown("**Admin:**", unsafe_allow_html=True)
            co2.markdown(f"<div style='border: 1px solid #ddd; padding: 5px; background-color: #F0F2F6'>{content[c]}</div>", unsafe_allow_html=True)
            co2.button('Delete Post', on_click=delete_post, args=([c] ), key=c)        

        
    except:
        if st.session_state.username=='':
            co2.text('Please Login first')        