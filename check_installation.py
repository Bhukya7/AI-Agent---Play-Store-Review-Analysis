#!/usr/bin/env python3
"""
Check if all required packages are installed
"""

import sys
import subprocess

def check_package(package_name, import_name=None):
    """Check if a package is installed and can be imported"""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"✅ {package_name}")
        return True
    except ImportError as e:
        print(f"❌ {package_name}: {e}")
        return False

def main():
    print("🔍 Checking installed packages...")
    print("=" * 50)
    
    packages = [
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("scikit-learn", "sklearn"),
        ("sentence-transformers", "sentence_transformers"),
        ("spacy", "spacy"),
        ("nltk", "nltk"),
        ("keybert", "keybert"),
        ("yake", "yake"),
        ("requests", "requests"),
        ("beautifulsoup4", "bs4"),
        ("google-play-scraper", "google_play_scraper"),
        ("matplotlib", "matplotlib"),
    ]
    
    all_installed = True
    for package_name, import_name in packages:
        if not check_package(package_name, import_name):
            all_installed = False
    
    # Test spaCy model separately
    print("\n🔍 Testing spaCy model...")
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        print("✅ spaCy model 'en_core_web_sm'")
    except Exception as e:
        print(f"❌ spaCy model: {e}")
        all_installed = False
    
    print("\n" + "=" * 50)
    if all_installed:
        print("🎉 All packages installed successfully!")
    else:
        print("⚠️ Some packages are missing.")
        print("\nRun: pip install [missing-package-name]")

if __name__ == "__main__":
    main()