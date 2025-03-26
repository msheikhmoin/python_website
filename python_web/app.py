import streamlit as st
import base64
import os

st.set_page_config(page_title="My Website", layout="wide")

def get_base64(file_path):
    """Convert file to base64 string"""
    if not os.path.exists(file_path):
        st.error(f"⚠️ Error: File not found - {file_path}")
        return None
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Corrected GIF path (direct inside "python_web" folder)
gif_path = os.path.join(os.path.dirname(__file__), "python.gif")

if os.path.exists(gif_path):
    gif_base64 = get_base64(gif_path)
    background_style = f'background: url("data:image/gif;base64,{gif_base64}") no-repeat center center fixed; background-size: cover;' if gif_base64 else 'background: #000000;'
else:
    st.warning("⚠️ Background image not found, using fallback.")
    background_style = 'background: url("https://raw.githubusercontent.com/msheikhmoin/python_website/main/python_web/python.gif") no-repeat center center fixed; background-size: cover;'  # Replace with actual GitHub URL

st.markdown(
    f"""
    <style>
        html, body, [data-testid="stAppViewContainer"] {{
            {background_style}
            font-family: 'Raleway', sans-serif;
            color: white;
            text-align: center;
            height: 100vh;
        }}
        .title {{
            font-size: 55px;
            font-weight: bold;
            background: linear-gradient(90deg, #00C9FF, #92FE9D, #F72585, #FFB703);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 3px 3px 15px rgba(0, 0, 0, 0.7);
            margin-top: 20px;
            padding: 10px;
            border-radius: 10px;
            animation: glow 3s infinite alternate;
        }}
        @keyframes glow {{
            0% {{ text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.6); }}
            100% {{ text-shadow: 0px 0px 20px rgba(255, 255, 255, 1); }}
        }}
        .footer {{
            text-align: center;
            font-size: 16px;
            margin-top: 40px;
            padding: 12px;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
        }}
        .footer-text {{
            font-size: 18px;
            font-weight: bold;
            background: linear-gradient(90deg, #FF5733, #FFC300, #00C9FF, #92FE9D);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">🔥 Welcome to My Stylish Website 🔥</h1>', unsafe_allow_html=True)

st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About", "Contact", "Features"])

if page == "Home":
    st.subheader("🏡 Home Page")
    st.write("Welcome to my **modern and interactive** Streamlit-based website! 🚀")
elif page == "About":
    st.subheader("ℹ️ About Page")
    st.write("This website is designed with **advanced UI styling** and built using **Python & Streamlit**.")
elif page == "Features":
    st.subheader("🔥 Features")
    st.write("- 🏆 **Fully Responsive Design**")
    st.write("- 🎨 **Custom Gradient Background**")
    st.write("- 🚀 **Interactive Sidebar Navigation**")
    st.write("- 🎭 **Smooth Hover Effects**")
elif page == "Contact":
    st.subheader("📩 Contact Me")
    name = st.text_input("Your Name")
    message = st.text_area("Your Message")
    if st.button("Send"):
        st.success(f"✅ Thank you, {name}! Your message has been received.")

st.markdown('<div class="footer"><span class="footer-text">Built with ❤️ by Moin Sheikh</span></div>', unsafe_allow_html=True)
