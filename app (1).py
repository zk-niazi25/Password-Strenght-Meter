import streamlit as st
import re
import random
import string

# Initialize session state for password history
if "password_history" not in st.session_state:
    st.session_state.password_history = []

# Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟠 Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🟠 Include at least one digit (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🟠 Include at least one special character (!@#$%^&*).")
    
    common_words = ["password", "123456", "qwerty", "admin", "letmein"]
    if any(word in password.lower() for word in common_words):
        score -= 1
        feedback.append("⚠️ Avoid using common words or sequences.")
    
    strength = "🔴 Weak" if score <= 2 else "🟠 Moderate" if score <= 4 else "🟢 Strong"
    return strength, feedback

# Password Generator
def generate_password(length=12, include_specials=True):
    chars = string.ascii_letters + string.digits + ("!@#$%^&*" if include_specials else "")
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit UI Customization
st.set_page_config(page_title="🔐 SecurePass Manager", page_icon="🔑", layout="centered")

st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #1abc9c, #3498db);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .main-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background: #2c3e50;
            border-radius: 10px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
        h1 {
            color: #f1c40f;
        }
        .stButton>button {
            background-color: #e74c3c;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 1rem;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #c0392b;
            transform: scale(1.05);
        }
        .password-box {
            background: rgba(255, 255, 255, 0.2);
            padding: 10px;
            border-radius: 5px;
            font-size: 1.2rem;
            text-align: center;
            margin: 10px 0;
        }
        .sidebar-content {
            background: #34495e;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("🔒 SecurePass Manager")
st.write("Check the strength of your password and generate secure passwords.")

# Sidebar Enhancements
st.sidebar.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
st.sidebar.header("🔍 Password Security Tips")
st.sidebar.write("- Use at least 12 characters.")
st.sidebar.write("- Mix uppercase and lowercase letters.")
st.sidebar.write("- Include numbers and special characters.")
st.sidebar.write("- Avoid common words or sequences.")
st.sidebar.write("- Enable Two-Factor Authentication (2FA).")
st.sidebar.markdown('</div>', unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
st.sidebar.header("🌟 Extra Features")
st.sidebar.write("📋 Copy password to clipboard.")
st.sidebar.write("📏 Customize password length.")
st.sidebar.write("🔧 Include/exclude special characters.")
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Password Strength Checker
st.header("🔍 Check Password Strength")
password = st.text_input("Enter your password", type="password")
if st.button("Check Strength"):
    if password:
        strength, feedback = check_password_strength(password)
        st.subheader(f"**Password Strength:** {strength}")
        for tip in feedback:
            st.warning(tip)
    else:
        st.error("❌ Please enter a password!")

# Password Generator
st.header("🔑 Generate a Strong Password")
length = st.slider("Select Password Length", min_value=8, max_value=30, value=12)
include_specials = st.checkbox("Include Special Characters", value=True)
if st.button("Generate Password"):
    new_password = generate_password(length, include_specials)
    st.session_state.password_history.append(new_password)
    st.markdown(f'<div class="password-box">{new_password}</div>', unsafe_allow_html=True)
    st.success("✅ Password generated!")

st.markdown('</div>', unsafe_allow_html=True)
