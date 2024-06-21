import streamlit as st
from intro import show_intro
from projects import show_projects

st.set_page_config(page_title='Maaz Jamshaid', layout='wide', menu_items={
    'Get Help': 'https://www.linkedin.com/in/maazjamshaid/',
    'Report a bug': 'https://www.linkedin.com/in/maazjamshaid/',
    'About': 'by [Maaz Jamshaid](https://www.linkedin.com/in/maazjamshaid/), maazjamshaid.123@gmail.com'
})


st.sidebar.image("images/maaz.jpg", use_column_width=True)


st.sidebar.code("maazjamshaid.123@gmail.com", language="bash")
st.sidebar.code("+923095183754", language="bash")

st.sidebar.markdown("---")

PAGE_DICT = {
    "HOME 🏠": show_intro,
    "PROJECTS 🦾": show_projects,
}
page = st.sidebar.selectbox("Get Started", PAGE_DICT)

st.sidebar.markdown("---")

st.sidebar.caption("©️MaazJamshaid")

#***********************************************************************************************

if page == "HOME 🏠": 
    show_intro()

#***********************************************************************************************

elif page == "PROJECTS 🦾": 
    show_projects()