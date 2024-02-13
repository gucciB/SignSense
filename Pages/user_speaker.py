import streamlit as st
from streamlit_webrtc import webrtc_streamer
role = 'speak'

st.set_page_config(
    initial_sidebar_state="expanded",
)

# st.markdown('''
#     <style>
#         .row-widget.stButton{
#             display: flex;
#             justify-content: center;
#     </style> 
# ''',unsafe_allow_html=True)

st.title('Welcome to :blue[SignSense]' , anchor=False , help='Interprets Performed Sign Language' )
st.subheader("Hello :violet[Speaker], Choose your Action to Perfrom : " ,anchor=False)

st.sidebar.title('Choose Action ')
method = st.sidebar.radio( 'Translate', options=[':violet[Recorded] Audio', ':violet[Live] Speech'] )

if (method == ":violet[Recorded] Audio"):
    st.subheader("Translate :violet[Recorded] Audio")
    uploaded_audio = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
    if uploaded_audio is not None:
        st.audio(uploaded_audio)
if ( method == ":violet[Live] Speech"):
    st.subheader("Translate :violet[Live] Speech")
    webrtc_streamer(key="live") 