"""
Station 2: Environment & Package Verification Script
The AI-Proof Software Engineer - Vivek Chauhan
"""

import sys

def verify_environment():
    print("=" * 50)
    print("🚀 STARTING AI-PROOF ENVIRONMENT VERIFICATION...")
    print("=" * 50)

    # 1. Check Python Version (Targeting 3.10+ as per book guidelines)
    python_version = sys.version_info
    print(f"🐍 Python Version: {sys.version.split()[0]}")
    if python_version.major == 3 and python_version.minor >= 10:
        print("✅ Python version meets the required baseline.")
    else:
        print("⚠️ Warning: Python 3.10+ is recommended for modern AI libraries.")

    # 2. Verify Core Library Imports
    libraries = ["numpy", "pandas", "torch", "requests", "openai", "dotenv"]
    missing_libs = []

    print("\n📦 Checking Core Dependencies...")
    for lib in libraries:
        try:
            if lib == "dotenv":
                import dotenv
                print(f"  ▪️ dotenv: Active (v{dotenv.__version__})")
            elif lib == "torch":
                import torch
                print(f"  ▪️ torch: Active (v{torch.__version__}) - GPU Available: {torch.cuda.is_available()}")
            else:
                imported_lib = __import__(lib)
                # Some libraries don't expose a clean __version__ string directly
                version = getattr(imported_lib, "__version__", "Detected")
                print(f"  ▪️ {lib}: Active ({version})")
        except ImportError:
            print(f"  ❌ {lib}: NOT FOUND")
            missing_libs.append(lib)

    # 3. Final Diagnostic Summary
    print("\n" + "=" * 50)
    if not missing_libs:
        print("🎉 SUCCESS: Your developer toolkit environment is 100% ready!")
        print("Proceed confidently to Station 3 (ML/DL Foundations).")
    else:
        print("❌ ERROR: Missing packages detected.")
        print(f"Please run: pip install -r requirements.txt")
        print("If you are on a restricted network, consider using a mobile hotspot.")
    print("=" * 50)

if __name__ == "__main__":
    verify_environment()
