# 🕵️‍♂️ AI Forensics Detective

[**العربية - اضغط هنا لقراءة الوثائق بالعربي**](README_AR.md) | [**Technical Details (Arabic)**](PROJECT_DETAILS_AR.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-orange)](https://huggingface.co/spaces)

**AI Forensics Detective** is a professional-grade digital investigation suite designed to identify AI-generated imagery and deepfakes. It uses the state-of-the-art **Qwen2-VL** vision-language model to perform deep-pixel analysis, looking for anatomical anomalies, lighting inconsistencies, and semantic artifacts.

---

## ✨ Key Features
- **Ultra-Premium UI**: Futuristic "Cyber-Forensics" interface with glassmorphism and neon accents.
- **Mission Dashboard**: Real-time investigation logs with timestamped stage tracking.
- **Deep Artifact Analysis**: Detects fused limbs, mismatched eye reflections, and inconsistent shadows.
- **Metadata Extraction**: Automatically parses EXIF data to verify camera authenticity.
- **100% Portable**: Stores models locally in the `/models/` folder for offline-ready deployment.

## 📸 Preview
![UI Mockup](ui_mockup.png)

## 🚀 Quick Start (Windows)
1. **Clone the project**:
   ```bash
   git clone https://github.com/your-username/AI-Forensics-Detective.git
   ```
2. **Run the Automated Launcher**:
   - Double-click **`START_PROJECT.bat`**.
   - The script will automatically set up your environment, move existing HF models, and launch the dashboard.

## 🛠 Tech Stack
- **Model Engine**: [Qwen/Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)
- **Framework**: Hugging Face Transformers & Gradio
- **Optimizations**: 4-bit BitsAndBytes Quantization (VRAM Efficient)
- **Styling**: Custom CSS / Google Fonts (Outfit & JetBrains Mono)

## 📄 Documentation
For a detailed guide on how to interpret forensic results and advanced configuration, see the [USER_GUIDE.md](USER_GUIDE.md).

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
