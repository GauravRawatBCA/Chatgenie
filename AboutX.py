import streamlit as st
import re
import requests
WEBHOOK_URL="https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTY4MDYzNzA0MzI1MjY1NTUzMjUxMzMi_pc"
def is_valid_email(email):
    email_pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None

@st.dialog("Contact Me")
def show_contact_form():
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if not WEBHOOK_URL:
                st.error(
                    "Email service is not set up. Please try again later.",icon="📧"
                )
                st.stop()
                
            if not name:
                st.error("Please provide your name.",icon="🧑")
                st.stop()
            
            if not email:
                st.error("Please provide your email address.",icon="✉️")
                st.stop()
            
            if not is_valid_email(email):
                st.error("Please provide your valid email address.",icon="📧")
                st.stop()
            
            if not message:
                st.error("Please provide a message.",icon="💬")
                st.stop()
                
            data={"email":email,"name":name,"message":message}
            response=requests.post(WEBHOOK_URL,json=data) 
            
            if response.status_code == 200:
                st.success("Your message has been sent successfully! 🎉",icon="🤩")
            else:
                st.error("There was an error sending your message.",icon="😨")
  
    
# --- Hero Section ---
col1,col2=st.columns(2,gap="small",vertical_alignment="center")
with col1:
    st.image(r"C:\Users\mk\OneDrive\Desktop\rawat.png",width=230)
with col2:
    st.title("Gaurav Rawat",anchor=False)
    st.write(
        "Data Analyst, assisting enterprises by supporting data-driven decision-making"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()
    
    
# --- Experience and qualification ---
st.write("\n")
st.subheader("Experience & Qualifications",divider="rainbow",anchor=False)
st.write(
    """
    - Experienced in extracting actionable insights from data
    - Strong knowledge in python and Excel
    - Good Understanding of statistical principles
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- Skills ---
st.write("\n")
st.subheader("Hard Skills",divider="rainbow",anchor=False)
st.write(
    """
    - Programming: Python (numpy, pandas, scikit-learn), SQL, VBA
    - Data Visualization: Power BI, Ms Excel, Plotly, Tableau
    - Modelling: Logistic regression, linear regression
    - Databases: MySQL, MS-SQL, MongoDB
    """
)