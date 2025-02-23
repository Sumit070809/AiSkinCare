import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import random

# Set page title and layout
st.set_page_config(layout="wide", page_title='AI Skin Quiz', page_icon='🧴')
st.title("🌿 AI-Powered Skin & Supplement Quiz")
st.write("Answer a few questions and get personalized skincare & supplement recommendations!")

# Sidebar with image
st.sidebar.image("skincare_logo.png", width=120)
st.sidebar.header("Your Personalized Skin Analysis")

# Step 1: Collect User Input
st.subheader("1️⃣ Tell us about your skin")
skin_type = st.selectbox("What is your skin type?", ["Oily", "Dry", "Combination", "Sensitive"])
skin_concern = st.multiselect("What are your primary skin concerns?", ["Acne", "Aging", "Pigmentation", "Dryness", "Dullness"])

# Step 2: Lifestyle Factors
st.subheader("2️⃣ Your Lifestyle & Habits")
sleep_hours = st.slider("How many hours do you sleep per night?", 4, 10, 7)
water_intake = st.slider("How much water do you drink daily? (Liters)", 0.5, 5.0, 2.0)
stress_level = st.radio("How stressed do you feel on a scale of 1-5?", [1, 2, 3, 4, 5])

diet = st.selectbox("What best describes your diet?", ["Balanced", "Vegan", "High Protein", "Keto", "High Sugar"])

# Step 3: Allergies & Sensitivities
st.subheader("3️⃣ Any Ingredient Allergies?")
allergies = st.text_area("List any ingredients you are allergic to (e.g., Retinol, Fragrances, Sulfates)")

# Step 4: Optional AI Skin Scan
st.subheader("4️⃣ Upload a Photo for AI Skin Analysis (Optional)")
skin_image = st.file_uploader("Upload a clear image of your face", type=["jpg", "png", "jpeg"])

if skin_image is not None:
    st.image(skin_image, caption="Uploaded Image", width=200)
    st.success("✅ AI Skin Analysis in Progress...")
    # Placeholder for AI model integration
    ai_skin_analysis = random.choice(["Signs of Dryness Detected", "Mild Acne Detected", "Good Skin Health"])
    st.write("🔍 **AI Analysis Result:**", ai_skin_analysis)

# Step 5: Personalized Recommendations
st.subheader("💡 Your Personalized Skincare & Supplement Plan")
recommendations = []

if "Acne" in skin_concern:
    recommendations.append("✔ Use Salicylic Acid-based products to fight acne.")
    recommendations.append("✔ Take Zinc supplements to reduce inflammation.")
if "Aging" in skin_concern:
    recommendations.append("✔ Use Retinol and Vitamin C serums for anti-aging.")
    recommendations.append("✔ Try Collagen peptides for better skin elasticity.")
if "Pigmentation" in skin_concern:
    recommendations.append("✔ Use Niacinamide and SPF daily to reduce dark spots.")
if "Dryness" in skin_concern:
    recommendations.append("✔ Use Hyaluronic Acid for deep hydration.")
    recommendations.append("✔ Omega-3 supplements can help retain moisture.")
if water_intake < 2.0:
    recommendations.append("⚠ Drink more water to improve skin hydration!")
if sleep_hours < 6:
    recommendations.append("⚠ Poor sleep affects your skin. Aim for 7-8 hours!")
if stress_level > 3:
    recommendations.append("✔ Try Adaptogens like Ashwagandha to reduce stress.")

for rec in recommendations:
    st.write(rec)

st.success("📩 We will send a full report with recommendations to your email soon!")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 14px; color: gray;'>
         © 2025 SkinAI Inc. All rights reserved.
    </p>
    """, unsafe_allow_html=True)
