# 📜 Project Rules - AI Forensics Detective

To ensure the project remains portable, efficient, and aligned with industry standards, the following rules must be strictly followed:

## 1. Single Folder Portability
- **Rule**: All project files (code, assets, documentation) must reside within the `AI Forensics Detective` folder.
- **Reason**: This allows for easy transfer of the project between different environments (Local, Hugging Face Spaces, GitHub) without breaking path references.

## 2. Hugging Face Verification
- **Rule**: Every model implementation, dependency version, and inference logic must be verified against the official **Hugging Face Hub** and **Transformers** documentation.
- **Reason**: AI models and libraries (especially VLM models like Qwen2-VL) evolve rapidly. Using verified methods prevents compatibility errors (like `KeyError: 'qwen2_vl'`).

## 3. Dependency Integrity
- **Rule**: `requirements.txt` must be kept up-to-date with versions known to be stable and compatible with the target hardware (e.g., T4 Medium or ZeroGPU).

## 4. Documentation First
- **Rule**: Any change in the logic or model must be reflected in the `IMPLEMENTATION_PLAN.md` and `README.md` immediately.

---
*These rules are designed to maintain the high quality and reliability of the AI Forensics Detective tool.*
