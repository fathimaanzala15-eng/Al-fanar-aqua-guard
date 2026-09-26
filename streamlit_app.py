import streamlit as st
import pandas as pd
import time

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Fanar Aqua Guard",
    page_icon="🪼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================
if "simulation_running" not in st.session_state:
    st.session_state.simulation_running = False

if "simulation_complete" not in st.session_state:
    st.session_state.simulation_complete = False

if "selected_response" not in st.session_state:
    st.session_state.selected_response = "Redirect"

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #06131f 0%, #082333 45%, #041018 100%);
    color: #e8f7ff;
}

section[data-testid="stSidebar"] {
    background: #061722;
    border-right: 1px solid #16445c;
}

section[data-testid="stSidebar"] * {
    color: #dff5ff !important;
}

h1, h2, h3 {
    color: #e8f7ff !important;
}

p, label {
    color: #b9d7e5 !important;
}

.kpi {
    background: linear-gradient(145deg, #0b2638, #071923);
    border: 1px solid #1c5069;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    min-height: 120px;
}

.kpi-title {
    color: #8eb8ca;
    font-size: 14px;
    margin-bottom: 10px;
}

.kpi-value {
    font-size: 28px;
    font-weight: 700;
    color: #e9fbff;
}

.kpi-sub {
    font-size: 12px;
    color: #79b8cf;
    margin-top: 5px;
}

.card {
    background: #091d2a;
    border: 1px solid #17465d;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 15px;
}

.section-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 12px;
    color: #e5f8ff;
}

.small {
    color: #88b6c9;
    font-size: 13px;
}

.status-high {
    color: #ff7777;
    font-weight: 700;
}

.status-medium {
    color: #ffc857;
    font-weight: 700;
}

.status-low {
    color: #63d6a1;
    font-weight: 700;
}

.alert-box {
    background: #321b1b;
    border: 1px solid #7a3838;
    border-radius: 12px;
    padding: 15px;
}

.warning-box {
    background: #332b17;
    border: 1px solid #75602b;
    border-radius: 12px;
    padding: 15px;
}

.success-box {
    background: #102c24;
    border: 1px solid #28634f;
    border-radius: 12px;
    padding: 15px;
}

.info-box {
    background: #0b2738;
    border: 1px solid #20546d;
    border-radius: 12px;
    padding: 15px;
}

.flow-card {
    background: #0a2231;
    border: 1px solid #1b5069;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
    min-height: 130px;
}

.flow-icon {
    font-size: 28px;
    margin-bottom: 8px;
}

.flow-title {
    font-weight: 700;
    color: #e9faff;
}

.flow-text {
    font-size: 12px;
    color: #8eb8ca;
    margin-top: 6px;
}

.fanar-visual {
    background: linear-gradient(135deg, #061722, #09283a);
    border: 1px solid #1c566f;
    border-radius: 18px;
    padding: 30px;
    margin-top: 10px;
    margin-bottom: 20px;
}

.visual-title {
    text-align: center;
    color: #e9faff;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 25px;
}

.visual-subtitle {
    text-align: center;
    color: #86b5c8;
    font-size: 13px;
    margin-bottom: 30px;
}

.visual-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
}

.visual-zone {
    text-align: center;
    flex: 1;
}

.zone-label {
    color: #8eb8ca;
    font-size: 12px;
    margin-bottom: 10px;
}

.jellyfish {
    font-size: 38px;
    letter-spacing: 4px;
}

.intake {
    background: #103c50;
    border: 2px solid #2d8fb1;
    border-radius: 12px;
    padding: 22px 10px;
    font-size: 35px;
}

.modules {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin: 12px 0;
}

.module {
    width: 45px;
    height: 45px;
    background: #11617c;
    border: 2px solid #54c7e9;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
}

.arrow {
    color: #4bc5e7;
    font-size: 30px;
    text-align: center;
}

.path {
    height: 5px;
    background: #28a9cf;
    border-radius: 5px;
    margin: 12px 0;
}

.safe-path {
    height: 5px;
    background: #48d69a;
    border-radius: 5px;
    margin: 12px 0;
}

.module-status {
    background: #08212e;
    border: 1px solid #1a4d63;
    border-radius: 10px;
    padding: 10px;
    margin-top: 15px;
    text-align: center;
    color: #9ed3e5;
    font-size: 12px;
}

.event-card {
    background: #081d29;
    border: 1px solid #1a4d63;
    border-radius: 12px;
    padding: 16px;
    min-height: 110px;
}

.event-label {
    color: #7faabd;
    font-size: 12px;
    margin-bottom: 7px;
}

.event-value {
    color: #e9faff;
    font-size: 20px;
    font-weight: 700;
}

.system-row {
    background: #081d29;
    border: 1px solid #17465d;
    border-radius: 8px;
    padding: 12px 15px;
    margin-bottom: 7px;
}

.system-name {
    color: #dceff6;
}

.system-active {
    color: #5fe0a8;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("🪼 Fanar Aqua Guard")
st.sidebar.caption("ATP 2026 • Autonomous Jellyfish Swarm Management")

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

st.sidebar.info(
    "Prototype demonstration only.\n\n"
    "All readings shown in this dashboard are simulated."
)

# =========================================================
# HEADER
# =========================================================
st.markdown("# 🪼 Fanar Aqua Guard")

st.markdown(
    "### Autonomous Jellyfish Swarm Management & Seawater Intake Protection"
)

st.markdown(
    '<div class="info-box">'
    '<b>Prototype Mode:</b> This dashboard demonstrates the FANAR '
    'decision-support and autonomous response concept using simulated sensor data.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("")


# =========================================================
# DASHBOARD
# =========================================================
if page == "Dashboard":

    # -----------------------------------------------------
    # CURRENT VALUES
    # -----------------------------------------------------
    swarm_intensity = 72
    distance = 320
    confidence = 91
    direction = "Toward intake"

    if swarm_intensity >= 70 and direction == "Toward intake":
        risk = "HIGH"
        response = "Redirect"
    elif swarm_intensity >= 45:
        risk = "MODERATE"
        response = "Adapt"
    else:
        risk = "LOW"
        response = "Monitor"

    # -----------------------------------------------------
    # KPI CARDS
    # -----------------------------------------------------
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-title">SWARM STATUS</div>
            <div class="kpi-value">Detected</div>
            <div class="kpi-sub">Active event</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        risk_class = "status-high" if risk == "HIGH" else (
            "status-medium" if risk == "MODERATE" else "status-low"
        )

        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-title">INTAKE RISK</div>
            <div class="kpi-value {risk_class}">{risk}</div>
            <div class="kpi-sub">Dynamic assessment</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi">
            <div class="kpi-title">CURRENT RESPONSE</div>
            <div class="kpi-value">{response}</div>
            <div class="kpi-sub">Adaptive response</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="kpi">
            <div class="kpi-title">AUTOMATION</div>
            <div class="kpi-value">Active</div>
            <div class="kpi-sub">Minimal manual intervention</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    # -----------------------------------------------------
    # MAIN FANAR VISUAL
    # -----------------------------------------------------
    st.markdown("""
    <div class="fanar-visual">

        <div class="visual-title">
            FANAR Autonomous Response Visualization
        </div>

        <div class="visual-subtitle">
            Detect → Predict → Adapt → Verify
        </div>

        <div class="visual-row">

            <div class="visual-zone">
                <div class="zone-label">
                    INCOMING JELLYFISH SWARM
                </div>

                <div class="jellyfish">
                    🪼 🪼 🪼
                </div>

                <div class="path"></div>

                <div class="zone-label">
                    Predicted movement toward intake
                </div>
            </div>

            <div class="arrow">
                →
            </div>

            <div class="visual-zone">

                <div class="zone-label">
                    FANAR RESPONSE MODULES
                </div>

                <div class="modules">
                    <div class="module">F1</div>
                    <div class="module">F2</div>
                    <div class="module">F3</div>
                </div>

                <div class="safe-path"></div>

                <div class="zone-label">
                    Controlled flow redirects swarm
                </div>

            </div>

            <div class="arrow">
                →
            </div>

            <div class="visual-zone">

                <div class="zone-label">
                    PROTECTED SEAWATER INTAKE
                </div>

                <div class="intake">
                    🌊
                </div>

                <div class="zone-label">
                    Intake exposure reduced
                </div>

            </div>

        </div>

        <div class="module-status">
            🟢 3/3 response modules active
            &nbsp;&nbsp;|&nbsp;&nbsp;
            ⚙ Automation active
            &nbsp;&nbsp;|&nbsp;&nbsp;
            🔄 Continuous monitoring
            &nbsp;&nbsp;|&nbsp;&nbsp;
            👤 Manual intervention minimal
        </div>

    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # RUN SIMULATION
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">Autonomous Demonstration</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Run a simulated high-risk jellyfish event and observe how FANAR "
        "moves through its autonomous decision cycle."
    )

    if st.button(
        "▶ Run FANAR Simulation",
        use_container_width=True,
        type="primary"
    ):

        progress = st.progress(0)

        status_box = st.empty()

        steps = [
            ("👁️ DETECT", "Jellyfish swarm detected by monitoring system.", 20),
            ("🧠 ANALYZE", "Swarm intensity and movement direction assessed.", 40),
            ("⚠️ ASSESS", "HIGH intake risk identified.", 60),
            ("⚙️ RESPOND", "Redirect response activated. FANAR modules engaged.", 80),
            ("🔄 VERIFY", "Swarm movement reassessed. Continue monitoring.", 100)
        ]

        for title, message, value in steps:
            status_box.markdown(
                f"""
                <div class="info-box">
                    <b>{title}</b><br>
                    {message}
                </div>
                """,
                unsafe_allow_html=True
            )

            progress.progress(value)
            time.sleep(0.7)

        st.session_state.simulation_complete = True

        st.success(
            "FANAR simulation complete — response verified and monitoring continues."
        )

    if st.session_state.simulation_complete:

        st.markdown("""
        <div class="success-box">
        <b>🟢 FANAR RESPONSE VERIFIED</b><br><br>
        The simulated swarm response has been completed.
        FANAR remains in continuous monitoring mode.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    # -----------------------------------------------------
    # CURRENT FANAR DECISION
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">Current FANAR Decision</div>',
        unsafe_allow_html=True
    )

    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown("""
        <div class="card">
            <h3>🔎 Analyze</h3>
            <p>
            FANAR evaluates swarm intensity, distance to the intake,
            movement direction and detection confidence.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with r2:
        st.markdown("""
        <div class="card">
            <h3>⚙️ Adapt</h3>
            <p>
            FANAR selects a response based on assessed intake risk
            and current swarm behaviour.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with r3:
        st.markdown("""
        <div class="card">
            <h3>↗️ Redirect</h3>
            <p>
            Controlled flow is used to guide the swarm away from
            the protected intake zone.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # SYSTEM STATUS
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">System Status</div>',
        unsafe_allow_html=True
    )

    systems = [
        ("Early Warning", "Connected"),
        ("Camera", "Active"),
        ("Sonar", "Active"),
        ("Water Sensors", "Active"),
        ("Risk Engine", "Active"),
        ("FANAR F1", "Active"),
        ("FANAR F2", "Active"),
        ("FANAR F3", "Active"),
        ("Continuous Monitoring", "Active")
    ]

    left, right = st.columns(2)

    for index, (name, status) in enumerate(systems):

        target = left if index % 2 == 0 else right

        with target:
            st.markdown(
                f"""
                <div class="system-row">
                    <span class="system-name">{name}</span>
                    <span style="float:right" class="system-active">
                        🟢 {status}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # ACTIVE EVENT
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">Active Event</div>',
        unsafe_allow_html=True
    )

    e1, e2, e3 = st.columns(3)

    with e1:
        st.markdown("""
        <div class="event-card">
            <div class="event-label">EVENT ID</div>
            <div class="event-value">FANAR-2026-001</div>
        </div>
        """, unsafe_allow_html=True)

    with e2:
        st.markdown("""
        <div class="event-card">
            <div class="event-label">SWARM</div>
            <div class="event-value">Detected</div>
        </div>
        """, unsafe_allow_html=True)

    with e3:
        st.markdown("""
        <div class="event-card">
            <div class="event-label">MOVEMENT</div>
            <div class="event-value">Toward intake</div>
        </div>
        """, unsafe_allow_html=True)

    e4, e5, e6 = st.columns(3)

    with e4:
        st.markdown("""
        <div class="event-card">
            <div class="event-label">DISTANCE</div>
            <div class="event-value">320 m</div>
        </div>
        """, unsafe_allow_html=True)

    with e5:
        st.markdown("""
        <div class="event-card">
            <div class="event-label">RISK</div>
            <div class="event-value status-high">HIGH</div>
        </div>
        """, unsafe_allow_html=True)

    with e6:
        st.markdown("""
        <div class="event-card">
            <div class="event-label">RESPONSE</div>
            <div class="event-value">REDIRECT</div>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # CLOSED LOOP
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">Closed-Loop Autonomous Workflow</div>',
        unsafe_allow_html=True
    )

    f1, f2, f3, f4 = st.columns(4)

    with f1:
        st.markdown("""
        <div class="flow-card">
            <div class="flow-icon">👁️</div>
            <div class="flow-title">Detect</div>
            <div class="flow-text">
                Sensors and early-warning data identify swarm presence.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="flow-card">
            <div class="flow-icon">🧠</div>
            <div class="flow-title">Analyze</div>
            <div class="flow-text">
                Swarm movement and intake risk are assessed.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="flow-card">
            <div class="flow-icon">⚙️</div>
            <div class="flow-title">Adapt</div>
            <div class="flow-text">
                Response mode and intensity are selected.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f4:
        st.markdown("""
        <div class="flow-card">
            <div class="flow-icon">🔄</div>
            <div class="flow-title">Verify</div>
            <div class="flow-text">
                Outcome is monitored and the response is adjusted.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # RESPONSE EFFECT CHART
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">Response Effect</div>',
        unsafe_allow_html=True
    )

    response_data = pd.DataFrame({
        "Time": [
            "14:00",
            "14:05",
            "14:10",
            "14:15",
            "14:20",
            "14:25",
            "14:30",
            "14:35"
        ],
        "Swarm Activity": [
            35, 42, 50, 62, 72, 68, 55, 48
        ],
        "Intake Risk": [
            20, 25, 32, 44, 65, 58, 42, 35
        ]
    })

    st.line_chart(
        response_data.set_index("Time")
    )

    st.caption(
        "Simulated demonstration: risk increases as the swarm approaches, "
        "then decreases following the simulated redirect response."
    )


# =========================================================
# SWARM ASSESSMENT
# =========================================================
elif page == "Swarm Assessment":

    st.header("🔎 Swarm Assessment")

    st.write(
        "Adjust the simulated sensor inputs to observe how the FANAR "
        "decision logic responds."
    )

    col1, col2 = st.columns(2)

    with col1:

        intensity = st.slider(
            "Swarm intensity",
            min_value=0,
            max_value=100,
            value=72
        )

        distance = st.slider(
            "Distance to protected intake (m)",
            min_value=50,
            max_value=1000,
            value=320
        )

        confidence = st.slider(
            "Detection confidence (%)",
            min_value=0,
            max_value=100,
            value=91
        )

    with col2:

        direction = st.selectbox(
            "Estimated movement direction",
            [
                "Toward intake",
                "Parallel to intake",
                "Away from intake"
            ]
        )

        water_condition = st.selectbox(
            "Local water condition",
            [
                "Normal",
                "Moderate current",
                "Strong current"
            ]
        )

    # -----------------------------------------------------
    # DECISION LOGIC
    # -----------------------------------------------------
    if intensity >= 70 and direction == "Toward intake":
        risk = "HIGH"
        response = "Redirect"

    elif intensity >= 45:
        risk = "MODERATE"
        response = "Adapt / Monitor"

    else:
        risk = "LOW"
        response = "Monitor"

    st.markdown("---")

    a1, a2, a3 = st.columns(3)

    with a1:

        if risk == "HIGH":
            css = "status-high"
        elif risk == "MODERATE":
            css = "status-medium"
        else:
            css = "status-low"

        st.markdown(
            f"""
            <div class="card">
                <div class="small">ASSESSED RISK</div>
                <h2 class="{css}">{risk}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a2:
        st.markdown(
            f"""
            <div class="card">
                <div class="small">RECOMMENDED RESPONSE</div>
                <h2>{response}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a3:
        st.markdown(
            f"""
            <div class="card">
                <div class="small">DETECTION CONFIDENCE</div>
                <h2>{confidence}%</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("")

    st.markdown(
        """
        <div class="info-box">
        <b>Decision Logic:</b><br><br>
        This prototype uses a transparent rule-based decision layer.
        It is not a trained machine-learning model. The purpose is to
        demonstrate how FANAR can combine swarm conditions and intake
        proximity to select an adaptive response.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# RESPONSE CONTROL
# =========================================================
elif page == "Response Control":

    st.header("⚙️ Response Control")

    st.write(
        "Select a simulated FANAR response mode."
    )

    response_mode = st.radio(
        "Response mode",
        [
            "Guide",
            "Redirect",
            "Collect",
            "Release"
        ],
        horizontal=True
    )

    st.session_state.selected_response = response_mode

    descriptions = {
        "Guide":
            "Use controlled flow to influence swarm movement away from the protected zone.",

        "Redirect":
            "Actively guide the swarm toward a safer path away from the seawater intake.",

        "Collect":
            "Use a localized response to manage concentrated jellyfish aggregation.",

        "Release":
            "Reduce intervention and allow the system to return toward normal monitoring."
    }

    reasons = {
        "Guide":
            "Used when the swarm can be influenced without requiring a stronger intervention.",

        "Redirect":
            "Selected when swarm movement creates an elevated risk to the protected intake.",

        "Collect":
            "Considered for concentrated aggregations requiring localized management.",

        "Release":
            "Used when intake risk has reduced and active intervention is no longer required."
    }

    st.markdown(
        f"""
        <div class="card">
            <h2>{response_mode}</h2>
            <p>{descriptions[response_mode]}</p>
            <hr>
            <p><b>Decision rationale:</b> {reasons[response_mode]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Automation", "Active")

    with c2:
        st.metric("Manual Intervention", "Minimal")

    with c3:
        st.metric("System State", "Monitoring")

    st.markdown("---")

    st.subheader("FANAR Module Status")

    m1, m2, m3 = st.columns(3)

    for col, module in zip(
        [m1, m2, m3],
        ["FANAR F1", "FANAR F2", "FANAR F3"]
    ):
        with col:
            st.markdown(
                f"""
                <div class="success-box">
                    <b>{module}</b><br><br>
                    🟢 Active<br>
                    Controlled response available
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")

    st.subheader("Response Sequence")

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown("""
        <div class="flow-card">
            <div class="flow-icon">📡</div>
            <div class="flow-title">Observe</div>
            <div class="flow-text">
                Receive swarm and environmental inputs.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s2:
        st.markdown("""
        <div class="flow-card">
            <div class="flow-icon">🧠</div>
            <div class="flow-title">Assess</div>
            <div class="flow-text">
                Evaluate risk to the protected intake.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s3:
        st.markdown("""
        <div class="flow-card">
            <div class="flow-icon">⚙️</div>
            <div class="flow-title">Respond</div>
            <div class="flow-text">
                Activate the selected response mode.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s4:
        st.markdown("""
        <div class="flow-card">
            <div class="flow-icon">🔄</div>
            <div class="flow-title">Verify</div>
            <div class="flow-text">
                Monitor the result and adjust if required.
            </div>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# MONITORING DATA
# =========================================================
elif page == "Monitoring Data":

    st.header("📊 Monitoring Data")

    st.write(
        "Simulated sensor and system data for prototype demonstration."
    )

    monitoring_data = pd.DataFrame({
        "Time": [
            "14:00",
            "14:05",
            "14:10",
            "14:15",
            "14:20",
            "14:25",
            "14:30",
            "14:35"
        ],
        "Swarm Intensity": [
            35, 42, 50, 62, 72, 68, 55, 48
        ],
        "Distance (m)": [
            720, 650, 570, 490, 320, 350, 430, 520
        ],
        "Detection Confidence (%)": [
            84, 86, 88, 90, 91, 92, 92, 93
        ],
        "Intake Risk": [
            "Low",
            "Low",
            "Moderate",
            "Moderate",
            "High",
            "Moderate",
            "Moderate",
            "Low"
        ],
        "Response": [
            "Monitor",
            "Monitor",
            "Adapt",
            "Adapt",
            "Redirect",
            "Redirect",
            "Adapt",
            "Monitor"
        ]
    })

    st.dataframe(
        monitoring_data,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("Swarm Activity")

    st.line_chart(
        monitoring_data.set_index("Time")[
            ["Swarm Intensity"]
        ]
    )

    st.subheader("Intake Distance")

    st.line_chart(
        monitoring_data.set_index("Time")[
            ["Distance (m)"]
        ]
    )

    st.markdown("---")

    st.subheader("Sensor Inputs")

    sensor_data = pd.DataFrame({
        "Sensor": [
            "Camera",
            "Sonar",
            "Water Condition Sensor",
            "Swarm Position Estimate"
        ],
        "Status": [
            "Active",
            "Active",
            "Active",
            "Available"
        ],
        "Purpose": [
            "Visual swarm detection",
            "Subsurface swarm awareness",
            "Local environmental conditions",
            "Approximate swarm location"
        ]
    })

    st.dataframe(
        sensor_data,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# ALERTS
# =========================================================
elif page == "Alerts":

    st.header("🚨 Alerts & Decision Log")

    st.markdown("""
    <div class="alert-box">
        <b>🔴 HIGH RISK — Active Event</b><br><br>
        Elevated jellyfish activity has been detected within the
        monitored intake-risk zone. FANAR recommends a Redirect response.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    st.subheader("Current Alert")

    alert1, alert2, alert3 = st.columns(3)

    with alert1:
        st.metric("Swarm Intensity", "72 / 100")

    with alert2:
        st.metric("Distance", "320 m")

    with alert3:
        st.metric("Detection Confidence", "91%")

    st.markdown("---")

    st.subheader("Decision Log")

    decision_log = pd.DataFrame({
        "Time": [
            "14:20",
            "14:21",
            "14:22",
            "14:23",
            "14:25",
            "14:30"
        ],
        "Event": [
            "Swarm detected",
            "Risk assessed",
            "Response selected",
            "FANAR modules activated",
            "Swarm movement reassessed",
            "Risk reduced"
        ],
        "System Action": [
            "Continue monitoring",
            "Risk classified as HIGH",
            "Redirect selected",
            "F1 / F2 / F3 active",
            "Verify response",
            "Continue adaptive monitoring"
        ],
        "Status": [
            "Complete",
            "Complete",
            "Complete",
            "Active",
            "Monitoring",
            "Monitoring"
        ]
    })

    st.dataframe(
        decision_log,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("Autonomous Decision Chain")

    st.markdown(
        """
        **Early Warning Received**
        ↓  
        **Assess Swarm**
        ↓  
        **Determine Intake Risk**
        ↓  
        **Activate Response**
        ↓  
        **Monitor Outcome**
        ↓  
        **Adapt if Required**
        """
    )


# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.caption(
    "Fanar Aqua Guard | ATP 2026 | AI-assisted jellyfish swarm "
    "management prototype | Demonstration interface — simulated data only"
)
