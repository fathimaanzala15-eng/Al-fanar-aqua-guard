import streamlit as st
import pandas as pd
import numpy as np
import time

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="FANAR | Autonomous Marine Protection",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROFESSIONAL THEME
# =========================================================

st.markdown(
    """
    <style>
        .stApp {
            background-color: #07131D;
            color: #E8F1F5;
        }

        section[data-testid="stSidebar"] {
            background-color: #081923;
            border-right: 1px solid #1D3442;
        }

        .block-container {
            max-width: 1450px;
            padding-top: 2rem;
        }

        h1, h2, h3 {
            color: #EAF5F8 !important;
        }

        .small-label {
            color: #7193A3;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .muted {
            color: #8BA5B2;
        }

        .accent {
            color: #54D3E8;
        }

        .success {
            color: #56D69A;
        }

        .warning {
            color: #F3C969;
        }

        .danger {
            color: #FF6B6B;
        }

        .card {
            background-color: #0B1D28;
            border: 1px solid #1C3847;
            border-radius: 12px;
            padding: 18px;
            margin-bottom: 14px;
        }

        .metric-card {
            background-color: #0B1D28;
            border: 1px solid #1C3847;
            border-radius: 12px;
            padding: 18px;
            min-height: 125px;
        }

        .metric-title {
            color: #7895A3;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .metric-value {
            color: #EDF7FA;
            font-size: 1.65rem;
            font-weight: 700;
            margin-top: 8px;
        }

        .metric-sub {
            color: #7693A0;
            font-size: 0.78rem;
            margin-top: 5px;
        }

        .status-dot {
            font-size: 0.8rem;
        }

        .header-line {
            border-bottom: 1px solid #1B3442;
            margin: 10px 0 25px 0;
        }

        .system-panel {
            background-color: #091A24;
            border: 1px solid #1B3A49;
            border-radius: 14px;
            padding: 22px;
        }

        .module {
            background-color: #0D2430;
            border: 1px solid #244858;
            border-radius: 10px;
            padding: 14px;
            text-align: center;
        }

        .module-name {
            font-weight: 700;
            color: #DCECF1;
        }

        .module-status {
            color: #55D69A;
            font-size: 0.75rem;
            margin-top: 5px;
        }

        .footer {
            text-align: center;
            color: #526D79;
            font-size: 0.72rem;
            padding-top: 35px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIMULATED OPERATIONAL DATA
# =========================================================

swarm_intensity = 72
swarm_density = 68
distance_to_intake = 320
confidence = 91
current_speed = 0.8
water_temperature = 28.4
direction = "Toward intake"

if swarm_intensity >= 70 and direction == "Toward intake":
    risk_level = "HIGH"
    response_mode = "REDIRECT"
elif swarm_intensity >= 45:
    risk_level = "MODERATE"
    response_mode = "ADAPT"
else:
    risk_level = "LOW"
    response_mode = "MONITOR"

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## FANAR")
    st.caption("Autonomous Marine Protection System")

    st.divider()

    page = st.radio(
        "OPERATIONS",
        [
            "Command Center",
            "Swarm Assessment",
            "Response Control",
            "Monitoring",
            "Incident Log"
        ]
    )

    st.divider()

    st.caption("ATP / ENEC ChallengeON 2026")

    st.caption("Prototype Environment")

# =========================================================
# COMMAND CENTER
# =========================================================

if page == "Command Center":

    st.title("FANAR Operations Center")

    st.markdown(
        "Autonomous jellyfish-swarm management for protection of "
        "seawater intake infrastructure."
    )

    st.markdown(
        '<div class="header-line"></div>',
        unsafe_allow_html=True
    )

    st.info(
        "PROTOTYPE ENVIRONMENT  •  Sensor inputs shown are simulated "
        "for demonstration purposes."
    )

    # -----------------------------------------------------
    # TOP METRICS
    # -----------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Swarm Condition</div>
                <div class="metric-value">DETECTED</div>
                <div class="metric-sub">
                    Intensity {swarm_intensity}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Intake Risk</div>
                <div class="metric-value danger">
                    {risk_level}
                </div>
                <div class="metric-sub">
                    {distance_to_intake} m from protected zone
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Autonomous Response</div>
                <div class="metric-value accent">
                    {response_mode}
                </div>
                <div class="metric-sub">
                    Direction: {direction}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-title">System State</div>
                <div class="metric-value success">
                    ONLINE
                </div>
                <div class="metric-sub">
                    Continuous monitoring active
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Autonomous Decision Path")

    # -----------------------------------------------------
    # OPERATIONAL FLOW
    # -----------------------------------------------------

    flow1, flow2, flow3, flow4, flow5 = st.columns(5)

    flow_items = [
        ("01", "DETECT", "Early warning received"),
        ("02", "ANALYZE", "Movement assessed"),
        ("03", "PREDICT", "Intake risk evaluated"),
        ("04", "ADAPT", "Response selected"),
        ("05", "VERIFY", "Outcome monitored")
    ]

    columns = [flow1, flow2, flow3, flow4, flow5]

    for column, item in zip(columns, flow_items):

        number, title, description = item

        with column:

            st.markdown(
                f"""
                <div class="card">
                    <div class="small-label">{number}</div>
                    <h4>{title}</h4>
                    <div class="muted">
                        {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # MARINE OPERATIONAL VIEW
    # -----------------------------------------------------

    st.markdown("### Marine Operational View")

    left, center, right = st.columns([1, 2, 1])

    with left:

        st.markdown(
            """
            <div class="system-panel">

            <div class="small-label">
            SWARM
            </div>

            <h3>Jellyfish Aggregation</h3>

            <p class="muted">
            Elevated swarm density detected within the
            monitored approach corridor.
            </p>

            <p>
            <b>Intensity:</b> 72%<br>
            <b>Density:</b> 68%<br>
            <b>Confidence:</b> 91%
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with center:

        st.markdown(
            """
            <div class="system-panel">

            <div class="small-label">
            RESPONSE CORRIDOR
            </div>

            <h3>Adaptive Redirection</h3>

            <p class="muted">
            FANAR modules coordinate a controlled response
            to reduce swarm accumulation near the protected
            intake zone.
            </p>

            """,
            unsafe_allow_html=True
        )

        progress = st.progress(68)

        st.caption(
            "Simulated response effectiveness indicator"
        )

        st.markdown(
            """
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.markdown(
            """
            <div class="system-panel">

            <div class="small-label">
            PROTECTED ASSET
            </div>

            <h3>Seawater Intake</h3>

            <p class="muted">
            Protected operational zone.
            </p>

            <p>
            <b>Status:</b>
            <span class="success"> Protected</span>
            </p>

            <p>
            <b>Distance:</b> 320 m
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # FANAR MODULES
    # -----------------------------------------------------

    st.markdown("### FANAR Response Modules")

    m1, m2, m3 = st.columns(3)

    for column, module, role in [
        (m1, "F1", "Forward response"),
        (m2, "F2", "Adaptive positioning"),
        (m3, "F3", "Boundary protection")
    ]:

        with column:

            st.markdown(
                f"""
                <div class="module">

                <div class="module-name">
                {module}
                </div>

                <div class="module-status">
                ● ACTIVE
                </div>

                <div class="muted">
                {role}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # LIVE SIMULATION
    # -----------------------------------------------------

    st.markdown("### Autonomous Response Simulation")

    if st.button(
        "Run Response Simulation",
        type="primary",
        use_container_width=True
    ):

        progress = st.progress(0)
        status = st.empty()

        stages = [
            ("Detecting swarm", 20),
            ("Analyzing movement", 40),
            ("Evaluating intake risk", 60),
            ("Activating FANAR modules", 80),
            ("Verifying response", 100)
        ]

        for message, value in stages:

            status.info(message)
            progress.progress(value)
            time.sleep(0.5)

        status.success(
            "Response cycle completed. Continuous monitoring remains active."
        )

    # -----------------------------------------------------
    # TREND
    # -----------------------------------------------------

    st.markdown("### Operational Trend")

    trend = pd.DataFrame(
        {
            "Swarm Activity": [42, 49, 57, 65, 72, 74, 61, 48],
            "Intake Risk": [18, 24, 31, 42, 55, 67, 49, 30]
        },
        index=[
            "T-35",
            "T-30",
            "T-25",
            "T-20",
            "T-15",
            "T-10",
            "T-05",
            "NOW"
        ]
    )

    st.line_chart(trend)

# =========================================================
# SWARM ASSESSMENT
# =========================================================

elif page == "Swarm Assessment":

    st.title("Swarm Assessment")

    st.markdown(
        "Operational assessment of swarm characteristics and "
        "potential exposure to the protected intake."
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        intensity = st.slider(
            "Swarm Intensity",
            0,
            100,
            72
        )

        density = st.slider(
            "Swarm Density",
            0,
            100,
            68
        )

        distance = st.slider(
            "Distance to Protected Intake (m)",
            50,
            2000,
            320
        )

    with right:

        detection_confidence = st.slider(
            "Detection Confidence",
            0,
            100,
            91
        )

        movement = st.selectbox(
            "Estimated Movement",
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
                "Elevated current",
                "Low current",
                "Turbulent"
            ]
        )

    if intensity >= 70 and movement == "Toward intake":

        assessment = "HIGH"
        recommendation = "REDIRECT"

    elif intensity >= 45:

        assessment = "MODERATE"
        recommendation = "ADAPT"

    else:

        assessment = "LOW"
        recommendation = "MONITOR"

    st.divider()

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric("Risk Classification", assessment)

    with r2:
        st.metric("Recommended Response", recommendation)

    with r3:
        st.metric(
            "Detection Confidence",
            f"{detection_confidence}%"
        )

    st.warning(
        "Prototype decision engine: rule-based demonstration logic. "
        "A field deployment would require validated thresholds, "
        "environmental calibration and operational approval."
    )

# =========================================================
# RESPONSE CONTROL
# =========================================================

elif page == "Response Control":

    st.title("Response Control")

    st.markdown(
        "Configure the response strategy selected for the current "
        "swarm condition."
    )

    st.divider()

    response = st.radio(
        "Response Mode",
        [
            "Guide",
            "Redirect",
            "Collect",
            "Release"
        ],
        horizontal=True
    )

    response_description = {
        "Guide":
            "Guide the swarm toward a lower-risk trajectory.",

        "Redirect":
            "Generate a controlled response to reduce accumulation "
            "near the protected intake.",

        "Collect":
            "Coordinate modular collection where appropriate "
            "and environmentally permitted.",

        "Release":
            "Release collected organisms under controlled conditions."
    }

    st.info(response_description[response])

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Automation", "ACTIVE")

    with c2:
        st.metric("Manual Intervention", "MINIMAL")

    with c3:
        st.metric("Control Loop", "CLOSED")

    st.markdown("### Module Status")

    modules = pd.DataFrame(
        {
            "Module": ["F1", "F2", "F3"],
            "Role": [
                "Forward response",
                "Adaptive positioning",
                "Boundary protection"
            ],
            "Status": [
                "ACTIVE",
                "ACTIVE",
                "ACTIVE"
            ]
        }
    )

    st.dataframe(
        modules,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# MONITORING
# =========================================================

elif page == "Monitoring":

    st.title("Monitoring")

    st.markdown(
        "Simulated environmental and operational data stream."
    )

    st.divider()

    timestamps = pd.date_range(
        "2026-10-10 10:00",
        periods=12,
        freq="5min"
    )

    monitoring = pd.DataFrame(
        {
            "Jellyfish Activity": [
                38, 42, 47, 53, 59, 65,
                70, 74, 69, 61, 52, 44
            ],

            "Intake Risk": [
                15, 18, 23, 29, 37, 46,
                56, 66, 59, 47, 34, 24
            ],

            "Detection Confidence": [
                84, 85, 87, 88, 89, 90,
                91, 92, 92, 91, 90, 89
            ]
        },
        index=timestamps
    )

    st.line_chart(monitoring)

    st.divider()

    sensor_data = pd.DataFrame(
        {
            "Sensor": [
                "Camera",
                "Sonar",
                "Water Temperature",
                "Current Sensor",
                "Swarm Position"
            ],

            "Reading": [
                "Aggregation detected",
                "High-density return",
                "28.4 °C",
                "0.8 m/s",
                "320 m from intake"
            ],

            "Status": [
                "ONLINE",
                "ONLINE",
                "ONLINE",
                "ONLINE",
                "ONLINE"
            ]
        }
    )

    st.dataframe(
        sensor_data,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# INCIDENT LOG
# =========================================================

elif page == "Incident Log":

    st.title("Incident Log")

    st.markdown(
        "Chronological record of the current demonstration event."
    )

    st.divider()

    incidents = pd.DataFrame(
        {
            "Time": [
                "10:00",
                "10:05",
                "10:10",
                "10:15",
                "10:20"
            ],

            "Event": [
                "Early warning received",
                "Swarm movement analyzed",
                "Intake risk classified",
                "Redirect response activated",
                "Response outcome verified"
            ],

            "System": [
                "Early Warning",
                "Risk Engine",
                "Risk Engine",
                "FANAR Modules",
                "Monitoring"
            ],

            "Status": [
                "COMPLETE",
                "COMPLETE",
                "HIGH RISK",
                "ACTIVE",
                "VERIFIED"
            ]
        }
    )

    st.dataframe(
        incidents,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.error(
        "HIGH-RISK EVENT — Swarm movement is currently toward "
        "the protected seawater intake."
    )

    st.info(
        "FANAR response: REDIRECT. The control loop remains active "
        "and continuously evaluates updated conditions."
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        FANAR AQUA GUARD  •  ATP / ENEC ChallengeON 2026<br>
        Autonomous jellyfish-swarm management and seawater intake protection<br>
        Demonstration interface — simulated data
    </div>
    """,
    unsafe_allow_html=True
)
