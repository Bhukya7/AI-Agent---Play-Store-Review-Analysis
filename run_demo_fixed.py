#!/usr/bin/env python3
"""
Fixed demo script for PulseGen AI Agent
"""

import sys
import os

# Add the src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def quick_demo():
    """Run a quick demo showing the project works"""
    print("🚀 PulseGen AI Agent - Quick Demo")
    print("=" * 40)
    
    # Check if we can import the main components
    try:
        # Try to import the main orchestrator
        from main_orchestrator import TrendAnalysisOrchestrator
        print("✅ Project imports working!")
        
        # Create a simple demo
        orchestrator = TrendAnalysisOrchestrator()
        app_url = "https://play.google.com/store/apps/details?id=in.swiggy.android"
        from datetime import datetime
        target_date = datetime(2024, 6, 30)
        
        print(f"📱 Analyzing: Swiggy")
        print(f"📅 Date: {target_date.strftime('%Y-%m-%d')}")
        print("⏳ This will use mock data for demonstration...")
        
        # Generate report
        report = orchestrator.generate_trend_report(app_url, target_date)
        
        if not report.empty:
            print("✅ Analysis completed!")
            print(f"📊 Found {len(report)} topics")
            
            # Show top 3 topics
            top_topics = report.sum(axis=1).nlargest(3)
            print("\n🏆 Top 3 Topics:")
            for topic, count in top_topics.items():
                print(f"   • {topic}: {int(count)} occurrences")
            
            # Save report
            os.makedirs('outputs', exist_ok=True)
            report.to_csv("outputs/demo_report.csv")
            print("💾 Saved to: outputs/demo_report.csv")
        else:
            print("📝 Using sample data for demonstration")
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("📊 Running in fallback demo mode...")
        run_fallback_demo()

def run_fallback_demo():
    """Fallback demo if imports fail"""
    import pandas as pd
    from datetime import datetime, timedelta
    
    # Create simple demo data
    dates = [datetime(2024, 6, 1) + timedelta(days=i) for i in range(7)]  # Just 7 days for demo
    date_headers = [d.strftime('%b %d') for d in dates]
    
    data = {
        'Delivery issue': [12, 8, 15, 10, 18, 14, 9],
        'Food stale': [5, 7, 3, 6, 8, 4, 5],
        'App crashing': [2, 4, 7, 3, 5, 6, 4],
    }
    
    report = pd.DataFrame(data, index=date_headers)
    report = report.T
    
    print("✅ Fallback demo completed!")
    print(f"📊 Sample data with {len(report)} topics")
    print("\n🏆 Sample Topics:")
    for topic in report.index:
        print(f"   • {topic}")
    
    # Save demo report
    os.makedirs('outputs', exist_ok=True)
    report.to_csv("outputs/demo_fallback_report.csv")
    print("💾 Saved to: outputs/demo_fallback_report.csv")

if __name__ == "__main__":
    quick_demo()