import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="Fanar Aqua Guard",
    page_icon="🪼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>
    .stApp {
        background: #07141d;
        color: #e8f5f7;
    }

    [data-testid="stSidebar"] {
        background: #061019;
        border-right: 1px solid #18313d;
    }

    .main-title {
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        color: #8fb8c3;
        font-size: 16px;
        margin-top: 3px;
    }

    .demo-banner {
        background: #102b35;
        border: 1px solid #245564;
        border-radius: 10px;
        padding: 12px 16px;
        margin: 18px 0;
        color: #bfe8ef;
    }

    .card {
        background: #0c202b;
        border: 1px solid #193b48;
        border-radius: 12px;
        padding: 18px;
        min-height: 120px;
    }

    .card-title {
        color: #82aeb9;
        font-size: 14px;
        margin-bottom: 7px;
    }

    .card-value {
        font-size: 27px;
        font-weight: 750;
    }

    .card-small {
        color: #8fb8c3;
        font-size: 13px;
        margin-top: 5px;
    }

    .status-good {
        color: #67e8a5;
    }

    .status-warning {
        color: #ffd166;
    }

    .status-danger {
        color: #ff7b7b;
    }

    .section-title {
        font-size: 22px;
        font-weight: 750;
        margin-top: 25px;
        margin-bottom: 12px;
    }

    .workflow {
        background: #0b1e28;
        border: 1px solid #1b3d49;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        height: 130px;
    }

    .workflow-icon {
        font-size: 30px;
    }

    .workflow-name {
        font-weight: 700;
        margin-top: 5px;
    }

    .workflow-desc {
        color: #86aab4;
        font-size: 12px;
    }

    .arrow {
        text-align: center;
        font-size: 28px;
        padding-top: 40px;
        color: #4e8b9a;
    }

    .intake-box {
        background: #0a2530;
        border: 2px solid #2c6878;
        border-radius: 15px;
        padding: 24px;
        text-align: center;
    }

    .swarm-box {
        background: #251b27;
        border: 2px solid #704c69;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }

    .response-box {
        background: #10291f;
        border: 2px solid #327052;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }

    .big-icon {
        font-size: 45px;
    }

    .metric-label {
        color: #8fb8c3;
        font-size: 13px;
    }

    .metric-value {
        font-size: 25px;
        font-weight: 750;
    }

    .footer {
        text-align: center;
        color: #607e87;
        font-size: 12px;
        padding: 35px 0 15px 0;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# SIMULATED DATA
# ============================================================

times = [
    "08:00", "09:00", "10:00", "11:00",
    "12:00", "13:00", "14:00", "15:00"
]

jellyfish_activity = [12, 17, 22, 31, 43, 52, 47, 38]
intake_risk = [8, 12, 18, 27, 39, 55, 48, 34]

monitoring_df = pd.DataFrame({
    "Time": times,
    "Jellyfish Activity": jellyfish_activity,
    "Intake Risk": intake_risk
})


# ============================================================
# SIDEBAR
# ============================================================

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

st.sidebar.markdown("### System Mode")
st.sidebar.success("🟢 Prototype Monitoring")

st.sidebar.markdown("### Prototype")
st.sidebar.caption(
    "Demo data is simulated and is used only "
    "to demonstrate the dashboard workflow."
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🪼 Fanar Aqua Guard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Autonomous Jellyfish Swarm Management & Seawater Intake Protection</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="demo-banner">
    ⚠️ <b>DEMONSTRATION MODE</b> — All readings shown in this prototype are simulated.
    The interface demonstrates the proposed sensing, decision and response workflow.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.markdown('<div class="section-title">System Overview</div>',
                unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
            <div class="card-title">SWARM STATUS</div>
            <div class="card-value">Detected</div>
            <div class="card-small">Early warning received</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <div class="card-title">INTAKE RISK</div>
            <div class="card-value status-warning">Moderate</div>
            <div class="card-small">Requires active monitoring</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <div class="card-title">CURRENT RESPONSE</div>
            <div class="card-value">Redirect</div>
            <div class="card-small">Adaptive response active</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="card">
            <div class="card-title">AUTOMATION</div>
            <div class="card-value status-good">Active</div>
            <div class="card-small">Minimal manual intervention</div>
        </div>
        """, unsafe_allow_html=True)


# --------------------------------------------------------
# MAIN VISUAL — FANAR PHYSICAL RESPONSE
# --------------------------------------------------------

st.markdown(
    '<div class="section-title">Live FANAR Response Zone</div>',
    unsafe_allow_html=True
)

st.caption(
    "Simulated view of the proposed autonomous response around the protected seawater intake."
)

st.markdown("""
<div style="
    background: linear-gradient(180deg, #08232d 0%, #061820 100%);
    border: 1px solid #245564;
    border-radius: 18px;
    padding: 28px;
    min-height: 390px;
">

<div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:25px;
">

<div>
    <div style="font-size:13px;color:#7faab5;">EVENT STATUS</div>
    <div style="font-size:25px;font-weight:800;">🟢 RESPONSE ACTIVE</div>
</div>

<div style="text-align:right;">
    <div style="font-size:13px;color:#7faab5;">CURRENT MODE</div>
    <div style="font-size:25px;font-weight:800;">↗️ REDIRECT</div>
</div>

</div>

<div style="
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:18px;
">

<!-- SWARM -->

<div style="
    background:#281b28;
    border:2px solid #714d6c;
    border-radius:16px;
    padding:22px;
    width:25%;
    text-align:center;
">

<div style="font-size:42px;">🪼🪼🪼</div>

<div style="font-size:20px;font-weight:800;">
INCOMING SWARM
</div>

<div style="color:#a9c0c6;font-size:13px;margin-top:7px;">
Movement: → Intake
</div>

<div style="color:#ffd166;font-size:13px;margin-top:5px;">
Intensity: HIGH
</div>

</div>


<!-- FLOW -->

<div style="
    width:12%;
    text-align:center;
">

<div style="
    font-size:32px;
    color:#6dc7d8;
">
→ → →
</div>

<div style="
    font-size:11px;
    color:#83aeb8;
">
PREDICTED PATH
</div>

</div>


<!-- FANAR MODULES -->

<div style="
    background:#102b35;
    border:2px solid #367889;
    border-radius:16px;
    padding:22px;
    width:27%;
    text-align:center;
">

<div style="font-size:38px;">
🟦 🟦 🟦
</div>

<div style="font-size:20px;font-weight:800;">
FANAR MODULES
</div>

<div style="color:#a9c0c6;font-size:13px;margin-top:7px;">
Adaptive positioning
</div>

<div style="color:#67e8a5;font-size:13px;margin-top:5px;">
Controlled redirection active
</div>

</div>


<!-- REDIRECTION -->

<div style="
    width:12%;
    text-align:center;
">

<div style="
    font-size:32px;
    color:#67e8a5;
">
↗ ↗ ↗
</div>

<div style="
    font-size:11px;
    color:#83aeb8;
">
SAFE PATH
</div>

</div>


<!-- INTAKE -->

<div style="
    background:#0b2731;
    border:2px solid #347284;
    border-radius:16px;
    padding:22px;
    width:24%;
    text-align:center;
">

<div style="font-size:42px;">
🌊
</div>

<div style="font-size:20px;font-weight:800;">
SEAWATER INTAKE
</div>

<div style="color:#a9c0c6;font-size:13px;margin-top:7px;">
Protected zone
</div>

<div style="color:#67e8a5;font-size:13px;margin-top:5px;">
Exposure: REDUCED
</div>

</div>

</div>

<div style="
    margin-top:25px;
    padding-top:18px;
    border-top:1px solid #21414b;
    display:flex;
    justify-content:space-around;
    text-align:center;
">

<div>
    <div style="color:#7faab5;font-size:12px;">
    MODULE STATUS
    </div>
    <b>3 / 3 ACTIVE</b>
</div>

<div>
    <div style="color:#7faab5;font-size:12px;">
    AUTOMATION
    </div>
    <b style="color:#67e8a5;">ACTIVE</b>
</div>

<div>
    <div style="color:#7faab5;font-size:12px;">
    MANUAL INTERVENTION
    </div>
    <b>MINIMAL</b>
</div>

<div>
    <div style="color:#7faab5;font-size:12px;">
    RESPONSE STATE
    </div>
    <b style="color:#67e8a5;">MONITORING</b>
</div>

</div>

</div>
""", unsafe_allow_html=True)


    # --------------------------------------------------------
    # WORKFLOW
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Closed-Loop Response Workflow</div>',
        unsafe_allow_html=True
    )

    w1, a1, w2, a2, w3, a3, w4 = st.columns(
        [1, 0.25, 1, 0.25, 1, 0.25, 1]
    )

    with w1:
        st.markdown("""
        <div class="workflow">
            <div class="workflow-icon">📡</div>
            <div class="workflow-name">DETECT</div>
            <div class="workflow-desc">Receive warning + sensor data</div>
        </div>
        """, unsafe_allow_html=True)

    with a1:
        st.markdown('<div class="arrow">→</div>', unsafe_allow_html=True)

    with w2:
        st.markdown("""
        <div class="workflow">
            <div class="workflow-icon">🧠</div>
            <div class="workflow-name">ANALYZE</div>
            <div class="workflow-desc">Estimate movement + risk</div>
        </div>
        """, unsafe_allow_html=True)

    with a2:
        st.markdown('<div class="arrow">→</div>', unsafe_allow_html=True)

    with w3:
        st.markdown("""
        <div class="workflow">
            <div class="workflow-icon">⚙️</div>
            <div class="workflow-name">ADAPT</div>
            <div class="workflow-desc">Coordinate response modules</div>
        </div>
        """, unsafe_allow_html=True)

    with a3:
        st.markdown('<div class="arrow">→</div>', unsafe_allow_html=True)

    with w4:
        st.markdown("""
        <div class="workflow">
            <div class="workflow-icon">↗️</div>
            <div class="workflow-name">VERIFY</div>
            <div class="workflow-desc">Observe and adjust</div>
        </div>
        """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # GRAPH
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Swarm Activity & Intake Risk</div>',
        unsafe_allow_html=True
    )

    chart_df = monitoring_df.set_index("Time")

    st.line_chart(
        chart_df,
        height=320
    )


    # --------------------------------------------------------
    # EVENT
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Current Event</div>',
        unsafe_allow_html=True
    )

    e1, e2, e3 = st.columns(3)

    with e1:
        st.markdown("""
        <div class="card">
            <div class="card-title">🪼 SWARM</div>
            <div class="card-value">Elevated</div>
            <div class="card-small">
            Direction: Toward protected zone<br>
            Confidence: Demo value
            </div>
        </div>
        """, unsafe_allow_html=True)

    with e2:
        st.markdown("""
        <div class="card">
            <div class="card-title">⚠️ INTAKE EXPOSURE</div>
            <div class="card-value status-warning">Moderate</div>
            <div class="card-small">
            Continuous monitoring active<br>
            Protection response engaged
            </div>
        </div>
        """, unsafe_allow_html=True)

    with e3:
        st.markdown("""
        <div class="card">
            <div class="card-title">🤖 AUTOMATION</div>
            <div class="card-value status-good">Active</div>
            <div class="card-small">
            Response: Redirect<br>
            Manual intervention: Minimal
            </div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# SWARM ASSESSMENT
# ============================================================

elif page == "Swarm Assessment":

    st.markdown("## 🔎 Swarm Assessment")

    st.info(
        "This page demonstrates how local sensor information could "
        "support swarm-risk assessment. Values are simulated."
    )

    col1, col2 = st.columns(2)

    with col1:

        intensity = st.slider(
            "Swarm intensity",
            0,
            100,
            72
        )

        distance = st.slider(
            "Distance to protected intake (demo)",
            10,
            1000,
            320
        )

        confidence = st.slider(
            "Detection confidence",
            0,
            100,
            91
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
                "Changing",
                "High flow variation"
            ]
        )

        if intensity >= 70 and direction == "Toward intake":
            risk = "HIGH"
            recommendation = "Redirect"
        elif intensity >= 45:
            risk = "MODERATE"
            recommendation = "Adapt / Monitor"
        else:
            risk = "LOW"
            recommendation = "Monitor"

        st.markdown("### Assessment Result")

        st.metric("Risk level", risk)
        st.metric("Recommended response", recommendation)

    st.markdown("---")

    st.markdown("### Decision Logic")

    st.write(
        "The prototype combines swarm intensity, estimated movement "
        "direction and proximity to the protected intake to demonstrate "
        "a response decision."
    )

    st.warning(
        "This is a transparent prototype rule set, not a trained "
        "machine-learning model."
    )


# ============================================================
# RESPONSE CONTROL
# ============================================================

elif page == "Response Control":

    st.markdown("## 🔄 Response Control")

    st.info(
        "Prototype control panel. These controls simulate the proposed "
        "response logic and do not operate real equipment."
    )

    response = st.radio(
        "Select response mode",
        [
            "Guide",
            "Redirect",
            "Collect",
            "Release"
        ],
        index=1,
        horizontal=True
    )

    if response == "Redirect":
        explanation = (
            "Adaptive flow is directed to guide the swarm away "
            "from the protected intake zone."
        )
    elif response == "Guide":
        explanation = (
            "Modules are positioned to influence swarm movement "
            "toward a safer open-water direction."
        )
    elif response == "Collect":
        explanation = (
            "Collection is represented as an alternative response "
            "when redirection is insufficient."
        )
    else:
        explanation = (
            "Release represents returning collected organisms "
            "to a safer open-water area."
        )

    st.success(f"Active response: {response}")

    st.markdown(f"### Response explanation\n{explanation}")

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Automation", "Active")

    with c2:
        st.metric("Manual intervention", "Minimal")

    with c3:
        st.metric("System state", "Monitoring")

    st.markdown("---")

    st.markdown("### Closed-Loop Response")

    steps = [
        ("01", "Observe", "Receive updated swarm position"),
        ("02", "Compare", "Check exposure against protected zone"),
        ("03", "Adjust", "Modify response direction"),
        ("04", "Verify", "Observe whether swarm moves away")
    ]

    for number, title, description in steps:
        st.markdown(
            f"""
            <div class="card" style="margin-bottom:10px;">
                <b>{number} — {title}</b><br>
                <span style="color:#8fb8c3;">{description}</span>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# MONITORING DATA
# ============================================================

elif page == "Monitoring Data":

    st.markdown("## 📊 Monitoring Data")

    st.info(
        "All values below are simulated demonstration data."
    )

    st.dataframe(
        monitoring_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### Activity Trend")

    st.line_chart(
        monitoring_df.set_index("Time")["Jellyfish Activity"],
        height=280
    )

    st.markdown("### Intake Risk Trend")

    st.line_chart(
        monitoring_df.set_index("Time")["Intake Risk"],
        height=280
    )

    st.markdown("### Prototype Sensor Inputs")

    sensor_df = pd.DataFrame({
        "Input": [
            "Swarm intensity",
            "Estimated direction",
            "Distance to intake",
            "Detection confidence",
            "Water condition"
        ],
        "Status": [
            "Elevated",
            "Toward intake",
            "320 m",
            "91%",
            "Normal"
        ]
    })

    st.dataframe(
        sensor_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# ALERTS
# ============================================================

elif page == "Alerts":

    st.markdown("## 🚨 Alerts & Decision Log")

    alerts = [
        ("13:00", "WARNING", "Elevated swarm activity detected"),
        ("13:05", "RISK", "Swarm movement trending toward protected intake"),
        ("13:07", "ACTION", "Redirect response activated"),
        ("13:12", "MONITOR", "Swarm movement being reassessed"),
        ("13:18", "VERIFY", "Response effectiveness under observation")
    ]

    for timestamp, level, message in alerts:

        if level == "WARNING":
            icon = "⚠️"
        elif level == "RISK":
            icon = "🔴"
        elif level == "ACTION":
            icon = "🔄"
        else:
            icon = "🟢"

        st.markdown(
            f"""
            <div class="card" style="margin-bottom:10px;">
                <b>{icon} {timestamp} — {level}</b><br>
                <span style="color:#9ab7bf;">{message}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown("### Current Decision")

    st.success(
        "Redirect response remains active while the system "
        "continues to monitor swarm movement."
    )

    st.caption(
        "Prototype only — no real operational equipment is connected."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Fanar Aqua Guard | ATP 2026 | AI-assisted jellyfish swarm management prototype<br>
        Demonstration interface — simulated data only
    </div>
    """,
    unsafe_allow_html=True
)
