import streamlit as st
import random
import time

# Page Configuration
st.set_page_config(page_title="සංඛ්‍යා දඩයම", page_icon="🎯", layout="wide")

# CSS - පිළිතුරු 4 වෙනස් වර්ණ සහ Animations සමඟ
st.markdown("""
    <style>
    /* පාවෙන Animations */
    @keyframes float1 { 0% {top: 15%; left: 10%;} 50% {top: 60%; left: 70%;} 100% {top: 15%; left: 10%;} }
    @keyframes float2 { 0% {top: 75%; left: 15%;} 50% {top: 25%; left: 80%;} 100% {top: 75%; left: 15%;} }
    @keyframes float3 { 0% {top: 20%; left: 75%;} 50% {top: 80%; left: 25%;} 100% {top: 20%; left: 75%;} }
    @keyframes float4 { 0% {top: 65%; left: 85%;} 50% {top: 15%; left: 15%;} 100% {top: 65%; left: 85%;} }

    /* බොත්තම් වල පොදු පෙනුම */
    .stButton > button {
        position: fixed;
        width: 140px;
        height: 140px;
        border-radius: 50%;
        font-size: 35px !important;
        font-weight: bold;
        color: white;
        border: 5px solid #ffffff;
        box-shadow: 0 12px 24px rgba(0,0,0,0.4);
        cursor: pointer;
        transition: transform 0.2s;
        z-index: 100;
    }

    /* පිළිතුරු 4 සඳහා වෙනස් වර්ණ 4 ක් */
    div.stButton:nth-child(1) > button { 
        animation: float1 9s infinite linear; 
        background-color: #FF5733 !important; /* තැඹිලි */
    }
    div.stButton:nth-child(2) > button { 
        animation: float2 7s infinite linear; 
        background-color: #2ECC71 !important; /* තද කොළ */
    }
    div.stButton:nth-child(3) > button { 
        animation: float3 11s infinite linear; 
        background-color: #3498DB !important; /* නිල් */
    }
    div.stButton:nth-child(4) > button { 
        animation: float4 8s infinite linear; 
        background-color: #9B59B6 !important; /* දම් */
    }

    .stButton > button:hover { transform: scale(1.2); border-color: yellow; }
    
    .q-display { 
        font-size: 70px !important; 
        font-weight: bold; 
        text-align: center; 
        margin-top: 30px; 
        color: #1e3799;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ගණිත ප්‍රශ්න සැකසීමේ function එක
def get_math_question():
    a = random.randint(1, 25)
    b = random.randint(1, 25)
    correct_val = a + b
    # වැරදි පිළිතුරු 3ක් තෝරා ගැනීම
    wrong_options = random.sample([i for i in range(2, 51) if i != correct_val], 3)
    all_options = wrong_options + [correct_val]
    random.shuffle(all_options)
    return {"q": f"{a} + {b} = ?", "options": all_options, "correct": str(correct_val)}

# ක්‍රීඩාවේ තත්ත්වය පවත්වා ගැනීම
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_count = 0
    st.session_state.current_q = get_math_question()

# ප්‍රශ්නය පෙන්වීම
st.markdown(f"<div class='q-display'>{st.session_state.current_q['q']}</div>", unsafe_allow_html=True)
st.write(f"## ⭐ ලකුණු: {st.session_state.score}  |  📝 ප්‍රශ්නය: {st.session_state.q_count + 1} / 20")

if st.session_state.q_count < 20:
    # පිළිතුරු 4 පාවෙන බොත්තම් ලෙස පෙන්වීම
    cols = st.columns(4)
    for i, val in enumerate(st.session_state.current_q['options']):
        with cols[i]:
            if st.button(str(val), key=f"hunt_{st.session_state.q_count}_{i}"):
                if str(val) == st.session_state.current_q['correct']:
                    st.session_state.score += 10
                    st.toast("නිවැරදියි! +10", icon="✅")
                else:
                    st.session_state.score -= 5
                    st.toast("වැරදියි! -5", icon="❌")
                
                # තත්පරයක විරාමයකින් පසු මීළඟ ප්‍රශ්නයට
                st.session_state.q_count += 1
                if st.session_state.q_count < 20:
                    st.session_state.current_q = get_math_question()
                st.rerun()
else:
    st.balloons()
    st.success("විශිෂ්ටයි! ඔබ ක්‍රීඩාව අවසන් කළා.")
    st.header(f"ඔබේ අවසන් ලකුණු සංඛ්‍යාව: {st.session_state.score}")
    if st.button("නැවත මුල සිට ආරම්භ කරන්න"):
        st.session_state.score = 0
        st.session_state.q_count = 0
        st.session_state.current_q = get_math_question()
        st.rerun()
