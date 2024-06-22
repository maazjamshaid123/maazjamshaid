import streamlit as st
import os

def download_file(file_path):
    with open(file_path, "rb") as file:
        btn = st.download_button(
            label="Download CV",
            data=file,
            file_name=os.path.basename(file_path),
            mime="text/plain"
        )

def show_intro():
    file_path = "docs/MaazJamshaid_CV.pdf"  
    st.title("Maaz Jamshaid")
    st.caption("Avionics Engineer - [Institute of Space Technology](https://ist.edu.pk/) (2022)")
    st.caption("📍Peshawar, Islamabad")

    download_file(file_path)

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)
    with col1:
        st.markdown("[![Linkedin](https://cdn0.iconfinder.com/data/icons/social-line-transparent/46/LinkedIn-line-transparent-128.png)](https://www.linkedin.com/in/maazjamshaid/)")
    with col2:
        st.markdown("[![Github](https://cdn0.iconfinder.com/data/icons/social-line-transparent/50/Github-line-transparent-128.png)](https://github.com/maazjamshaid123)")
    with col3:
        st.markdown("[![Whatsapp](https://cdn0.iconfinder.com/data/icons/social-line-transparent/50/Whatsapp-line-transparent-128.png)](https://wa.me/03095183754)")
    with col4:
        st.markdown("[![Calendly](https://cdn0.iconfinder.com/data/icons/social-line-transparent/50/Trello-line-transparent-64.png)](https://calendly.com/maazjamshaid-123/30min)")
        
    st.markdown("---")
    st.text("AVIONICS | UAVs | SPACE")

    st.caption('''I am currently serving as an Imagery Design Engineer at the [Pakistan Air Force](https://en.wikipedia.org/wiki/Pakistan_Air_Force), 
             where I am working in object detection and tracking using IR imagery, integrating deep learning algorithms, and 
             enhancing gimbal systems with computer vision.''')
    st.caption('''My previous role as an Avionics Engineer at [Sysverve Aerospace](https://www.sysverveaerospace.com/) 
             involved developing AI-based UAV systems for autonomous target tracking and implementing classical image processing 
             techniques on embedded systems. I have hands-on experience with various flight controllers and Mission Planner 
             software and a robust background in both theoretical and practical aspects of Avionics and Machine Learning''')
    st.caption("I aim to broaden my skills and deepen my expertise in the field of space.")
    
    st.markdown("---")

    st.write("Final Year Project")
    st.caption("[Design of Lightweight Encryption Scheme for Secure Data Communication in UAVs](https://github.com/maazjamshaid123/MyProjects/raw/main/Design%20of%20Lightweight%20Image%20Encryption%20Scheme%20for%20Secure%20Communication%20for%20UAVs.pptx)")
    
    st.markdown("---")
    st.write("Courses and Certifications")
    st.caption("[Introduction to Programming with MATLAB](http://coursera.org/verify/4MC8TB57DLUP)")
    st.caption("[Programming for Everybody (Getting Started with Python)](https://www.coursera.org/account/accomplishments/verify/SHY6LQMJQ2YX)")
    st.caption("[Robotics: Aerial Robotics](https://www.coursera.org/account/accomplishments/verify/3X7FYGR4PWRN)")
    st.caption("[Supervised Machine Learning: Regression and Classification](https://www.coursera.org/account/accomplishments/verify/DLGNS4CNAM7Y)")
    st.caption("[Advanced Learning Algorithms](https://www.coursera.org/account/accomplishments/verify/HJKTURGQ4BQ8)")
    st.caption("[Data-driven Astronomy](https://www.coursera.org/learn/data-driven-astronomy)")
    st.markdown("---")

    st.write("Technical Skills")
    items = [
        'Python',
        'OpenCV',
        'UAV system integration',
        'MATLAB',
        'Image Processing',
        'Statistical Analytics',
        'Computer Vision',
        'CAD Modelling in Fusion 360',
        'Mission Planner & QGround Control',
        'UAV Transmission Links: MK32, H16, Herelink',
        'Gimbal control using PWM/serial signals',
        'Gimbals: SIYI, Tarot',
        'Socket Programming',
        'Data WebApp Development'
    ]
    num_rows = len(items) // 3 + 1
    
    for i in range(num_rows):
        col1, col2, col3 = st.columns(3)
        if i*3 < len(items):
            col1.info(items[i*3])
        if i*3+1 < len(items):
            col2.info(items[i*3+1])
        if i*3+2 < len(items):
            col3.info(items[i*3+2])
