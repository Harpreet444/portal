import streamlit as st

from streamlit_option_menu import option_menu

import account, community, events, your_posts, gallary

st.set_page_config(
        page_title="BBSBC Alumini Portal",page_icon="LOGO.jpg",layout='wide'
)

st.sidebar.image("logo.png")

class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })    

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='BBSBC',
                options=['Account','Community','Events','Your Posts','Gallery'],
                icons=['person-circle','house-fill','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0
                # styles={
        #             "container": {"padding": "5!important"},
        # "icon": {"color": "white", "font-size": "23px"}, 
        # "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        # "nav-link-selected": {"background-color": "#02ab21"},}
                
                )    

        if app== 'Community':
            community.app()
        elif app== 'Account':
            account.app()
        elif app== 'Events':
            events.app()
        elif app== 'Your Posts':
            your_posts.app()
        elif app == 'Gallery':
            gallary.app()
        

    run()                                         

    