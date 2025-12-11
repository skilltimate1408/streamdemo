import streamlit as st

# ---- USER DATABASE (Replace with real DB in production) ----
USER_CREDENTIALS = {
    "admin": "1234",
    "user": "pass"
}

# ---- SESSION STATE INITIALIZATION ----
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# ---- LOGIN FUNCTION ----
def login(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Logged in successfully!")
    else:
        st.error("Invalid username or password")

# ---- LOGOUT FUNCTION ----
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""

# ---- LOGIN PAGE UI ----
def login_page():
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        login(username, password)

# ---- MAIN APP CONTENT (after login) ----
def main_app():
    st.title("🎉 Welcome!")
    st.write(f"Hello, **{st.session_state.username}** 👋")

    if st.button("Logout"):
        logout()

# ---- PAGE ROUTER ----
if st.session_state.logged_in:
    main_app()
else:
    login_page()
