import streamlit as st
from streamlit_webrtc import webrtc_streamer

role = 'perform'

st.set_page_config(
    initial_sidebar_state="expanded",
)

st.title('Welcome to :blue[SignSense]' , anchor=False , help='Interprets Performed Sign Language' )
st.subheader("Hello :orange[Performer], Choose your Action to Perfrom" ,anchor=False)

st.sidebar.title('Choose Action ')
method = st.sidebar.radio( 'Translate', options=[':orange[Recorded] Video', ':orange[Live] Actions'] )

if (method == ":orange[Recorded] Video"):
    st.subheader("Translate :orange[Recorded] Video")
    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "mov", "mpeg4"])
    if uploaded_video is not None:
        st.video(uploaded_video)
if ( method == ":orange[Live] Actions"):
    st.subheader("Translate :orange[Live] Actions")
    webrtc_streamer(key="live") 



