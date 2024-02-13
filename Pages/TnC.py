import streamlit as st

st.header('Terms and Conditions for :blue[SignSense]')
st.write('''
    1. <strong>Introduction</strong>:

    These Terms and Conditions ("Terms") govern your access and use of the SignSense platform ("Platform"), which provides real-time sign language interpretation services through speech recognition, computer vision, and machine learning. By accessing or using the Platform, you agree to be bound by these Terms.

    2. <strong>Eligibility</strong>:

    The Platform is intended for use by individuals who are 18 years of age or older and have the legal capacity to enter into binding contracts.

    3. <strong>User Accounts</strong>:

    You may create a user account on the Platform by providing accurate and complete information. You are responsible for maintaining the confidentiality of your account credentials and are solely responsible for all activities that occur under your account.

    4. <strong>Acceptable Use</strong>:

    You agree to use the Platform only for lawful purposes and in accordance with these Terms. You may not:

    Use the Platform in a way that violates the privacy or intellectual property rights of others.
    Use the Platform to transmit any harmful or offensive content.
    Interfere with or disrupt the Platform or its servers.
    Attempt to gain unauthorized access to the Platform.
         
    5. <strong>Interpreter Services</strong>:

    SignSense provides access to professional sign language interpreters through video calls. The interpreters are independent contractors and are not employees of SignSense. You are responsible for your own interactions with the interpreters and understand that SignSense is not responsible for any disputes arising from such interactions.

    6. <strong>Fees and Payment</strong>:

    SignSense charges a fee for using its services. The fees are subject to change, and we will provide you with reasonable notice of any changes. Payment is due at the time of service and can be made through the approved payment methods offered on the Platform.

    7. <strong>Disclaimer of Warranties</strong>:

    SignSense provides the Platform "as is" and makes no warranties, express or implied, about its accuracy, reliability, completeness, or suitability for any particular purpose. We do not guarantee that the Platform will be available at all times or that it will be free from errors or interruptions.

    8. <strong>Limitation of Liability</strong>:

    SignSense is not liable for any damages arising out of or in connection with your use of the Platform, including, but not limited to, direct, indirect, incidental, consequential, or punitive damages.

    9. <strong>Termination</strong>:

    SignSense may terminate your access to the Platform at any time and for any reason, with or without notice. You may also terminate your account at any time.

    10. <strong>Governing Law</strong>:

    These Terms shall be governed by and construed in accordance with the laws of [Jurisdiction].

    11. <strong>Entire Agreement</strong>:

    These Terms constitute the entire agreement between you and SignSense regarding your use of the Platform.

    12. <strong>Amendments</strong>:

    SignSense may amend these Terms at any time by posting the amended Terms on the Platform.

    13. <strong>Contact</strong>:

    If you have any questions about these Terms, please contact us at [Email Address].            
''' , unsafe_allow_html=True)

st.divider()
st.page_link( 'index.py' , label='Back to :blue[Main Page]' )