import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="AutoResume Gen", layout="centered", initial_sidebar_state="auto")

# Injecting custom CSS for modern light theme
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
        color: #212529;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        background-color: #ffffff;
        color: #000000;
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #ced4da;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✨AutoResume Gen")
st.markdown("Craft a beautiful resume step by step with ease.")

# Session state to store user input and current step
if "step" not in st.session_state:
    st.session_state.step = 1

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

# Step 1: Personal Information
if st.session_state.step == 1:
    st.header("Personal Information")
    st.session_state.name = st.text_input("Full Name")
    st.session_state.email = st.text_input("Email")
    st.session_state.phone = st.text_input("Phone Number")
    if st.button("Next ➡"):
        next_step()

elif st.session_state.step == 2:
    st.header("Profile Summary")
    st.session_state.profile = st.text_area("Write a brief summary about yourself")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            prev_step()
    with col2:
        if st.button("Next ➡"):
            next_step()

elif st.session_state.step == 3:
    st.header("Education")
    st.session_state.college = st.text_input("College/University Name")
    st.session_state.degree = st.text_input("Degree")
    st.session_state.education_year = st.text_input("Year of Graduation")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            prev_step()
    with col2:
        if st.button("Next ➡"):
            next_step()

elif st.session_state.step == 4:
    st.header("Skills")
    st.session_state.skills = st.text_area("List your skills (comma-separated)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            prev_step()
    with col2:
        if st.button("Next ➡"):
            next_step()

elif st.session_state.step == 5:
    st.header("Experience")
    st.session_state.experience = st.text_area("Describe your experience (projects, internships, jobs)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            prev_step()
    with col2:
        if st.button("Next ➡"):
            next_step()

elif st.session_state.step == 6:
    st.header("Hobbies & Interests")
    st.session_state.hobbies = st.text_area("Your hobbies/interests (comma-separated)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            prev_step()
    with col2:
        if st.button("Next ➡"):
            next_step()

elif st.session_state.step == 7:
    st.header("Preview & Download Resume")

    st.markdown(f"""
    **Name:** {st.session_state.name}  
    **Email:** {st.session_state.email}  
    **Phone:** {st.session_state.phone}  

    ---
    **Profile Summary:**  
    {st.session_state.profile}  

    ---
    **Education:**  
    {st.session_state.degree}, {st.session_state.college} ({st.session_state.education_year})  

    ---
    **Skills:** {st.session_state.skills}  

    ---
    **Experience:**  
    {st.session_state.experience}  

    ---
    **Hobbies:** {st.session_state.hobbies}
    """)

    if st.button("⬅ Back"):
        prev_step()

    if st.button("Download Resume as PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.set_fill_color(245, 245, 245)
        pdf.rect(0, 0, 210, 30, 'F')
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", 'B', 20)
        pdf.set_xy(10, 10)
        pdf.cell(190, 10, st.session_state.name, ln=True, align='C')

        pdf.set_font("Arial", size=12)
        pdf.set_xy(10, 18)
        pdf.cell(190, 10, f"{st.session_state.email} | {st.session_state.phone}", ln=True, align='C')

        def section_title(title):
            pdf.set_font("Arial", 'B', 14)
            pdf.ln(10)
            pdf.cell(0, 10, title, ln=True)
            y = pdf.get_y()
            pdf.line(10, y, 200, y)
            pdf.ln(2)

        def add_text(text):
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, text)
            pdf.ln(1)

        section_title("Profile Summary")
        add_text(st.session_state.profile)

        section_title("Education")
        add_text(f"{st.session_state.degree}\n{st.session_state.college} ({st.session_state.education_year})")

        section_title("Experience")
        add_text(st.session_state.experience)

        section_title("Skills")
        skills_list = [s.strip() for s in st.session_state.skills.split(",")]
        add_text(" | ".join(skills_list))

        section_title("Hobbies")
        hobbies_list = [h.strip() for h in st.session_state.hobbies.split(",")]
        add_text(" | ".join(hobbies_list))

        pdf_output = pdf.output(dest="S").encode("latin-1")

        st.download_button(
            label="Download Resume (Styled)",
            data=pdf_output,
            file_name="Styled_Resume.pdf",
            mime="application/pdf"
        )
