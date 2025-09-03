import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="InstaPitch", page_icon="🚀", layout="centered")

# --- Styling (No background box) ---
st.markdown("""
<style>
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        font-size: 16px;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #004c99;
    }
</style>
""", unsafe_allow_html=True)

# --- App Header ---
st.markdown("<h1 style='text-align: center;'>🚀 InstaPitch</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Your Instant AI Startup Pitch Coach</p>", unsafe_allow_html=True)

# --- INPUT SECTION ---
with st.expander("📝 Step 1: Describe Your Startup Idea", expanded=True):
    problem = st.text_input("❌ Problem you're solving")
    solution = st.text_input("💡 Your solution")
    audience = st.text_input("👥 Target audience")
    business_model = st.text_input("💰 Business model")
    competitors = st.text_input("⚔️ Competitors (optional)")

# --- INVESTOR PERSONA ---
with st.expander("🎯 Step 2: Choose Investor Type", expanded=True):
    persona = st.selectbox(
        "Choose the investor type to pitch to:",
        ["Tech VC", "Social Impact Funder", "Angel Investor", "Shark Tank-style", "Government/Incubator"]
    )

# --- Generate Pitch Button ---
if st.button("✨ Generate My InstaPitch"):
    st.markdown("----")
    
    st.subheader("🎙️ Elevator Pitch")
    st.markdown(f"""
    **Hook:** {problem or '*[Please enter the problem]*'}  
    **Solution:** {solution or '*[Please enter the solution]*'}  
    **Target Audience:** {audience or '*[Please enter target audience]*'}  
    **Business Model:** {business_model or '*[Please enter business model]*'}  
    **Competitors:** {competitors if competitors else '*No competitors listed.*'}  
    **Tailored for:** {persona}
    """)

    st.subheader("🤔 Likely Investor Questions")
    investor_questions = [
        f"1. What makes your solution unique for {audience or 'your users'}?",
        f"2. How do you plan to generate revenue via {business_model or 'your business model'}?",
        "3. What's your go-to-market strategy?",
        "4. How scalable is your idea?",
        f"5. Why should a {persona} invest in you?"
    ]
    for q in investor_questions:
        st.markdown(f"🔹 {q}")

    st.success("✅ Your pitch is ready! Refine your content based on the questions above.")