TruthSentinel: AI vs AI — Detecting Deepfake & Misinformation 🛡️
An AI-powered, modular web application designed to detect deepfake content and misinformation in text, with future-ready support for image, video, and audio detection.

📌 Project Overview
TruthSentinel is a scalable AI tool to help combat misinformation and AI-generated deepfakes. Built with Python and Streamlit, the app currently detects fake or misleading text content with a confidence score and clean, interactive UI.

✅ Current Features (June 2025)
🔍 Text-Based Misinformation Detection

Analyze user-input text for legitimacy.

Mock probability score (placeholder model for now).

Detects and flags misleading statements.

🖼️ Image Deepfake Detector Placeholder

Upload image interface prepared.

Placeholder message — real model to be integrated later.

🎨 Custom Streamlit UI Enhancements

Project title, Indian flag favicon 🇮🇳, head banner.

Light theme with personalized color palette.

Modular, clean folder structure for scalable development.

⚙️ Streamlit config.toml Customization

Port management, CORS disabled, error toolbar minimized.

📁 Current Folder Structure
bash
Copy
Edit
TruthSentinel/
├── data/              # For storing datasets (future)
├── env/               # Virtual environment (DO NOT COMMIT)
├── models/            # Placeholder for trained models
├── static/            # Images, CSS, etc.
│   └── india_flag.png
├── templates/         # Future HTML templates
├── utils/
│   └── text_detector.py
│   └── image_detector.py
├── main.py            # Main Streamlit app
└── config.toml        # Streamlit config
🚀 Planned Features (Upcoming)
📝 Result History Log
Save all detection results locally for review.

🧭 About / Help Sidebar
Project description, links, and usage guide.

📸 Actual Image Deepfake Detection
Integrate a pretrained CNN or vision model for real detection.

📹 Video Deepfake Detection
Extend to video frame analysis.

🎵 Audio Deepfake Detection
Detect synthetic voice or AI-generated audio.

🗂️ Multi-language Support
Future addition for Hindi and other regional content.

🌐 Public Web Deployment
Possibly via Streamlit Community Cloud or custom server.

🛠️ Tech Stack
Python 3.11+

Streamlit

NLTK

Custom config.toml

(Future: TensorFlow / PyTorch, OpenCV, DeepFace etc.)

📦 Installation & Run
bash
Copy
Edit
# Clone repository
git clone https://github.com/AKSHATKUAMRSINGH/TruthSentinel.git  
cd TruthSentinel

# Create virtual environment
python -m venv env
.\env\Scripts\activate   # for Windows

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run main.py
📄 License
This project is open-sourced under the MIT License.

