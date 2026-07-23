import os
import streamlit as st

# Configure page layout and title
st.set_page_config(
    page_title="Goalkeeper Performance Analysis",
    page_icon="⚽",
    layout="wide"
)

# Header Section
st.title("⚽ Goalkeeper Performance Analysis Dashboard")
st.markdown("---")

# Video Section (Side-by-side layout)
st.header("📹 Video Analysis")

col1, col2 = st.columns(2)

video_1_path = "Event_1_web.mp4"
video_2_path = "Pitch_Tactical_Flipped_under25mb.mp4"

with col1:
    st.subheader("Event Analysis")
    if os.path.exists(video_1_path):
        st.video(video_1_path)
    else:
        st.error(f"Video file not found: `{video_1_path}`")

with col2:
    st.subheader("Pitch Tactical Analysis")
    if os.path.exists(video_2_path):
        st.video(video_2_path)
    else:
        st.error(f"Video file not found: `{video_2_path}`")

st.markdown("---")

# Report Section
st.header("📊 Performance Report")

report_path = "Goalkeeper_Performance_Report_v2.md"

if os.path.exists(report_path):
    with open(report_path, "r", encoding="utf-8") as file:
        report_md = file.read()
    st.markdown(report_md, unsafe_allow_html=True)
else:
    st.warning(f"Report file not found: `{report_path}`")
