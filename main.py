import streamlit as st
from utils.text_detector import detect_fake_text
from utils.image_detector import detect_deepfake_image
from utils.history_logger import log_result, get_history
from utils.video_detector import detect_deepfake_video  # ✅ New import
from utils.source_checker import check_source_reliability


st.set_page_config(page_title="TruthSentinel AI — Deepfake & Misinformation Detector", page_icon="static/india_flag.png")

# Sidebar content
with st.sidebar:
    st.image("static/india_flag.png", width=120)
    st.title("🛡️ TruthSentinel AI")
    st.markdown("""
    ### About this Project  
    **TruthSentinel: AI vs AI** is a prototype tool for detecting potential deepfake or misinformation in text, image, and soon video content.  

    **Current Features:**  
    - 📖 Text deepfake detection  
    - 🖼️ Image deepfake detection (placeholder)  
    - 📹 Video deepfake detection (placeholder)  
    - 📜 Detection history log  

    **Upcoming Plans:**  
    - Real AI detection models  
    - Source reliability scoring  

    **Contact / GitHub**  
    [View Project Repo](https://github.com/AKSHATKUAMRSINGH/TruthSentinel-AI-vs-AI-Detecting-Deepfake-Misinformation)  
    """)

    st.write("---")
    st.markdown("Made in 🇮🇳 with ❤️")

st.image("static/Banner.jpg", use_container_width=True)

st.title("TruthSentinel: AI vs AI — Detecting Deepfake & Misinformation")
st.write("This AI tool detects fake or misleading text, image, and video content.")

# Text detection section
st.subheader("📝 Text Deepfake Detection")
user_input = st.text_area("Enter your text here:")

if st.button("Analyze Text"):
    if user_input:
        result = detect_fake_text(user_input)
        st.write(result)

        # Log the result
        log_result({
            "type": "text",
            "input": user_input,
            "result": result
        })
    else:
        st.write("⚠️ Please enter some text before analyzing.")

# Image detection section
st.subheader("🖼️ Image Deepfake Detection")
uploaded_image = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

if st.button("Analyze Image"):
    if uploaded_image:
        with open("data/temp_uploaded_image.png", "wb") as f:
            f.write(uploaded_image.read())
        result = detect_deepfake_image("data/temp_uploaded_image.png")
        st.write(f"🛡️ Verdict: {result['verdict']}")
        st.write(f"🧪 Confidence Score: {result['confidence']}")

        # Log the result
        log_result({
            "type": "image",
            "input": uploaded_image.name,
            "result": result['verdict']
        })
    else:
        st.write("⚠️ Please upload an image before analyzing.")

# 📹 Video deepfake detection section (NEW)
# Video deepfake detection section
with st.expander("🔍 Video Deepfake Detection"):
    uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "avi"])

    if st.button("Analyze Video"):
        if uploaded_video:
            result = detect_deepfake_video(uploaded_video)
            st.success(f"Verdict: {result['verdict']} ({result['confidence']})")

            # Log the result
            log_result({
                "type": "video",
                "input": uploaded_video.name,
                "result": result['verdict']
            })
        else:
            st.write("⚠️ Please upload a video before analyzing.")


# Source reliability check section
with st.expander("🌐 Source Link Reliability Check"):
    url_input = st.text_input("Enter a source URL (e.g. https://thehindu.com/some-news)")

    if st.button("Check Source Reliability"):
        if url_input:
            result = check_source_reliability(url_input)
            st.write(f"📝 Verdict: {result['verdict']}")
            st.write(f"🔍 Confidence Score: {result['confidence']}")

            # Log the result
            log_result({
                "type": "source",
                "input": url_input,
                "result": result['verdict']
            })
        else:
            st.write("⚠️ Please enter a URL to check.")


# 📜 View past history section
with st.expander("📜 View Past Detection History"):
    history = get_history()
    if history:
        for item in reversed(history[-10:]):
            st.write(f"**{item['timestamp']}** — *{item['type'].capitalize()}*: {item['result']}")
    else:
        st.write("No past history available yet.")
