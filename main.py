import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# Page configuration
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Custom CSS
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(37, 99, 235, 0.10), transparent 25%),
            radial-gradient(circle at 90% 20%, rgba(168, 85, 247, 0.10), transparent 25%),
            linear-gradient(135deg, #f8fafc 0%, #eef2ff 50%, #f8fafc 100%);
    }

    /* Remove default top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero section */
    .hero {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #1e3a8a 50%,
            #312e81 100%
        );
        padding: 42px 45px;
        border-radius: 24px;
        margin-bottom: 30px;
        box-shadow: 0 15px 45px rgba(15, 23, 42, 0.20);
        position: relative;
        overflow: hidden;
    }

    .hero:before {
        content: "";
        position: absolute;
        width: 260px;
        height: 260px;
        background: rgba(255,255,255,0.07);
        border-radius: 50%;
        right: -70px;
        top: -100px;
    }

    .hero:after {
        content: "";
        position: absolute;
        width: 180px;
        height: 180px;
        background: rgba(96,165,250,0.12);
        border-radius: 50%;
        left: -60px;
        bottom: -100px;
    }

    .hero-content {
        position: relative;
        z-index: 2;
    }

    .hero-icon {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .hero-title {
        color: white;
        font-size: 38px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        color: #cbd5e1;
        font-size: 17px;
        margin-top: 10px;
        line-height: 1.6;
    }

    .badge {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        color: #e0e7ff;
        padding: 7px 14px;
        border-radius: 50px;
        font-size: 13px;
        margin-top: 15px;
    }

    /* Section title */
    .section-title {
        font-size: 23px;
        font-weight: 750;
        color: #0f172a;
        margin: 10px 0 18px 2px;
    }

    .section-description {
        color: #64748b;
        font-size: 14px;
        margin-top: -10px;
        margin-bottom: 20px;
    }

    /* Select boxes */
    div[data-baseweb="select"] > div {
        border-radius: 13px !important;
        border: 1px solid #dbe3ef !important;
        background: white !important;
        min-height: 50px !important;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
        transition: all 0.2s ease;
    }

    div[data-baseweb="select"] > div:hover {
        border-color: #6366f1 !important;
        box-shadow: 0 5px 18px rgba(99, 102, 241, 0.12);
    }

    label {
        font-weight: 650 !important;
        color: #334155 !important;
        font-size: 14px !important;
    }

    /* Generate button */
    .stButton > button {
        width: 100%;
        height: 56px;
        border-radius: 14px;
        border: none;
        background: linear-gradient(135deg, #2563eb, #4f46e5);
        color: white;
        font-size: 17px;
        font-weight: 750;
        letter-spacing: 0.2px;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.25);
        transition: all 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(37, 99, 235, 0.32);
        background: linear-gradient(135deg, #1d4ed8, #4338ca);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    /* Result card */
    .result-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
        padding: 18px 22px;
        border-radius: 16px 16px 0 0;
        margin-top: 28px;
    }

    .result-title {
        font-size: 18px;
        font-weight: 750;
    }

    .result-badge {
        background: #22c55e;
        color: white;
        padding: 5px 12px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 700;
    }

    .result-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-top: none;
        border-radius: 0 0 16px 16px;
        padding: 26px;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
        color: #1e293b;
        line-height: 1.8;
        font-size: 16px;
        white-space: pre-wrap;
    }

    /* Info cards */
    .info-card {
        background: rgba(255,255,255,0.75);
        border: 1px solid rgba(226,232,240,0.9);
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(15,23,42,0.05);
    }

    .info-icon {
        font-size: 28px;
    }

    .info-title {
        color: #0f172a;
        font-weight: 700;
        margin-top: 8px;
    }

    .info-text {
        color: #64748b;
        font-size: 13px;
        margin-top: 4px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 45px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
    }

</style>
""", unsafe_allow_html=True)


# Main app layout
def main():

    # Hero
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <div class="hero-icon">💼</div>
            <div class="hero-title">LinkedIn Post Generator</div>
            <div class="hero-subtitle">
                Create professional, engaging and personalized LinkedIn posts
                with the power of AI.
            </div>
            <div class="badge">
                ✨ AI-Powered Content Creation
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


    # Section heading
    st.markdown(
        '<div class="section-title">Create Your LinkedIn Post</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Choose your topic, preferred post length and language to generate your post.'
        '</div>',
        unsafe_allow_html=True
    )


    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3, gap="large")

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        selected_tag = st.selectbox(
            "🏷️ Topic",
            options=tags
        )

    with col2:
        selected_length = st.selectbox(
            "📏 Length",
            options=length_options
        )

    with col3:
        selected_language = st.selectbox(
            "🌐 Language",
            options=language_options
        )


    # Spacing
    st.markdown("<br>", unsafe_allow_html=True)


    # Generate Button
    if st.button("✨ Generate LinkedIn Post", use_container_width=True):

        with st.spinner("🤖 Creating your LinkedIn post..."):

            post = generate_post(
                selected_length,
                selected_language,
                selected_tag
            )

        st.markdown("""
        <div class="result-header">
            <div class="result-title">📝 Generated LinkedIn Post</div>
            <div class="result-badge">✓ Ready</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            f'<div class="result-card">{post}</div>',
            unsafe_allow_html=True
        )


    # Feature cards
    st.markdown("<br><br>", unsafe_allow_html=True)

    feature1, feature2, feature3 = st.columns(3, gap="large")

    with feature1:
        st.markdown("""
        <div class="info-card">
            <div class="info-icon">🎯</div>
            <div class="info-title">Personalized</div>
            <div class="info-text">
                Generate content based on your selected topic.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with feature2:
        st.markdown("""
        <div class="info-card">
            <div class="info-icon">⚡</div>
            <div class="info-title">AI Powered</div>
            <div class="info-text">
                Create engaging posts quickly using AI.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with feature3:
        st.markdown("""
        <div class="info-card">
            <div class="info-icon">🌍</div>
            <div class="info-title">Multiple Languages</div>
            <div class="info-text">
                Generate posts in English or Hinglish.
            </div>
        </div>
        """, unsafe_allow_html=True)


    # Footer
    st.markdown("""
    <div class="footer">
        LinkedIn Post Generator • AI Content Creation Platform
        <br>
        Built with Python, Streamlit & LangChain
    </div>
    """, unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    main()