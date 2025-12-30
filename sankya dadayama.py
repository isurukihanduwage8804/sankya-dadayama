import streamlit as st
import random
import time

# පිටුවේ සැකසුම්
st.set_page_config(page_title="සංඛ්‍යා දඩයම - Number Hunt", page_icon="🎯", layout="centered")

# CSS - Animation සහ පාවෙන පිළිතුරු සඳහා
st.markdown("""
    <style>
    @keyframes float {
        0% { transform: translate(0, 0); }
        25% { transform: translate(200px, 50px); }
        50% { transform: translate(-150px, 150px); }
        75% { transform: translate(100px, -100px); }
        100% { transform: translate(0, 0); }
    }
    .stButton > button {
        background-color: #ff4b4b;
        color: white;
        font-size: 30px !important;
        font-weight: bold;
        border-radius: 50%;
        width: 120px;
        height: 120px;
        animation: float 5s infinite alternate ease-in-out;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        border: 4px solid white;
    }
    .q-text {
        font-size: 50px !important;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# ප්‍රශ්න 20ක් නිර්මාණය කිරීම
def get_game_questions():
    questions = []
    for i in range(1, 21):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        questions.append({"q": f"{a} + {b} = ?", "ans": str(a + b)})
    return questions

# Session State
if 'game_data' not in st.session_state:
    st.session_state.game_data = get_game_questions()
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.show_ans = False

st.markdown("<h1 style='text-align: center;'>🎯 සංඛ්‍යා දඩයම (Number Hunt)</h1>", unsafe_allow_html=True)

if st.session_state.idx < 20:
    q = st.session_state.game_data[st.session_state.idx]
    
    st.markdown(f"<div class='q-text'>{q['q']}</div>", unsafe_allow_html=True)
    
    # ප්‍රශ්නය පෙන්වා තත්පර 1කට පසු පිළිතුර පෙන්වයි
    if not st.session_state.show_ans:
        time.sleep(1)
        st.session_state.show_ans = True
        st.rerun()

    if st.session_state.show_ans:
        st.write("### පිළිතුර පාවෙමින් පවතී... ඉක්මනින් එය අල්ලන්න!")
        
        # පිළිතුර සහිත පාවෙන බොත්තම
        if st.button(q['ans']):
            st.session_state.score += 1
            st.session_state.idx += 1
            st.session_state.show_ans = False
            st.success("නියමයි! ඔබට ලකුණක් ලැබුණා.")
            time.sleep(1)
            st.rerun()
            
    st.progress((st.session_state.idx) / 20)
    st.write(f"ලකුණු: {st.session_state.score} | ප්‍රශ්න: {st.session_state.idx + 1}/20")

else:
    st.balloons()
    st.markdown(f"<h1 style='text-align:center;'>ක්‍රීඩාව අවසන්! 🎉</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;'>ඔබේ දඩයමේ ලකුණු: {st.session_state.score} / 20</h2>", unsafe_allow_html=True)
    
    if st.button("නැවත සෙල්ලම් කරන්න"):
        st.session_state.game_data = get_game_questions()
        st.session_state.idx = 0
        st.session_state.score = 0
        st.session_state.show_ans = False
        st.rerun()
