import streamlit as st

#Config
st.set_page_config(
    initial_sidebar_state="collapsed",
)
col1 , col2 = st.columns(2)
 

with col1:
    #Title
    st.markdown( 
        ''' 
        <style>
            .appview-container .main .block-container { 
                padding-top: 2.5rem; 
                width: 100%;
            }
            .st-emotion-cache-uf99v8 { 
                align-items: start; 
                padding-left: 10%;
                padding-right: 10rem;
            }
            .sign-Sense{
                color: rgb(96, 180, 255); 
                font-size: 1.5rem;
            }
            .st-emotion-cache-ocqkz7{
                width: 80vw;
            }
            .st-emotion-cache-1v0mbdj{
                margin-top: 10rem;
                border-radius: 25px;
                border: 2px solid #60B4FF; 
            }
            .st-emotion-cache-upseer{
                justify-content: center;
                border: 2px solid #60B4FF;
                height: 80px;
            }
        </style> 
        ''' ,unsafe_allow_html=True 
    ) 
    st.title(':blue[SignSense]' , anchor=False  )
    st.subheader('Inclusive Platform For :blue[Deaf and Mute]' , anchor=False  , divider='blue')

    #Introduction,Abstract,Conclusion
    st.markdown('''
        <p>
            Imagine a world where communication barriers dissolve entirely,where online spaces buzz with vibrant conversation regardless of hearing ability. This vision becomes reality with the introduction of <span class="sign-Sense" >SignSense</span> , a revolutionary online platform dedicated to seamlessly bridging the communication gap for deaf and mute individuals. Leveraging advancements in speech recognition, computer vision, and machine learning, <span class="sign-Sense" >SignSense</span> empowers deaf and mute communities to actively participate in online meetings, educational endeavors, and even entertainment spheres like never before.
                
        </p>
        <p>
            Driven by a deep commitment to inclusivity, <span class="sign-Sense" >SignSense</span> tackles the pervasive challenge of online communication inaccessibility for the deaf and mute population. Equipped with cutting-edge technology, the platform seamlessly translates spoken language into sign language and vice versa, ensuring real-time, uninterrupted dialogue. The platform caters to diverse use cases, including online meetings fostering collaborative work environments, educational settings maximizing learning potential, and entertainment platforms unlocking immersive experiences.
        </p>   
        <p>
            More than just a technological marvel, <span class="sign-Sense" >SignSense</span> represents a significant step towards fostering a truly inclusive online world. By breaking down communication barriers, the platform empowers deaf and mute individuals to actively engage, contribute, and thrive in the digital landscape. <span class="sign-Sense" >SignSense</span> stands as a testament to the power of technology to connect, empower, and ultimately dismantle communication barriers, fostering a more inclusive and vibrant online society for all.
        </p>
        ''' , unsafe_allow_html=True 
    )
    agree_terms = st.checkbox("I agree to Terms and Conditions")
    st.page_link( './Pages/TnC.py' , label='Terms and Conditions ')
    if agree_terms :
        to_main = st.button("Enter into :blue[SignSense]"  )
        if to_main:
            with st.container():
                st.subheader("Choose your Role:")
                c1, c2 = st.columns(2)
                with c1:
                    st.page_link("./Pages/user_speaker.py", label="Speaker", help="Click to proceed as a Speaker")
                with c2:
                    st.page_link("./Pages//user_performer.py", label="Performer", help="Click to proceed as a Performer")

    else:
        st.button("Enter into :blue[SignSense]" , disabled=True)
with col2:
    st.image('./index-bg.png' , use_column_width=True) 
    