#!/usr/bin/env python3
"""
Main entry point for PulseGen AI Agent
"""

import pandas as pd
from datetime import datetime
from src.main_orchestrator import TrendAnalysisOrchestrator
from src.utils.config import Config

def main():
    """
    Main function to run the trend analysis
    """
    try:
        print("🚀 PulseGen AI Agent - Play Store Review Analysis")
        print("=" * 60)
        
        # Initialize
        config = Config()
        orchestrator = TrendAnalysisOrchestrator(config)
        
        # Set parameters
        app_store_link = "https://play.google.com/store/apps/details?id=in.swiggy.android"
        target_date = datetime(2024, 6, 30)
        
        print(f"📱 App: Swiggy")
        print(f"📅 Target Date: {target_date.strftime('%Y-%m-%d')}")
        print("⏳ Starting analysis...")
        
        # Generate report
        report_df = orchestrator.generate_trend_report(app_store_link, target_date)
        
        if report_df.empty:
            print("❌ No data available to generate report.")
            return
        
        # Display summary
        print("\n📊 REPORT SUMMARY")
        print("=" * 50)
        print(f"Total Topics: {len(report_df)}")
        print(f"Total Days: {len(report_df.columns)}")
        
        # Show top topics
        top_topics = report_df.sum(axis=1).nlargest(5)
        print("\n🏆 TOP 5 TOPICS:")
        for topic, count in top_topics.items():
            print(f"  • {topic}: {int(count)} occurrences")
        
        # Save report
        import os
        os.makedirs('outputs', exist_ok=True)
        output_file = f"outputs/trend_report_{target_date.strftime('%Y%m%d')}.csv"
        report_df.to_csv(output_file)
        print(f"\n💾 Report saved to: {output_file}")
        
        print("\n🎉 Analysis completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()