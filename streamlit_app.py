```python
import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Fanar Aqua Guard",
    page_icon="🪼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #071923;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

h1, h2, h3 {
    color: #EAF7FA;
}

.subtitle {
    color: #9CCBD3;
    font-size: 1.05rem;
    margin-top: -12px;
    margin-bottom: 25px;
}

.card {
    background: linear-gradient(145deg, #102B35, #0B2029);
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #214752;
    min-height: 135px;
}

.card-title {
    color: #8FBCC4;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

.card-value {
    color: #F2FBFC;
    font-size: 1.8rem;
    font-weight: 700;
    margin-top: 10px;
}

.card-small {
    color: #9CCBD3;
    font-size: 0.82rem;
    margin-top: 5px;
}

.section {
    background: #0C222B;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #1E424D;
    margin-top: 20px;
}

.status-good {
    background: #123A36;
    color: #8FE0C7;
    padding: 12px 18px;
    border-radius: 10px;
    font-weight: 600;
}

.status-warning {
    background: #493A16;
    color: #F6D77A;
    padding: 12px 18px;
    border-radius: 10px;
    font-weight: 600;
}

.status-danger {
    background: #491F24;
    color: #FF9FA7;
    padding: 12px 18px;
    border-radius: 10px;
    font-weight: 600;
}

.workflow {
    background: #102B35;
    border: 1px solid #28505A;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    color: #DDF4F6;
    font-weight: 600;
}

.arrow {
    text-align: center;
    font-size: 1.5rem;
    color: #64C6D2;
    padding-top: 15px;
}

.demo {
    background: #172A30;
    border-left: 4px solid #64C6D2;
    padding: 12px 16px;
    border-radius: 6px;
    color: #B8D4D8;
    font-size: 0.85rem;
}

.footer {
    text-align: center;
    color: #7899A0;
    font-size: 0.8rem;
    padding: 35px 0 10px 0;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DEMO DATA
# ---------------------------------------------------------

time_points = [
    "08:00", "09:00", "10:00", "11:00",
    "12:00", "13:00", "14:00", "15:00"
]

jellyfish_activity = [12, 15, 18, 27, 34, 41, 38, 32]
intake_risk = [5, 7, 9, 14, 22, 31, 28, 23]

activity_df = pd.DataFrame({
    "Time": time_points,
    "Jellyfish Activity": jellyfish_activity,
    "Intake Risk": intake_risk
})

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.markdown("## 🪼 Fanar Aqua Guard")
st.sidebar.caption("AI-Assisted Jellyfish Swarm Management")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Swarm Assessment",
        "Response Control",
        "Monitoring Data",
        "Alerts"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    **System Mode**

    🟢 Prototype Monitoring
    """
)

st.sidebar.markdown(
    """
    **Prototype**

    Demo data is simulated and is used only to demonstrate the dashboard workflow.
    """
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🪼 Fanar Aqua Guard")
st.markdown(
    '<div class="subtitle">AI-Assisted Jellyfish Swarm Management & Intake Protection</div>',
    unsafe_allow_html=True
)

# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

    st.markdown(
        '<div class="demo">⚠️ DEMONSTRATION MODE — All readings shown in this prototype are simulated.</div>',
        unsafe_allow_html=True
    )

    st.markdown("## System Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">Swarm Status</div>
            <div class="card-value">Detected</div>
            <div class="card-small">Early warning received</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Intake Risk</div>
            <div class="card-value">Moderate</div>
            <div class="card-small">Requires monitoring</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-title">Response Mode</div>
            <div class="card-value">Redirect</div>
            <div class="card-small">Automated response</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="card-title">System Status</div>
            <div class="card-value">Active</div>
            <div class="card-small">Monitoring continuously</div>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # WORKFLOW
    # -----------------------------------------------------

    st.markdown("## Response Workflow")

    w1, a1, w2, a2, w3, a3, w4 = st.columns([2, .5, 2, .5, 2, .5, 2])

    with w1:
        st.markdown(
            '<div class="workflow">🪼<br>Early Warning<br>Received</div>',
            unsafe_allow_html=True
        )

    with a1:
        st.markdown('<div class="arrow">→</div>', unsafe_allow_html=True)

    with w2:
        st.markdown(
            '<div class="workflow">🔎<br>Swarm<br>Assessment</div>',
            unsafe_allow_html=True
        )

    with a2:
        st.markdown('<div class="arrow">→</div>', unsafe_allow_html=True)

    with w3:
        st.markdown(
            '<div class="workflow">⚠️<br>Intake Risk<br>Assessment</div>',
            unsafe_allow_html=True
        )

    with a3:
        st.markdown('<div class="arrow">→</div>', unsafe_allow_html=True)

    with w4:
        st.markdown(
            '<div class="workflow">🔄<br>Response<br>Activated</div>',
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # CHARTS
    # -----------------------------------------------------

    st.markdown("## Swarm Activity & Intake Risk")

    st.line_chart(
        activity_df.set_index("Time"),
        height=350
    )

    # -----------------------------------------------------
    # CURRENT EVENT
    # -----------------------------------------------------

    st.markdown("## Current Event")

    left, right = st.columns(2)

    with left:
        st.markdown("""
        <div class="section">
        <h3>🪼 Jellyfish Swarm</h3>
        <p><b>Status:</b> Early warning received</p>
        <p><b>Activity:</b> Elevated</p>
        <p><b>Trend:</b> Increasing</p>
        <p><b>Detection confidence:</b> Demo value</p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="section">
        <h3>⚠️ Intake Protection</h3>
        <p><b>Risk:</b> Moderate</p>
        <p><b>Current response:</b> Redirect</p>
        <p><b>Manual intervention:</b> Minimal</p>
        <p><b>System state:</b> Monitoring response</p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SWARM ASSESSMENT
# =========================================================

elif page == "Swarm Assessment":

    st.header("🔎 Swarm Assessment")

    st.markdown(
        '<div class="demo">Demo assessment interface. Replace simulated inputs with real early-warning/detection data when available.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Swarm Inputs")

        swarm_intensity = st.slider(
            "Swarm intensity",
            0,
            100,
            65
        )

        proximity = st.slider(
            "Proximity to intake",
            0,
            100,
            55
        )

        confidence = st.slider(
            "Detection confidence",
            0,
            100,
            80
        )

    with col2:
        st.subheader("Assessment")

        score = (
            swarm_intensity * 0.4
            + proximity * 0.4
            + confidence * 0.2
        )

        if score < 30:
            risk = "LOW"
        elif score < 60:
            risk = "MODERATE"
        elif score < 80:
            risk = "HIGH"
        else:
            risk = "CRITICAL"

        st.metric("Demo Risk Score", f"{score:.0f}/100")
        st.metric("Intake Risk", risk)

    st.markdown("## Why this risk level?")

    st.info(
        "The prototype combines swarm intensity, proximity to the intake, "
        "and detection confidence to demonstrate an explainable risk-assessment workflow. "
        "This is a demo rule-based system and is not a trained predictive model."
    )

# =========================================================
# RESPONSE CONTROL
# =========================================================

elif page == "Response Control":

    st.header("🔄 Response Control")

    st.markdown(
        '<div class="demo">Prototype response-control interface. Actions shown here are simulated and do not control real equipment.</div>',
        unsafe_allow_html=True
    )

    st.subheader("Select Response Mode")

    response = st.radio(
        "Response strategy",
        [
            "Guide",
            "Redirect",
            "Collect",
            "Release"
        ],
        horizontal=True
    )

    st.markdown("---")

    if response == "Guide":
        st.success(
            "GUIDE selected — demonstrate controlled movement of the swarm toward a safer pathway."
        )

    elif response == "Redirect":
        st.warning(
            "REDIRECT selected — demonstrate directing the swarm away from the intake area."
        )

    elif response == "Collect":
        st.warning(
            "COLLECT selected — demonstrate controlled collection while minimizing harm to marine organisms."
        )

    elif response == "Release":
        st.info(
            "RELEASE selected — demonstrate safe release after controlled collection or handling."
        )

    st.markdown("## Response Status")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Current Mode", response)

    with c2:
        st.metric("Manual Intervention", "Minimal")

    with c3:
        st.metric("System Status", "Active")

    st.markdown("## Response Sequence")

    sequence = pd.DataFrame({
        "Stage": [
            "Early Warning",
            "Assessment",
            "Response Activated",
            "Outcome Monitoring"
        ],
        "Status": [
            "Complete",
            "Complete",
            "Active",
            "Monitoring"
        ]
    })

    st.dataframe(
        sequence,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# MONITORING DATA
# =========================================================

elif page == "Monitoring Data":

    st.header("📊 Monitoring Data")

    st.markdown(
        '<div class="demo">SIMULATED DATA — Replace with real sensor, detection, or early-warning data when available.</div>',
        unsafe_allow_html=True
    )

    data = pd.DataFrame({
        "Time": time_points,
        "Swarm Activity": jellyfish_activity,
        "Intake Risk": intake_risk,
        "Response": [
            "Monitoring",
            "Monitoring",
            "Assessment",
            "Assessment",
            "Redirect",
            "Redirect",
            "Redirect",
            "Monitoring"
        ]
    })

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("## Activity Trend")

    st.line_chart(
        data.set_index("Time")[["Swarm Activity", "Intake Risk"]]
    )

# =========================================================
# ALERTS
# =========================================================

elif page == "Alerts":

    st.header("🚨 Alerts")

    st.markdown(
        '<div class="demo">Demo alerts only. These alerts do not represent live ENEC operational data.</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="status-warning">
        ⚠️ MODERATE — Jellyfish swarm activity increasing near monitored intake area.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="status-good">
        🟢 RESPONSE ACTIVE — Redirect response selected for demonstration.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="status-good">
        🟢 MONITORING — System is tracking response outcome.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Recommended Operational Logic")

    st.info(
        "When an early warning is received, the system should assess swarm conditions, "
        "estimate potential intake impact, select an appropriate response, "
        "and continuously monitor whether the response is effective."
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    '<div class="footer">Fanar Aqua Guard | AI-assisted jellyfish swarm management prototype | Demo system</div>',
    unsafe_allow_html=True
)

