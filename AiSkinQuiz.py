import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# Set Streamlit page layout
st.set_page_config(layout="wide", page_title='Skincare AI', page_icon='🌿')

# Load and display logo in sidebar
st.sidebar.image("skincare_logo.png", width=150)

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"  # Replace with your email
SENDER_PASSWORD = "your_app_password"  # Use App Password

# AI-Powered Skincare Analysis Function
def analyze_skin(skin_type, concerns, age, lifestyle):
    recommendations = {
        "Dry": ["Hydrating cleanser", "Moisturizing cream", "Hyaluronic acid serum"],
        "Oily": ["Oil-free cleanser", "Mattifying moisturizer", "Salicylic acid serum"],
        "Combination": ["Balanced face wash", "Lightweight moisturizer", "Niacinamide serum"],
        "Sensitive": ["Gentle cleanser", "Soothing moisturizer", "Aloe vera gel"],
    }
    
    lifestyle_factor = "Drink more water and maintain a balanced diet." if lifestyle else "Consider incorporating more hydration and vitamins into your routine."
    suggested_products = recommendations.get(skin_type, ["Consult a dermatologist for a specialized routine."])
    return suggested_products, lifestyle_factor

# Function to send email
def send_email(user_email, skin_type, recommendations, lifestyle_advice):
    try:
        subject = "Your Personalized Skincare Routine"
        body = f"""
        Hello,

        Based on your skin type ({skin_type}), here are some recommended skincare products:
        {', '.join(recommendations)}

        Additional Advice:
        {lifestyle_advice}

        Stay radiant!
        """
        
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = user_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, user_email, msg.as_string())
        server.quit()
        
        st.success("✅ Skincare recommendation sent successfully!")
    except Exception as e:
        st.error(f"❌ Error sending email: {e}")

# Skincare Input Form
st.subheader("AI-Powered Skincare Analysis")
skin_type = st.selectbox("Select Your Skin Type:", ["Dry", "Oily", "Combination", "Sensitive"])
skin_concerns = st.multiselect("Select Your Skin Concerns:", ["Acne", "Wrinkles", "Pigmentation", "Redness", "Dark Circles"])
age = st.slider("Select Your Age:", 15, 70, 25)
lifestyle = st.checkbox("Do you maintain a healthy diet & hydration?")
user_email = st.text_input("Enter your Email to receive personalized skincare routine:")

# Generate AI Recommendations
if st.button("Analyze Skin & Get Recommendations"):
    recommendations, lifestyle_advice = analyze_skin(skin_type, skin_concerns, age, lifestyle)
    st.write("### Recommended Skincare Products:")
    st.write(recommendations)
    st.write("### Additional Advice:")
    st.write(lifestyle_advice)
    
    # Send email if provided
    if user_email:
        send_email(user_email, skin_type, recommendations, lifestyle_advice)

# Footer with Copyright & Branding
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 14px; color: gray;'>
         © 2025 Skincare AI. All rights reserved.
    </p>
    """,
    unsafe_allow_html=True
)
