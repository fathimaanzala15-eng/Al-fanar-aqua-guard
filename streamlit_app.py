import streamlit as st
import pandas as pd
import numpy as np
import time

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Fanar Aqua Guard",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================
if "simulation_running" not in st.session_state:
    st.session_state.simulation_running = False

if "simulation_step" not in st.session_state:
    st.session_state.simulation_step = "System Ready"

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

    /* ---------- GLOBAL ---------- */
    .stApp {
        background:
            radial-gradient(circle at 20% 10%, rgba(0, 180, 220, 0.08), transparent 30%),
            radial-gradient(circle at 80% 20%, rgba(0, 100, 180, 0.08), transparent 30%),
            #06111c;
        color: #e8f7ff;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ---------- SIDEBAR ---------- */
    section[data-testid="stSidebar"] {
        background: #071722;
        border-right: 1px solid #173344;
    }

    section[data-testid="stSidebar"] * {
        color: #dff6ff !important;
    }

    /* ---------- MAIN TITLE ---------- */
    .main-title {
        font-size: 38px;
        font-weight: 800;
        color: #e8fbff;
        margin-bottom: 4px;
    }

    .subtitle {
        color: #8fb6c7;
        font-size: 16px;
        margin-bottom: 25px;
    }

    /* ---------- BRAND ---------- */
    .brand-box {
        padding: 18px;
        border-radius: 16px;
        background: linear-gradient(135deg, #0b2535, #09202d);
        border: 1px solid #1d4c61;
        margin-bottom: 20px;
    }

    .brand-title {
        font-size: 23px;
        font-weight: 800;
        color: #eaffff;
    }

    .brand-subtitle {
        color: #8db7c8;
        font-size: 12px;
        margin-top: 4px;
    }

    /* ---------- KPI ---------- */
    .kpi {
        background: linear-gradient(145deg, #0c1d29, #091722);
        border: 1px solid #1b3c4e;
        border-radius: 16px;
        padding: 20px;
        min-height: 125px;
    }

    .kpi-label {
        color: #87adbd;
        font-size: 13px;
        margin-bottom: 8px;
    }

    .kpi-value {
        font-size: 28px;
        font-weight: 800;
        color: #effcff;
    }

    .kpi-small {
        color: #6e9caf;
        font-size: 12px;
        margin-top: 5px;
    }

    /* ---------- SECTION ---------- */
    .section-title {
        font-size: 23px;
        font-weight: 750;
        color: #eafaff;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    /* ---------- CARDS ---------- */
    .card {
        background: #091a26;
        border: 1px solid #183b4d;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        color: #e7faff;
        margin-bottom: 8px;
    }

    .card-text {
        color: #91b6c5;
        line-height: 1.55;
        font-size: 14px;
    }

    /* ---------- FANAR VISUAL ---------- */
    .fanar-visual {
        background:
            linear-gradient(180deg, rgba(7, 38, 55, 0.95), rgba(4, 19, 29, 0.98));
        border: 1px solid #20536a;
        border-radius: 20px;
        padding: 25px;
        margin-top: 15px;
        margin-bottom: 25px;
        overflow: hidden;
    }

    .visual-title {
        text-align: center;
        font-size: 24px;
        font-weight: 800;
        color: #eaffff;
        margin-bottom: 25px;
    }

    .visual-subtitle {
        text-align: center;
        color: #7fa9bb;
        font-size: 13px;
        margin-top: -15px;
        margin-bottom: 25px;
    }

    .visual-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        flex-wrap: wrap;
    }

    .visual-box {
        flex: 1;
        min-width: 180px;
        text-align: center;
        background: rgba(5, 24, 35, 0.95);
        border: 1px solid #21495c;
        border-radius: 16px;
        padding: 20px;
    }

    .visual-icon {
        font-size: 42px;
        margin-bottom: 8px;
        line-height: 1.2;
    }

    .visual-label {
        font-weight: 700;
        color: #e7faff;
        font-size: 15px;
    }

    .visual-info {
        color: #82aabd;
        font-size: 12px;
        margin-top: 5px;
    }

    .arrow {
        font-size: 30px;
        color: #55d6ff;
        font-weight: bold;
    }

    /* ---------- MODULES ---------- */
    .module-grid {
        display: flex;
        gap: 12px;
        justify-content: center;
        margin-top: 20px;
        flex-wrap: wrap;
    }

    .module {
        background: #0a2533;
        border: 1px solid #23718c;
        border-radius: 12px;
        padding: 14px 22px;
        text-align: center;
        min-width: 120px;
    }

    .module-name {
        color: #aeefff;
        font-weight: 700;
    }

    .module-status {
        color: #65e6a8;
        font-size: 11px;
        margin-top: 4px;
    }

    /* ---------- STATUS ---------- */
    .status-active {
        color: #62e6a4;
        font-weight: 700;
    }

    .status-high {
        color: #ff7373;
        font-weight: 800;
    }

    .status-moderate {
        color: #ffd166;
        font-weight: 800;
    }

    .status-low {
        color: #63e6a4;
        font-weight: 800;
    }

    /* ---------- ALERT ---------- */
    .alert-box {
        background: rgba(110, 25, 25, 0.25);
        border: 1px solid #a74444;
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 15px;
    }

    /* ---------- DEMO ---------- */
    .demo-banner {
        background: rgba(0, 130, 180, 0.12);
        border: 1px solid #1f6d88;
        border-radius: 12px;
        padding: 12px 16px;
        color: #9fd9ea;
        font-size: 13px;
        margin-bottom: 20px;
    }

    /* ---------- FOOTER ---------- */
    .footer {
        text-align: center;
        color: #587888;
        font-size: 12px;
        padding: 30px 0 10px 0;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown("""
    <div class="brand-box">
        <div class="brand-title">🌊 AL FANAR</div>
        <div class="brand-subtitle">
            Fanar Aqua Guard
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Swarm Assessment",
            "Response Control",
            "Monitoring Data",
            "Alerts"
        ]
    )

    st.markdown("---")

    st.markdown(
        "<div style='color:#76a8bb;font-size:12px;'>"
        "ATP / ENEC ChallengeON 2026"
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# DEMO DATA
# =========================================================
swarm_intensity = 72
distance = 320
confidence = 91
direction = "Toward intake"

if swarm_intensity >= 70 and direction == "Toward intake":
    risk = "HIGH"
    response = "REDIRECT"
elif swarm_intensity >= 45:
    risk = "MODERATE"
    response = "ADAPT"
else:
    risk = "LOW"
    response = "MONITOR"


# =========================================================
# DASHBOARD
# =========================================================
if page == "Dashboard":

    st.markdown(
        '<div class="main-title">🌊 Fanar Aqua Guard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Autonomous Jellyfish Swarm Management & Seawater Intake Protection'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="demo-banner">'
        '⚠️ Demonstration prototype — all sensor readings and swarm conditions '
        'shown here are simulated.'
        '</div>',
        unsafe_allow_html=True
    )

    # ---------- KPI ROW ----------
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-label">SWARM STATUS</div>
            <div class="kpi-value">🪼 DETECTED</div>
            <div class="kpi-small">Intensity: {swarm_intensity}%</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-label">INTAKE RISK</div>
            <div class="kpi-value">{risk}</div>
            <div class="kpi-small">Distance: {distance} m</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-label">CURRENT RESPONSE</div>
            <div class="kpi-value">{response}</div>
            <div class="kpi-small">Direction: {direction}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="kpi">
            <div class="kpi-label">AUTOMATION</div>
            <div class="kpi-value">ACTIVE</div>
            <div class="kpi-small">Manual intervention minimized</div>
        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # FANAR VISUAL
    # =====================================================
    st.markdown("""
    <div class="fanar-visual">

        <div class="visual-title">
            🪼 FANAR Autonomous Response Visualization
        </div>

        <div class="visual-subtitle">
            Detect → Analyze → Assess → Respond → Verify
        </div>

        <div class="visual-row">

            <div class="visual-box">
                <div class="visual-icon">🪼</div>
                <div class="visual-label">Incoming Swarm</div>
                <div class="visual-info">
                    High activity detected
                </div>
            </div>

            <div class="arrow">→</div>

            <div class="visual-box">
                <div class="visual-icon">📡</div>
                <div class="visual-label">Detection</div>
                <div class="visual-info">
                    Camera + sonar + sensors
                </div>
            </div>

            <div class="arrow">→</div>

            <div class="visual-box">
                <div class="visual-icon">🧠</div>
                <div class="visual-label">Risk Engine</div>
                <div class="visual-info">
                    Intake risk assessment
                </div>
            </div>

            <div class="arrow">→</div>

            <div class="visual-box">
                <div class="visual-icon">⚙️</div>
                <div class="visual-label">FANAR Modules</div>
                <div class="visual-info">
                    Adaptive response
                </div>
            </div>

            <div class="arrow">→</div>

            <div class="visual-box">
                <div class="visual-icon">🌊</div>
                <div class="visual-label">Protected Intake</div>
                <div class="visual-info">
                    Reduced swarm exposure
                </div>
            </div>

        </div>

        <div class="module-grid">

            <div class="module">
                <div class="module-name">F1</div>
                <div class="module-status">● ACTIVE</div>
            </div>

            <div class="module">
                <div class="module-name">F2</div>
                <div class="module-status">● ACTIVE</div>
            </div>

            <div class="module">
                <div class="module-name">F3</div>
                <div class="module-status">● ACTIVE</div>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # SIMULATION
    # =====================================================
    st.markdown(
        '<div class="section-title">Autonomous Response Simulation</div>',
        unsafe_allow_html=True
    )

    if st.button("▶ Run FANAR Simulation", use_container_width=True):

        progress = st.progress(0)

        steps = [
            ("Detecting jellyfish swarm...", 20),
            ("Analyzing swarm movement...", 40),
            ("Assessing intake risk...", 60),
            ("Activating adaptive response...", 80),
            ("Verifying response outcome...", 100)
        ]

        for message, value in steps:
            st.session_state.simulation_step = message
            st.info(message)
            progress.progress(value)
            time.sleep(0.6)

        st.success(
            "FANAR response verified — swarm exposure to the protected intake "
            "has been reduced in the demonstration scenario."
        )

    # =====================================================
    # CURRENT DECISION
    # =====================================================
    st.markdown(
        '<div class="section-title">Current FANAR Decision</div>',
        unsafe_allow_html=True
    )

    d1, d2, d3 = st.columns(3)

    with d1:
        st.markdown("""
        <div class="card">
            <div class="card-title">🧠 Risk Assessment</div>
            <div class="card-text">
                High-risk condition detected because the swarm has high intensity
                and is moving toward the protected intake.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with d2:
        st.markdown("""
        <div class="card">
            <div class="card-title">⚙️ Response</div>
            <div class="card-text">
                FANAR selects a redirect response and coordinates the active
                response modules.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with d3:
        st.markdown("""
        <div class="card">
            <div class="card-title">🔄 Verification</div>
            <div class="card-text">
                System continuously monitors swarm movement and adjusts the
                response based on updated conditions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # SYSTEM STATUS
    # =====================================================
    st.markdown(
        '<div class="section-title">System Status</div>',
        unsafe_allow_html=True
    )

    status_data = pd.DataFrame({
        "System": [
            "Early Warning",
            "Camera",
            "Sonar",
            "Water Sensors",
            "Risk Engine",
            "F1 Module",
            "F2 Module",
            "F3 Module",
            "Continuous Monitoring"
        ],
        "Status": ["ACTIVE"] * 9
    })

    st.dataframe(
        status_data,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # ACTIVE EVENT
    # =====================================================
    st.markdown(
        '<div class="section-title">Active Event</div>',
        unsafe_allow_html=True
    )

    e1, e2, e3, e4, e5 = st.columns(5)

    event_values = [
        ("EVENT", "FANAR-2026-001"),
        ("STATUS", "DETECTED"),
        ("DIRECTION", "TOWARD INTAKE"),
        ("DISTANCE", "320 m"),
        ("RESPONSE", "REDIRECT")
    ]

    for col, (label, value) in zip(
        [e1, e2, e3, e4, e5],
        event_values
    ):
        with col:
            st.markdown(f"""
            <div class="kpi">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value" style="font-size:18px;">
                    {value}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # =====================================================
    # CLOSED LOOP
    # =====================================================
    st.markdown(
        '<div class="section-title">Closed-Loop Control</div>',
        unsafe_allow_html=True
    )

    loop = pd.DataFrame({
        "Stage": [
            "1. Detect",
            "2. Analyze",
            "3. Assess",
            "4. Adapt",
            "5. Verify"
        ],
        "Function": [
            "Detect swarm presence",
            "Track swarm movement",
            "Determine intake risk",
            "Activate response",
            "Monitor outcome"
        ]
    })

    st.dataframe(
        loop,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # RESPONSE CHART
    # =====================================================
    st.markdown(
        '<div class="section-title">Response Effect — Demonstration Data</div>',
        unsafe_allow_html=True
    )

    chart_data = pd.DataFrame({
        "Time": [
            "T-4",
            "T-3",
            "T-2",
            "T-1",
            "T0",
            "T+1",
            "T+2"
        ],
        "Swarm Activity": [
            45, 55, 65, 72, 75, 58, 42
        ],
        "Intake Risk": [
            20, 28, 40, 55, 70, 48, 25
        ]
    })

    st.line_chart(
        chart_data.set_index("Time")
    )


# =========================================================
# SWARM ASSESSMENT
# =========================================================
elif page == "Swarm Assessment":

    st.markdown(
        '<div class="main-title">🪼 Swarm Assessment</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Evaluate swarm conditions and determine intake risk.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        intensity = st.slider(
            "Swarm Intensity (%)",
            0,
            100,
            72
        )

        distance_input = st.slider(
            "Distance to Protected Intake (m)",
            50,
            2000,
            320
        )

        detection_confidence = st.slider(
            "Detection Confidence (%)",
            0,
            100,
            91
        )

    with col2:

        movement_direction = st.selectbox(
            "Estimated Movement Direction",
            [
                "Toward intake",
                "Parallel to intake",
                "Away from intake",
                "Uncertain"
            ]
        )

        water_condition = st.selectbox(
            "Local Water Condition",
            [
                "Normal",
                "High current",
                "Low current",
                "Turbulent"
            ]
        )

    if intensity >= 70 and movement_direction == "Toward intake":
        assessment_risk = "HIGH"
        recommended_response = "REDIRECT"

    elif intensity >= 45:
        assessment_risk = "MODERATE"
        recommended_response = "ADAPT / MONITOR"

    else:
        assessment_risk = "LOW"
        recommended_response = "MONITOR"

    st.markdown(
        '<div class="section-title">Assessment Result</div>',
        unsafe_allow_html=True
    )

    a1, a2, a3 = st.columns(3)

    with a1:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-label">RISK LEVEL</div>
            <div class="kpi-value">{assessment_risk}</div>
        </div>
        """, unsafe_allow_html=True)

    with a2:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-label">RECOMMENDED RESPONSE</div>
            <div class="kpi-value" style="font-size:21px;">
                {recommended_response}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with a3:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-label">CONFIDENCE</div>
            <div class="kpi-value">{detection_confidence}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">Decision Logic</div>
        <div class="card-text">
            This demonstration uses a transparent rule-based prototype.
            It is not a trained machine-learning model.
            In a field deployment, the decision engine would use calibrated
            sensor data and validated operating thresholds.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# RESPONSE CONTROL
# =========================================================
elif page == "Response Control":

    st.markdown(
        '<div class="main-title">⚙️ Response Control</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Select and inspect the autonomous response mode.'
        '</div>',
        unsafe_allow_html=True
    )

    selected_response = st.radio(
        "Response Mode",
        [
            "Guide",
            "Redirect",
            "Collect",
            "Release"
        ],
        horizontal=True
    )

    descriptions = {
        "Guide":
            "Guide the swarm toward a safer path away from the protected intake.",

        "Redirect":
            "Generate a controlled response to reduce swarm accumulation near the intake.",

        "Collect":
            "Coordinate modular collection when appropriate and environmentally permitted.",

        "Release":
            "Release collected organisms in a controlled location when conditions permit."
    }

    st.markdown(f"""
    <div class="card">
        <div class="card-title">Selected Response: {selected_response}</div>
        <div class="card-text">
            {descriptions[selected_response]}
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Automation", "ACTIVE")

    with c2:
        st.metric("Manual Intervention", "MINIMAL")

    with c3:
        st.metric("System State", "MONITORING")

    st.markdown(
        '<div class="section-title">FANAR Module Status</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3 = st.columns(3)

    for col, module in zip([m1, m2, m3], ["F1", "F2", "F3"]):
        with col:
            st.markdown(f"""
            <div class="module" style="width:100%;">
                <div class="module-name">{module}</div>
                <div class="module-status">● ACTIVE</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Autonomous Response Chain</div>',
        unsafe_allow_html=True
    )

    response_chain = pd.DataFrame({
        "Step": [
            "1",
            "2",
            "3",
            "4",
            "5"
        ],
        "Action": [
            "Observe",
            "Assess",
            "Select response",
            "Activate modules",
            "Verify outcome"
        ],
        "Status": [
            "Complete",
            "Complete",
            "Complete",
            "Active",
            "Monitoring"
        ]
    })

    st.dataframe(
        response_chain,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# MONITORING DATA
# =========================================================
elif page == "Monitoring Data":

    st.markdown(
        '<div class="main-title">📊 Monitoring Data</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Simulated sensor and swarm monitoring data.'
        '</div>',
        unsafe_allow_html=True
    )

    data = pd.DataFrame({
        "Time": pd.date_range(
            "2026-10-10 10:00",
            periods=10,
            freq="5min"
        ),
        "Jellyfish Activity": [
            42, 48, 55, 61, 68,
            72, 75, 67, 55, 44
        ],
        "Intake Risk": [
            18, 22, 30, 37, 48,
            60, 70, 58, 42, 25
        ],
        "Detection Confidence": [
            84, 86, 88, 89, 90,
            91, 92, 91, 90, 89
        ]
    })

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-title">Jellyfish Activity</div>',
        unsafe_allow_html=True
    )

    st.line_chart(
        data.set_index("Time")["Jellyfish Activity"]
    )

    st.markdown(
        '<div class="section-title">Intake Risk</div>',
        unsafe_allow_html=True
    )

    st.line_chart(
        data.set_index("Time")["Intake Risk"]
    )

    st.markdown(
        '<div class="section-title">Sensor Inputs</div>',
        unsafe_allow_html=True
    )

    sensors = pd.DataFrame({
        "Sensor": [
            "Camera",
            "Sonar",
            "Water Temperature",
            "Current",
            "Swarm Position"
        ],
        "Reading": [
            "Swarm detected",
            "Aggregation detected",
            "28.4 °C",
            "0.8 m/s",
            "320 m from intake"
        ],
        "Status": [
            "ACTIVE",
            "ACTIVE",
            "ACTIVE",
            "ACTIVE",
            "ACTIVE"
        ]
    })

    st.dataframe(
        sensors,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# ALERTS
# =========================================================
elif page == "Alerts":

    st.markdown(
        '<div class="main-title">🚨 Alerts</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Operational alerts and autonomous decision log.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="alert-box">
        <strong>🚨 HIGH-RISK SWARM DETECTED</strong><br><br>
        Jellyfish activity is elevated and movement is toward the protected
        seawater intake. FANAR has selected a redirect response.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Active Alerts", "1")

    with c2:
        st.metric("Risk Level", "HIGH")

    with c3:
        st.metric("Response", "REDIRECT")

    st.markdown(
        '<div class="section-title">Decision Log</div>',
        unsafe_allow_html=True
    )

    decision_log = pd.DataFrame({
        "Time": [
            "10:00",
            "10:05",
            "10:10",
            "10:15",
            "10:20"
        ],
        "Event": [
            "Swarm detected",
            "Movement analyzed",
            "Intake risk assessed",
            "Redirect activated",
            "Outcome verified"
        ],
        "System": [
            "Early Warning",
            "Risk Engine",
            "Risk Engine",
            "FANAR Modules",
            "Monitoring"
        ],
        "Status": [
            "Complete",
            "Complete",
            "HIGH RISK",
            "ACTIVE",
            "Verified"
        ]
    })

    st.dataframe(
        decision_log,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-title">Autonomous Chain</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <div class="card-text">
            Early Warning → Swarm Assessment → Risk Evaluation →
            FANAR Response → Continuous Monitoring
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
    FANAR Aqua Guard | ATP / ENEC ChallengeON 2026<br>
    AI-assisted jellyfish swarm management prototype<br>
    Demonstration interface — simulated data only
</div>
""", unsafe_allow_html=True)
