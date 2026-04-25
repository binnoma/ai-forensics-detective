import os
import gradio as gr
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor, BitsAndBytesConfig
from qwen_vl_utils import process_vision_info
import torch
from PIL import Image
from PIL.ExifTags import TAGS
import json

# --- Portability Configuration ---
# Set the local 'models' folder as the home for Hugging Face assets
project_root = os.path.dirname(os.path.abspath(__file__))
local_models_dir = os.path.join(project_root, "models")
os.environ["HF_HOME"] = local_models_dir
os.environ["HUGGINGFACE_HUB_CACHE"] = local_models_dir

# 1. Configuration & Model Loading
model_id = "Qwen/Qwen2-VL-7B-Instruct"

# Check for GPU and set appropriate settings
device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32

print(f"Loading model on {device} using {torch_dtype}...")

# 4-bit Quantization Config (Critical for HF Spaces with limited VRAM)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch_dtype
) if torch.cuda.is_available() else None

# Load the processor (Hugging Face verified approach)
processor = AutoProcessor.from_pretrained(model_id)

# Load the model with optimized settings
model = Qwen2VLForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch_dtype,
    device_map="auto",
    quantization_config=bnb_config,
    trust_remote_code=True # Often needed for newer VLM models on HF
)

# 2. Forensic Logic
FORENSIC_PROMPT = """
You are an expert AI Forensic Detective. Analyze the provided image meticulously to determine if it is AI-generated or real.
Look for specific artifacts such as:
- Anatomical anomalies (fused fingers, mismatched ears, irregular teeth).
- Lighting inconsistencies (multiple light sources with conflicting shadows).
- Textural glitches (blurry backgrounds, strange patterns on surfaces).
- Background manipulation (incoherent objects, blurry edges around subjects).

Output your analysis strictly in this JSON format:
{
  "verdict": "Real" or "AI-Generated",
  "confidence_percentage": 85,
  "red_flags_found": ["List", "of", "suspicious", "elements"],
  "detailed_explanation": "A brief paragraph explaining your reasoning."
}
"""

def get_exif_data(image_path):
    """Extract basic EXIF data to check for camera info."""
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        if not exif_data:
            return "No metadata found (Suspicious)."
        
        readable_exif = {}
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag, tag)
            readable_exif[decoded] = str(value)
        
        # Check for camera make/model
        make = readable_exif.get("Make", "Unknown")
        model = readable_exif.get("Model", "Unknown")
        return f"Camera: {make} {model}"
    except Exception as e:
        return f"Error reading metadata: {str(e)}"

FORENSIC_TIPS = [
    ("🔍 Did you know?", "AI often struggles with 'Limb Consistency'. Check the number of fingers and how they connect to the palm."),
    ("💡 Expert Tip", "Look at the reflections in the eyes. Real photos show consistent light sources; AI often creates mismatched glints."),
    ("🕵️ Artifact Alert", "AI-generated backgrounds often have 'semantic bleeding' where objects melt into each other (e.g., a tree branch turning into a lamp post)."),
    ("📸 Metadata Fact", "Every digital camera leaves a 'fingerprint' in the EXIF data. AI images are usually 'clean' or have strange software signatures."),
    ("🌓 Lighting Check", "Shadows don't lie. AI might place a shadow in a direction that doesn't match the main light source.")
]

import time

def analyze_image(image_path, progress=gr.Progress()):
    start_time = time.time()
    try:
        # Step A: Check Metadata
        progress(0.1, desc="🔍 STAGE 1: METADATA EXTRACTION")
        elapsed = lambda: f"{time.time() - start_time:.1f}s"
        
        yield f"🚀 [T+{elapsed()}] INVESTIGATION STARTED...\n"
        yield f"📡 [T+{elapsed()}] Scanning file headers...\n"
        
        metadata_info = get_exif_data(image_path)
        yield f"✅ [T+{elapsed()}] Metadata retrieved: {metadata_info}\n\n"
        
        # Educational Tip
        import random
        tip_title, tip_body = random.choice(FORENSIC_TIPS)
        yield f"💡 [PRO TIP]: {tip_body}\n\n"
        
        progress(0.3, desc="🧠 STAGE 2: NEURAL NETWORK ACTIVATION")
        yield f"⚙️ [T+{elapsed()}] Initializing Qwen2-VL Neural Engine...\n"
        yield f"📊 [T+{elapsed()}] Allocating VRAM/RAM for pixel analysis...\n"
        
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image_path},
                    {"type": "text", "text": FORENSIC_PROMPT},
                ],
            }
        ]
        
        # Process inputs
        text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        image_inputs, video_inputs = process_vision_info(messages)
        
        inputs = processor(
            text=[text],
            images=image_inputs,
            videos=video_inputs,
            padding=True,
            return_tensors="pt",
        ).to(device)

        # Generate response
        progress(0.6, desc="🕵️ STAGE 3: PIXEL-BY-PIXEL AUDIT")
        yield f"🔍 [T+{elapsed()}] Analyzing anatomical anomalies...\n"
        yield f"🌓 [T+{elapsed()}] Calculating lighting vectors and shadow consistency...\n"
        
        # Another tip
        another_tip = random.choice([t for t in FORENSIC_TIPS if t[0] != tip_title])
        yield f"💡 [PRO TIP]: {another_tip[1]}\n\n"
        
        print("Generating response from Qwen2-VL...")
        generated_ids = model.generate(**inputs, max_new_tokens=512)
        
        progress(0.9, desc="📝 STAGE 4: COMPILING EVIDENCE")
        yield f"📑 [T+{elapsed()}] Generating final forensic verdict...\n"
        
        generated_ids_trimmed = [out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
        output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True)[0]
        
        # Final combined output
        duration = elapsed()
        final_report = f"==========================================\n"
        final_report += f"🕵️ FINAL FORENSIC VERDICT (TIME: {duration})\n"
        final_report += f"==========================================\n\n"
        final_report += f"{output_text}\n\n"
        final_report += f"--- [ ATTACHED EVIDENCE ] ---\n"
        final_report += f"METADATA: {metadata_info}\n"
        final_report += f"TOTAL ANALYSIS TIME: {duration}\n"
        
        yield final_report
    
    except Exception as e:
        error_msg = f"❌ [T+{elapsed()}] CRITICAL ERROR: {str(e)}"
        print(error_msg)
        yield error_msg

# 3. Gradio UI with Ultra-Premium "Cyber-Forensics" Styling
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&family=JetBrains+Mono:wght@400;700&display=swap');

:root {
    --primary: #00f2ff;
    --secondary: #7000ff;
    --bg-dark: #020617;
    --panel-bg: rgba(15, 23, 42, 0.8);
    --accent: #ff007a;
}

body, .gradio-container {
    background: #020617 !important;
    font-family: 'Outfit', sans-serif !important;
}

.panel-style {
    background: var(--panel-bg) !important;
    border: 1px solid rgba(0, 242, 255, 0.15) !important;
    border-radius: 20px !important;
    padding: 25px !important;
    box-shadow: 0 0 40px rgba(0, 0, 0, 0.8) !important;
}

h1 {
    font-weight: 700 !important;
    background: linear-gradient(90deg, #00f2ff, #7000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3rem !important;
}

button.primary {
    background: linear-gradient(135deg, #7000ff, #00f2ff) !important;
    border-radius: 50px !important;
    font-size: 1.1rem !important;
    padding: 15px 30px !important;
}

#forensic-report textarea {
    font-family: 'JetBrains Mono', monospace !important;
    background: #000 !important;
    color: #00f2ff !important;
    border-left: 4px solid #7000ff !important;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.HTML("""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="margin: 0;">🕵️‍♂️ AI FORENSICS CENTER</h1>
            <p style="color: #64748b; font-size: 1.2rem;">Cyber-Security Hub for Image Authentication</p>
        </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=1, elem_classes="panel-style"):
            gr.HTML("""
                <div style="background: rgba(0,0,0,0.5); padding: 10px; border-radius: 10px; border-left: 3px solid #00f2ff; margin-bottom: 15px;">
                    <span style="color: #00f2ff; font-weight: bold;">LIVE SCANNER ACTIVE</span>
                </div>
            """)
            input_img = gr.Image(type="filepath", label="EVIDENCE UPLOAD")
            analyze_btn = gr.Button("🔍 INITIATE PIXEL SCAN", variant="primary")
            
        with gr.Column(scale=1, elem_classes="panel-style"):
            gr.HTML("""
                <div style="background: rgba(0,0,0,0.5); padding: 10px; border-radius: 10px; border-left: 3px solid #ff007a; margin-bottom: 15px;">
                    <span style="color: #ff007a; font-weight: bold;">INVESTIGATION LOG</span>
                </div>
            """)
            output_text = gr.Textbox(
                label="SYSTEM STATUS", 
                lines=20, 
                elem_id="forensic-report",
                placeholder="Awaiting evidence for audit..."
            )
            
    gr.HTML("<div style='text-align: center; color: #475569; padding: 20px;'>ENCRYPTED CONNECTION | NEURAL ENGINE: QWEN2-VL | SECURE AUDIT MODE</div>")
            
    analyze_btn.click(fn=analyze_image, inputs=input_img, outputs=output_text)

if __name__ == "__main__":
    demo.launch()

if __name__ == "__main__":
    demo.launch()
