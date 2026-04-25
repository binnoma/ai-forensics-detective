# 🕵️‍♂️ AI Forensics Detective - User Guide & Documentation

## 1. Introduction
AI Forensics Detective is a state-of-the-art digital investigation tool designed to authenticate images and detect AI-generated content. By leveraging the **Qwen2-VL** vision-language model, it performs deep pixel analysis and metadata extraction to provide a comprehensive forensic verdict.

---

## 2. Getting Started

### 🖥️ Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ai-forensics-detective.git
   ```
2. **Run the Automated Setup**:
   - Double-click `START_PROJECT.bat` (Windows).
   - The script will handle Python checks, dependency installation, and model optimization.

---

## 3. How to Use the Tool

### Step 1: Evidence Upload
- Click on the **"EVIDENCE UPLOAD"** panel.
- Select a suspicious image (JPG, PNG, or WEBP).
- **Pro Tip**: Use the highest resolution available for better artifact detection.

### Step 2: Initiate Scan
- Click the **"INITIATE PIXEL SCAN"** button.
- The **Investigation Log** will start updating in real-time.

### Step 3: Monitoring the Log
- **Stage 1 (Metadata)**: The system checks for EXIF data (Camera make, model, software).
- **Stage 2 (Activation)**: The Neural Engine loads the AI model into memory.
- **Stage 3 (Audit)**: The AI performs a pixel-by-pixel search for "Anatomical Anomalies" (e.g., extra fingers) and "Lighting Inconsistencies".
- **Stage 4 (Verdict)**: A final report is compiled.

---

## 4. Understanding the Results

### 📊 Verdict Indicators
- **AI-Generated**: High probability that the image was created using models like Midjourney or DALL-E. The report will list "Red Flags" like fused limbs or inconsistent shadows.
- **Real/Authentic**: The image shows consistent physical patterns and valid metadata common to real cameras.
- **Confidence Percentage**: Shows how certain the AI is about the result (e.g., 95% Confidence).

### 🔍 Forensic Artifacts to Watch For:
1. **Fingers & Limbs**: AI often melts fingers together or adds extra ones.
2. **Reflections**: Mismatched glints in eyes or water surfaces.
3. **Semantic Bleeding**: Background objects that blur or transform into unrelated items.

---

## 5. Technical Rules & Portability
- **Self-Contained**: The project stores models in the `/models/` subfolder.
- **Privacy**: All analysis is performed locally; no images are sent to external servers beyond the initial model download.

---
> [!NOTE]
> This project is designed for investigation and education. Always use multiple sources of evidence for legal or high-stakes forensic audits.
