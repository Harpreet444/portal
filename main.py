import streamlit as st

from streamlit_option_menu import option_menu

import account, community, events, your_posts, gallary,about

st.set_page_config(
        page_title="BBSBEC Alumini Portal",page_icon="LOGO.jpg",layout='wide'
)

# Create columns in the sidebar
col1, col2, col3 = st.sidebar.columns([0.5, 4, 0.5])


with col2:
    st.image("logo.png")  # Replace with your image path


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
                menu_title='BBSBEC',
                options=['Account','Community','Events','Your Posts','Gallery','Developers'],
                icons=['person-circle','house-fill','trophy-fill','chat-fill','info-circle-fill','gear'],
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
        elif app =='Developers':
            about.app()
        
    run()                                         

    