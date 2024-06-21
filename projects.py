import streamlit as st
import webbrowser

def show_projects():

    # UAV Object Tracker
    col1, col2 = st.columns(2)
    image_url = "images//tgt_mil.png"
    col1.image(image_url, width = 400)
    col2.title("OpenCV Target Tracker for UAVs")
    col2.caption('''Utilizes computer vision and Kalman filtering techniques to track objects in real-time. The application 
                 allows users to select an object for tracking by clicking on it in the video stream, and then visualizes the 
                 tracking process, including predicted object positions and velocities.''')
    col2.text("[View More](https://github.com/maazjamshaid123/Target-Tracker-using-OpenCV-and-Kalman-Filter)")

    # AI Research Assistant
    col1, col2 = st.columns(2)
    image_url = "https://www.nasa.gov/wp-content/uploads/2023/08/aiassistants.jpg"
    col1.image(image_url, width = 400)
    col2.title("AI Research Assistant for Space Scientists")
    col2.caption('''Leverages data-driven approaches such as data analysis, visualization, machine learning, and artificial 
               intelligence using OpenAI and provides effective solutions for a wide range of problems.''')
    col2.text("[Explore](https://odyssey.streamlit.app/)")
    col2.text("[View More](https://github.com/maazjamshaid123/AI-Research-Assistant-Odyssey)")


    


