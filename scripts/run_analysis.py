#!/usr/bin/env python3
"""
Script to run analysis with different parameters
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from datetime import datetime
from src.main_orchestrator import TrendAnalysisOrchestrator

def run_analysis(app_url: str, target_date_str: str):
    """
    Run analysis with specific parameters
    """
    orchestrator = TrendAnalysisOrchestrator()
    target_date = datetime.strptime(target_date_str, '%Y-%m-%d')
    
    report_df = orchestrator.generate_trend_report(app_url, target_date)
    
    # Save with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = f"outputs/trend_report_{timestamp}.csv"
    orchestrator.report_generator.save_report(report_df, output_file)
    
    print(f"Report saved to: {output_file}")
    return report_df

if __name__ == "__main__":
    # Example usage
    app_url = "https://play.google.com/store/apps/details?id=in.swiggy.android"
    target_date = "2024-06-30"
    
    report = run_analysis(app_url, target_date)
    print(report.head())