# 🕵️‍♂️ AI Forensics Detective - Implementation Plan

## 1. Project Overview
**AI Forensics Detective** is an advanced interactive web application designed to analyze images and determine if they are authentic or AI-generated (e.g., Midjourney, DALL-E, Stable Diffusion). Unlike simple binary classifiers, this tool provides a detailed "Forensic Report" explaining the reasoning behind its verdict, focusing on anatomical anomalies, lighting inconsistencies, and textural glitches.

## 2. Technical Stack (Hugging Face Native)
To ensure seamless integration with the Hugging Face (HF) ecosystem, the project will use:
- **UI Framework**: [Gradio](https://gradio.app/) (Standard for HF Spaces).
- **Core Libraries**: `transformers`, `torch`, `qwen-vl-utils`.
- **Model (The Brain)**: `Qwen/Qwen2-VL-7B-Instruct`. Chosen for its superior reasoning and detailed image analysis capabilities.
- **Environment**: Hugging Face Spaces (ZeroGPU or T4 Medium recommended).

## 3. Development Phases

### Phase 1: MVP (Minimum Viable Product)
- **Environment Setup**: Initialize a Gradio-based Space on Hugging Face.
- **Dependency Management**: Create `requirements.txt` with optimized versions.
- **Core Logic**:
    - Implement the `FORENSIC_PROMPT` to guide the model.
    - Setup the Qwen2-VL inference pipeline.
    - Apply 4-bit quantization to fit within standard GPU memory constraints.

### Phase 2: Enhanced Analysis (Metadata & EXIF)
- **Metadata Extraction**: Use `Pillow` to extract EXIF data (Camera model, focal length, timestamps).
- **Heuristic Logic**: If EXIF data is missing or suspicious (e.g., "Software: Adobe Firefly"), flag it as a potential indicator of AI generation.

### Phase 3: Performance & Accuracy Optimization
- **Ensemble Method**: Integrate a lightweight classifier (e.g., `umm-maybe/AI-image-detector`) as a first-pass filter.
- **Fine-Tuning**: Potential training of a specialized `Qwen2-VL-2B` model using a curated dataset of AI artifacts.

## 4. Project Structure
```text
AI-Forensics-Detective/
├── app.py              # Main Gradio application logic
├── requirements.txt    # Python dependencies
├── IMPLEMENTATION_PLAN.md # This document
└── README.md           # Project documentation and usage guide
```

## 5. Technical Challenges & Solutions
| Challenge | Solution |
| :--- | :--- |
| **VRAM Consumption** | Use `bitsandbytes` for 4-bit quantization (`load_in_4bit=True`). |
| **Latency** | Implement `gr.LoadingSpinner` and meaningful progress messages. |
| **False Positives** | Use the "Reasoning-First" approach where the model must list red flags before giving a verdict. |

## 6. Deployment Guide
1. **Create Space**: Choose "Gradio" and "Public/Private".
2. **Upload Files**: `app.py`, `requirements.txt`.
3. **Configure Hardware**: Set to `T4 Medium` or `ZeroGPU`.
4. **Wait for Build**: HF will automatically install requirements and launch the app.
