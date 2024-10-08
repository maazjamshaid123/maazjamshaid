import streamlit as st
import webbrowser

def show_projects():
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)
    col7.markdown("[![Github](https://cdn0.iconfinder.com/data/icons/social-line-transparent/50/Github-line-transparent-128.png)](https://github.com/maazjamshaid123)")
    st.markdown("---")

    #SIYI APP
    col1, col2 = st.columns(2)
    image_url = "images/a8.png"
    col1.image(image_url, width = 400)
    col2.title("SIYI Gimbal Control System App")
    col2.caption('''This gimbal control app is designed for SIYI Gimbals, including models like the A8 Mini and ZR30. 
                    It allows you to manage various gimbal functions, such as movement, zoom, and codec settings.
                    Additionally, the app enables you to test different hex commands to execute specific operations.''')
    col2.caption("[`View More`](https://github.com/maazjamshaid123/SIYI-Gimbal-Control-App)")
    
    st.markdown("---")
    
    # UAV Object Tracker
    col1, col2 = st.columns(2)
    image_url = "images//tgt_mil.png"
    col1.image(image_url, width = 400)
    col2.title("Target Tracking using OpenCV and Kalman Filtering")
    col2.caption('''Utilizes computer vision and Kalman filtering techniques to track objects in real-time. The application 
                 allows users to select an object for tracking by clicking on it in the video stream, and then visualizes the 
                 tracking process, including predicted object positions and velocities.''')
    col2.caption("[`View More`](https://github.com/maazjamshaid123/Target-Tracker-using-OpenCV-and-Kalman-Filter)")

    st.markdown("---")

    #COAC
    col1, col2 = st.columns(2)
    image_url = "images/coc.png"
    col1.image(image_url, width = 400)
    col2.title("Celestial Object Angles Calculator")
    col2.caption('''Designed to calculate and display the azimuth and elevation angles of various celestial objects (such as 
                 the Sun, Moon, and planets) based on a user's specified location (latitude and longitude) and time. It 
                 leverages the `PyEphem` library to compute the positions of these celestial bodies and presents the results in a 
                 user-friendly table format.''')
    col2.caption("[`View More`](https://github.com/maazjamshaid123/Celestial-Object-Angles-Calculator)")

    st.markdown("---")

    # AI Research Assistant
    col1, col2 = st.columns(2)
    image_url = "https://www.nasa.gov/wp-content/uploads/2023/08/aiassistants.jpg"
    col1.image(image_url, width = 400)
    col2.title("AI Research Assistant for Space Scientists")
    col2.caption("`NASA HACKATHON`")
    col2.caption('''Leverages data-driven approaches such as data analysis, visualization, machine learning, and artificial 
               intelligence using `OpenAI` and provides effective solutions for a wide range of problems.''')
    col2.caption("[`Explore`](https://odyssey.streamlit.app/)")
    col2.caption("[`View More`](https://github.com/maazjamshaid123/AI-Research-Assistant-Odyssey)")

    st.markdown("---")
