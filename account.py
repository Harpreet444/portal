import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import prof


cred = credentials.Certificate("alumni-portal-30675-b39489f69d11.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
# firebase_admin.initialize_app(cred)
    

db = firestore.client()
st.session_state.db = db
    
def app():

    co1,co2,co3 = st.columns([1,3,1])
    co2.title('Welcome to :violet[BBSBEC Alumini Portal] :sunglasses:')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''


    def f(): 
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)

            doc_ref = db.collection('Pass').document(user.uid)
            doc = doc_ref.get()

            if doc.exists:
                stored_pw = doc.to_dict().get('pw')  # Replace 'password_field_name' with the actual field name

                print(stored_pw[0] +  "\n" + pw)
                if stored_pw[0] == pw:
                    
                    st.session_state.username = user.uid
                    st.session_state.useremail = user.email
                    
                    global Usernm
                    Usernm=(user.uid)
                    
                    st.session_state.signedout = True
                    st.session_state.signout = True    
                
                else:
                    1/0
            
            else:
                1/0
  
            
        except: 
            co2.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''
    
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        

        
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = co2.selectbox('Login/Signup',['Login','Sign up'])
        email = co2.text_input('Email Address')
        pw = co2.text_input('Password',type='password')
        

        
        if choice == 'Sign up':
            username = co2.text_input("Enter  your unique username")
            if co2.button('Create my account'):
                user = auth.create_user(email = email, password = pw,uid=username)
                
                co2.success('Account created successfully!')
                co2.markdown('Please Login using your email and password')
                data = {"pw": [pw], 'Username': username}
                db.collection('Pass').document(username).set(data)
                st.balloons()
        else:
            # st.button('Login', on_click=f)          
            co2.button('Login', on_click=f)
            
            
    if st.session_state.signout:
                co2.text('Name '+st.session_state.username)
                co2.text('Email id: '+st.session_state.useremail)
                a,b,c = co2.columns([1,1,1])
                a.button('Sign out', on_click=t) 
                prof.app( st.session_state.username)

                      
    def ap():
        st.write('Posts')