import streamlit as st
from datetime import date

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="centered"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
body {
    background-color: #eef2f7;
}
.main {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
}
h1 {
    text-align: center;
    color: #2c3e50;
}
.stButton>button {
    background-color: #6c63ff;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.result {
    background-color: #f0f4ff;
    padding: 20px;
    border-radius: 12px;
    font-size: 20px;
    color: #2c3e50;
    text-align: center;
    margin-top: 20px;
}
.footer {
    text-align: center;
    color: gray;
    margin-top: 30px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.markdown("<h1>🎂 Age Calculator</h1>", unsafe_allow_html=True)
st.write("Select your **Date of Birth** and calculate your exact age.")

# -------------------- INPUT --------------------
dob = st.date_input(
    "📅 Select your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

# -------------------- CALCULATION --------------------
if st.button("Calculate Age 🎉"):
    today = date.today()

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        days += 30

    if months < 0:
        years -= 1
        months += 12

    st.markdown(
        f"""
        <div class="result">
            🎈 You are <br><br>
            <b>{years}</b> Years  
            <b>{months}</b> Months  
            <b>{days}</b> Days old
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- FOOTER --------------------
st.markdown(
    "<div class='footer'>Made with ❤️ using Streamlit</div>",
    unsafe_allow_html=True
)
