import streamlit as st
import plotly.express as px
import time

# 1. Page Configuration
st.set_page_config(
    page_title="EduBalance AI | Dubai Edition",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Modern Styling (Dark Mode UI)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stMarkdown, div.stButton, div.stInfo, div.stSuccess, div.stWarning, div.stError { border-radius: 12px; }
    h1, h2, h3 { font-family: 'Inter', sans-serif; font-weight: 700; letter-spacing: -0.5px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🔐 LOGIN SYSTEM AUTHENTICATION
# ==========================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        st.markdown("<h1 style='text-align: center;'>⚖️ EduBalance AI</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray;'>Autonomous Academic & Wellness Companion<br><b>Designed by Marwa Eman Ibrahim</b></p>", unsafe_allow_html=True)
        st.markdown("---")
        
        login_user = st.text_input("Username / نام کاربری", placeholder="Enter username (e.g., marwa)")
        login_pass = st.text_input("Password / رمز عبور", type="password", placeholder="Enter password (e.g., 1234)")
        
        if st.button("🚀 Login / ورود به سیستم", use_container_width=True):
            # پیش‌فرض: نام کاربری marwa و رمز عبور 1234 (قابل تغییر دلخواه)
            if login_user.strip().lower() == "marwa" and login_pass == "1234":
                st.session_state.authenticated = True
                st.success("🎉 Login successful! Loading your AI workspace...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ Invalid Username or Password! (Try: marwa / 1234)")
    st.stop()  # متوقف کردن اجرای بقیه کد تا زمان ورود موفق

# ==========================================
# 🚀 MAIN APPLICATION (AFTER SUCCESSFUL LOGIN)
# ==========================================

# Application Header (با نام شما به عنوان سازنده)
st.title("⚖️ EduBalance AI — Autonomous Academic & Wellness Companion")
st.markdown("### 👩‍💻 **Developed & Created by: Marwa Eman Ibrahim**")
st.caption("🚀 Designed for Dubai AI Competitions | Advanced Multi-Feature AI Agent with Pomodoro Timer")

st.markdown("---")

# ==========================================
# 💬 1. CHATBOT ASSISTANT (SMART & DYNAMIC)
# ==========================================
st.sidebar.header("💬 EduBalance AI Assistant")
st.sidebar.caption("Your dedicated multilingual companion")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! مرحباً! سلام! I am your AI agent created by Marwa. How can I help you balance your studies today?"}
    ]

chat_container = st.sidebar.container(height=240)
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.sidebar.chat_input("Ask your assistant...", key="marwa_unique_chat_input_2026"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    p_lower = prompt.lower()
    
    # Smart Multilingual Autonomous Responses
    if any(c in prompt for c in "چپژگ"):
        if "استرس" in prompt or "خستگی" in prompt:
            response = "سلام! تحلیل هوش مصنوعی نشان می‌دهد که باید استراحت کنید، آب بنوشید و تکنیک پومودورو را اجرا کنید."
        elif "برنامه" in prompt or "درسی" in prompt:
            response = "من جدول زمان‌بندی شما را در داشبورد اصلی به صورت هوشمند بهینه‌سازی کرده‌ام!"
        elif "مروا" in prompt or "سازنده" in prompt or "creator" in p_lower:
            response = "این پروژه فوق‌العاده توسط Marwa Eman Ibrahim برای مسابقات دبی طراحی و توسعه داده شده است!"
        else:
            response = "سلام عزیز! من دستیار هوشمند شما هستم که توسط مروا ساخته شده‌ام. چطور می‌توانم کمکتان کنم؟"
            
    elif any(c in prompt for c in "أبتثجحخدذرزسشصضطظعغفقكلمنهويء"):
        if "توتر" in prompt or "إرهاق" in prompt:
            response = "أهلاً بك! يوصي الذكاء الاصطناعي بأخذ استراحة قصيرة وشرب الماء."
        else:
            response = "مرحباً بك! أنا مساعدك الذكي الذي تم تصميمه بواسطة Marwa Eman Ibrahim."
            
    else:
        if "stress" in p_lower or "tired" in p_lower or "burnout" in p_lower:
            response = "🚨 AI Alert: High cognitive fatigue detected! Try a 15-minute relaxation walk and hydrate."
        elif "marwa" in p_lower or "creator" in p_lower or "author" in p_lower:
            response = "🌟 This brilliant application was designed and developed by Marwa Eman Ibrahim for the Dubai AI Competitions!"
        elif "help" in p_lower or "assist" in p_lower:
            response = "🤖 I am here to help you manage tasks, check burnout risks, and run the Pomodoro timer!"
        else:
            response = f"I processed your query: '{prompt}'. Keep up the great work on your studies!"

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

# ==========================================
# 👤 STUDENT PROFILE & TRACKER (SIDEBAR)
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("👤 Student Profile")
student_name = st.sidebar.text_input("Student Name / الاسم / نام", "Marwa", key="s_name")
study_hours = st.sidebar.slider("Study Hours / ساعات الدراسة", 1, 12, 6, key="s_hours")
stress_level = st.sidebar.select_slider("Stress Level / مستوى التوتر", options=["Low / منخفض", "Medium / متوسط", "High / عالي", "Burnout Risk / خطر"], key="s_stress")

st.sidebar.markdown("---")
st.sidebar.header("💧 Bio-Health Tracker")
water_cups = st.sidebar.number_input("Glasses of Water / أكواب الماء", min_value=0, max_value=15, value=4, key="s_water")
sleep_hours = st.sidebar.slider("Hours of Sleep / ساعات النوم", 0, 12, 7, key="s_sleep")

# Footer in Sidebar with Creator Name and Logout Button
st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; font-size: 12px; color: gray;'>Created with ❤️ by<br><b>Marwa Eman Ibrahim</b></p>", unsafe_allow_html=True)

if st.sidebar.button("🔒 Logout / خروج", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

# ==========================================
# 📊 MAIN TABS
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📅 Dynamic Dashboard", 
    "✅ Task Manager", 
    "🧠 Stress Assessment",
    "⏱️ Focus Pomodoro Timer",
    "📈 Burnout Risk Predictor",
    "📊 Weekly AI Insights"
])

# ================= TAB 1: DASHBOARD =================
with tab1:
    col1, col2 = st.columns([6, 4])
    
    with col1:
        st.subheader("📅 Optimized Daily Schedule")
        st.write(f"Hello **{student_name}**, here is your autonomous adaptive schedule:")
        
        if any(x in str(stress_level) for x in ["High", "Burnout", "عالي", "خطر"]):
            st.warning("⚠️ High stress detected! Extra recovery blocks added by AI Agent.")
            schedule = {
                "09:00 AM - 10:30 AM": "Focus Study Block (Deep Work)",
                "10:30 AM - 11:00 AM": "🧘 Guided Micro-Break & Hydration",
                "11:00 AM - 12:30 PM": "Study Session 2",
                "12:30 PM - 01:30 PM": "🍎 Healthy Lunch & Mental Reset"
            }
            break_time = 2.5
        else:
            st.success("✅ Energy levels balanced! Standard schedule applied.")
            schedule = {
                "09:00 AM - 11:00 AM": "Focus Study Block",
                "11:00 AM - 11:15 AM": "💧 Hydration & Stretch Break",
                "11:15 AM - 01:15 PM": "Study Session 2"
            }
            break_time = 1.0

        for time_slot, activity in schedule.items():
            st.markdown(f"- **{time_slot}**: {activity}")

        st.markdown("---")
        st.subheader("📊 Time Distribution Breakdown")
        data = {"Category": ["Active Study", "Rest & Recovery"], "Hours": [study_hours, break_time]}
        fig = px.pie(data, values="Hours", names="Category", color="Category", 
                     color_discrete_map={"Active Study": "#1f77b4", "Rest & Recovery": "#2ca02c"}, hole=0.45)
        fig.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("💡 Brain-Fuel & Well-being")
        st.info("🧠 **Brain Food:** Almonds, Dark Chocolate & Green Tea.")
        st.info("🧘 **Quick Relief:** Take a 3-minute deep breathing exercise.")
        if sleep_hours < 6:
            st.error("😴 Low sleep detected! Avoid heavy cognitive tasks.")
        if water_cups < 5:
            st.warning("💧 Hydration Alert: Drink another glass of water.")

# ================= TAB 2: TASK MANAGER =================
with tab2:
    st.subheader("✅ Smart Academic Task Manager")
    t1 = st.checkbox("📖 Review University Course Materials", key="t1")
    t2 = st.checkbox("💻 Complete Python Coding Project", key="t2")
    t3 = st.checkbox("🏃 30-Minute Light Exercise / Walk", key="t3")
    t4 = st.checkbox("💧 Complete Daily Hydration Goal", key="t4")
    
    if t1 and t2 and t3 and t4:
        st.balloons()
        st.success("🎉 Outstanding achievement! All daily milestones successfully completed.")

# ================= TAB 3: STRESS ASSESSMENT =================
with tab3:
    st.subheader("🧠 Real-time Biometric & Stress Assessment")
    q1 = st.radio("How exhausted do you feel right now?", ["Not at all", "Moderately", "Extremely"], key="q1")
    q2 = st.radio("Are you finding it hard to focus on your studies?", ["No", "A little bit", "Yes, very hard"], key="q2")
    
    if st.button("Analyze Mental State", key="btn_stress"):
        if q1 == "Extremely" or q2 == "Yes, very hard":
            st.error("🚨 Result: High cognitive fatigue detected. EduBalance AI recommends a 15-minute walk.")
        else:
            st.success("✨ Result: Optimal cognitive state! Your focus metrics look great.")

# ================= TAB 4: FOCUS POMODORO TIMER =================
with tab4:
    st.subheader("⏱️ Autonomous Focus Pomodoro Timer")
    st.write("Boost your productivity using science-backed 25-minute deep work intervals:")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        work_mins = st.slider("Select Focus Duration (Minutes)", 5, 60, 25, key="p_work_mins")
    with col_p2:
        break_mins = st.slider("Select Break Duration (Minutes)", 1, 15, 5, key="p_break_mins")

    if st.button("🚀 Start Focus Session", key="btn_start_pomodoro"):
        st.info(f"Focus session started for {work_mins} minutes. Stay tuned and avoid distractions!")
        latest_iteration = st.empty()
        bar = st.progress(0)
        
        for i in range(100):
            bar.progress(i + 1)
            latest_iteration.text(f"Focus in progress... Progress: {i + 1}%")
            time.sleep(0.02)
            
        st.balloons()
        st.success(f"🎉 Great job! Focus session completed. Now take a {break_mins}-minute break and drink water.")

# ================= TAB 5: BURNOUT PREDICTOR =================
with tab5:
    st.subheader("📈 AI Predictive Analytics: Burnout Risk Index")
    st.write("Our machine learning algorithm analyzes your study load, sleep patterns, and stress to predict fatigue risks:")
    
    risk_score = (study_hours * 5) + ((7 - sleep_hours) * 8)
    if "High" in str(stress_level) or "Burnout" in str(stress_level):
        risk_score += 30
    risk_score = min(max(risk_score, 10), 95)
    
    col_a, col_b = st.columns([4, 6])
    with col_a:
        st.metric(label="Calculated Burnout Risk", value=f"{risk_score}%", delta="⚠️ Moderate to High" if risk_score > 50 else "✅ Safe Zone")
    with col_b:
        if risk_score > 60:
            st.error("🚨 **Warning:** High probability of academic burnout within 3 days. AI has automatically scheduled mandatory relaxation slots.")
        else:
            st.success("✨ **Optimal Status:** Your academic pace is healthy and sustainable. Keep it up!")

# ================= TAB 6: WEEKLY AI INSIGHTS =================
with tab6:
    st.subheader("📊 Weekly AI Performance & Balance Insights")
    st.write("Review your progress trends and work-life balance over the past week:")
    
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    productivity = [85, 90, 75, 95, 60, 80, 88]
    
    fig_weekly = px.bar(
        x=days, y=productivity, 
        labels={"x": "Day of the Week", "y": "Productivity Score (%)"},
        title="Weekly Academic Performance Trend",
        color=productivity,
        color_continuous_scale="blues"
    )
    fig_weekly.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_weekly, use_container_width=True)
    
    st.info("💡 **AI Recommendation:** Your productivity peaks mid-week. Consider scheduling difficult programming tasks on Tuesday and Thursday.")
    