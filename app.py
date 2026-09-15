import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Venkateshwaran A | Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .hero-btn {
        display: inline-block;
        padding: 0.5em 1em;
        color: #FFFFFF;
        background-color: #1E1E1E;
        border: 1px solid #4CAF50;
        border-radius: 5px;
        text-decoration: none;
        margin-right: 10px;
        margin-bottom: 10px;
        text-align: center;
        transition: 0.3s;
    }
    .hero-btn:hover {
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([2.5, 1])
with col1:
    st.title("Hi, I'm Venkateshwaran A 👋")
    st.subheader("Data Analyst | Python | SQL")
    st.write("Turning data into actionable insights through SQL, Python, EDA, visualization, and machine learning.")
    
    # Links
    st.markdown("""
        <a href="#projects" class="hero-btn">View Projects</a>
        <a href="https://github.com/vw636029-prog" target="_blank" class="hero-btn">GitHub</a>
        <a href="https://www.linkedin.com/in/venkateshwaran-akilandeshwaran-481419422/" target="_blank" class="hero-btn">LinkedIn</a>
    """, unsafe_allow_html=True)
    
    # Resume Download Button (Native Streamlit)
    try:
        with open("resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume",
                data=pdf_file,
                file_name="Venkateshwaran_A_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("⚠️ Resume file not found. Please add 'resume.pdf' to your folder.")

with col2:
    try:
        st.image("profile.jpeg", width=150) # Replace with your image file
    except FileNotFoundError:
        st.info("📷 Place 'profile.jpeg' in your folder to see it here.")

st.write("---")

# --- QUICK STATS ---
stat1, stat2, stat3, stat4 = st.columns(4)
stat1.metric("Major Projects", "2")
stat2.metric("ML Models Compared", "5")
stat3.metric("Best Test Accuracy", "92%")
stat4.metric(label="Education", value="BCA", delta="2023–2026", delta_color="off")

st.write("---")

# --- ABOUT ME & WHAT I DO ---
col_about, col_do = st.columns([1.5, 1])
with col_about:
    st.header("👤 About Me")
    st.write("""
    I am a BCA graduate with hands-on experience in SQL, Python, data analysis, exploratory data analysis, visualization, and machine learning. 
    I enjoy transforming raw data into meaningful insights and building practical analytical solutions. I have worked on SQL analytics and student churn prediction projects.
    """)

with col_do:
    st.header("🎯 What I Do")
    st.write("📊 **Analyze:** Clean, explore and interpret datasets.")
    st.write("💡 **Discover:** Identify patterns and generate business insights.")
    st.write("🤖 **Predict:** Build classification and predictive models.")
    st.write("📈 **Present:** Create dashboards and communicate findings.")

st.write("---")

# --- SKILLS ---
st.header("🛠️ Skills")
s1, s2, s3 = st.columns(3)
with s1:
    st.write("**🐍 Programming:** Python")
    st.write("**🗄️ Database:** SQL, MySQL")
with s2:
    st.write("**📊 Data Analysis:** Pandas, NumPy, EDA")
    st.write("**📈 Visualization:** Matplotlib, Seaborn, Plotly")
with s3:
    st.write("**🤖 Machine Learning:** Scikit-learn, Logistic Regression, Decision Tree, Random Forest, KNN, SVM")
    st.write("**🛠️ Tools:** Excel, Streamlit, Git/GitHub")

st.write("---")

# --- PROJECTS ---
st.markdown("<h2 id='projects'>🚀 Projects</h2>", unsafe_allow_html=True)

# Project 1
st.subheader("🎓 Student Churn Analysis & Risk Prediction Dashboard")
st.caption("Python | Streamlit | Pandas | Scikit-learn | Plotly")
st.write("Interactive dashboard for analyzing student data, performing EDA, comparing classification models, and identifying churn risk with rule-based counselor recommendations.")
st.write("Here are some of the example datasets and visualization from the project. You can use the dataset from the github link to run the project or use your own dataset with the same structure to run the project.")

# Project 1 Images (Columns)
img1, img2, img3 = st.columns(3)
with img1:
    st.markdown("**Dataset Overview**<br>250 rows | 12 cols | 0 duplicates | 0 missing", unsafe_allow_html=True)
    st.image("churn_data.png", use_container_width=True)
    
with img2:
    st.markdown("**Model Comparison**<br>Logistic Reg: 92% | RF: 90% | KNN: 90%", unsafe_allow_html=True)
    st.image("churn_models.png", use_container_width=True)
    
with img3:
    st.markdown("**Risk Simulator**<br>Risk drivers & counselor recommendations", unsafe_allow_html=True)
    st.image("churn_risk.png", use_container_width=True)

# Project 2
st.subheader("🛒 E-Commerce Advanced Analytics & CLV Engine")
st.caption("MySQL | SQL | CTEs | Window Functions | RFM")
st.write("SQL-based e-commerce analytics project covering relational database design, RFM customer segmentation, purchase-cycle analysis, MAU, and revenue growth.")
st.markdown("[View on GitHub](https://github.com/vw636029-prog)")

st.write("---")

# --- EXPERIENCE & EDUCATION ---
col_exp, col_cert = st.columns(2)
with col_exp:
    st.header("💼 Experience")
    st.write("**Industrial Trainee — SUBZERO Technologies**")
    st.caption("May 2025 | Nov 2025 – Mar 2026")
    st.write("Contributed as an intern team member to an AI-powered financial fraud detection project, gaining hands-on experience in transaction data preprocessing, fraud prediction workflows, and web-based application development.")

with col_cert:
    st.header("🏆 Certifications")
    st.write("- **Oracle Certified Professional:** Oracle Autonomous Database Cloud")
    st.write("- **AWS Cloud Masterclass:** Cloud Practitioner Essentials")
    st.write("- **IBM IT & Cloud Fundamentals:** Coursera / IBM")

st.write("---")

# --- CONTACT ---
st.header("📫 Let's Connect")
st.write("Open to: **Entry-Level Data Analyst opportunities**")
st.write(f"📧 **Email:** venkateshwaran142005@gmail.com")
st.write(f"📱 **Phone:** 6379180684")
st.markdown("[🔗 **LinkedIn Profile**](https://www.linkedin.com/in/venkateshwaran-akilandeshwaran-481419422/)")
st.markdown("[💻 **GitHub Projects**](https://github.com/vw636029-prog)")

st.write("---")

# --- FOOTER ---
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Venkateshwaran A | Data Analyst | Python | SQL</p>", unsafe_allow_html=True)