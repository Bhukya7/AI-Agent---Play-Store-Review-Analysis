# AI Agent - Play Store Review Analysis

Trend Analysis of App Store Reviews

## Overview

This AI agent analyzes Google Play Store reviews to create trend analysis reports for issues, requests, and feedback. The system uses agentic AI approaches for topic analysis and trend detection.

## Features

- Daily batch processing of reviews
- Semantic topic analysis using sentence transformers
- Trend analysis over 30-day periods
- Automatic topic discovery and consolidation
- CSV report generation

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Install spaCy model: `python -m spacy download en_core_web_sm`
6. Copy `.env.example` to `.env` and configure your settings

## Usage

```python
from src.main_orchestrator import TrendAnalysisOrchestrator
from datetime import datetime

orchestrator = TrendAnalysisOrchestrator()
report = orchestrator.generate_trend_report(
    "https://play.google.com/store/apps/details?id=in.swiggy.android",
    datetime(2024, 6, 30)
)