import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit_lottie as stl

def load_lottieurl(url: str):
    """Fetches Lottie JSON data from a URL and handles errors."""
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def app():
    lottie_url_hello = "https://lottie.host/2f4b36dc-1658-4c73-9a78-82df738904c1/dYCuQOEYeh.json"
    lottie_hello = load_lottieurl(lottie_url_hello)

    # Create columns for layout
    col1, col2 = st.columns(2)

    # Display animation only in the second column
    with col2:
        stl.st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",  # Adjust quality as needed
            height=None,
            width=None,
            key=None,
        )

    col1.header("Team :")
    col1.subheader(">>> :violet[Harpreet Singh]")
    col1.subheader(">>> :violet[Harpreet Singh]")
    col1.subheader(">>> :violet[Harnoor Singh]")
    col1.subheader(">>> :violet[Harshpreet Singh]")
if __name__ == "__main__":
    app()
