import sys
import os
import pandas as pd
from datetime import datetime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def create_demo_report():
    """Create a comprehensive demo trend report"""
    print("🚀 PulseGen AI Agent - Play Store Review Analysis")
    print("📊 Generating Trend Analysis Report")
    print("=" * 60)
    
    start_date = datetime(2024, 6, 1)
    dates = [start_date + timedelta(days=i) for i in range(30)]
    date_headers = [d.strftime('%b %d') for d in dates]
    
    data = {
        'Delivery issue': [12, 8, 15, 10, 18, 14, 9, 20, 16, 11, 13, 19, 17, 12, 15, 21, 14, 16, 18, 13, 15, 17, 19, 16, 14, 12, 18, 20, 15, 23],
        'Food stale': [5, 7, 3, 6, 8, 4, 5, 9, 6, 4, 7, 8, 5, 6, 4, 10, 5, 7, 6, 5, 8, 7, 9, 6, 5, 7, 8, 9, 7, 11],
        'Delivery partner rude': [8, 12, 6, 9, 11, 7, 10, 13, 8, 9, 11, 10, 7, 12, 9, 14, 8, 10, 11, 9, 12, 10, 13, 9, 11, 10, 12, 11, 10, 9],
        'App crashing': [2, 4, 7, 3, 5, 6, 4, 8, 5, 3, 6, 7, 4, 5, 6, 9, 4, 7, 5, 6, 8, 6, 7, 5, 6, 7, 8, 6, 7, 5],
        'Payment problem': [1, 3, 2, 4, 3, 5, 2, 6, 4, 3, 5, 4, 2, 6, 3, 7, 4, 5, 3, 4, 6, 5, 4, 3, 5, 4, 6, 5, 4, 8],
        'Refund issue': [3, 2, 4, 3, 5, 4, 3, 6, 4, 5, 3, 4, 5, 3, 6, 4, 5, 3, 4, 5, 3, 6, 4, 5, 3, 4, 5, 6, 4, 7],
        'Maps not working properly': [2, 4, 3, 5, 4, 6, 3, 5, 4, 3, 5, 4, 6, 3, 5, 4, 3, 6, 4, 5, 3, 4, 5, 6, 4, 3, 5, 4, 6, 6],
        'Food quality poor': [4, 3, 5, 4, 6, 3, 5, 4, 3, 6, 4, 5, 3, 4, 5, 6, 3, 4, 5, 3, 6, 4, 5, 3, 4, 5, 6, 4, 3, 5],
        'Order cancellation issue': [3, 4, 2, 5, 3, 4, 2, 5, 3, 4, 2, 5, 3, 4, 2, 5, 3, 4, 5, 2, 4, 3, 5, 4, 2, 3, 5, 4, 2, 6],
        'Missing items': [2, 3, 4, 2, 5, 3, 4, 2, 5, 3, 4, 2, 5, 3, 4, 2, 5, 3, 4, 5, 2, 4, 3, 5, 4, 2, 5, 3, 4, 5],
        'Packaging damaged': [1, 2, 1, 3, 2, 1, 3, 2, 1, 4, 2, 1, 3, 2, 1, 4, 2, 1, 3, 2, 4, 1, 2, 3, 1, 4, 2, 1, 3, 4],
        'Customer service poor': [3, 2, 4, 3, 2, 5, 3, 4, 2, 3, 5, 4, 2, 3, 4, 5, 2, 3, 4, 2, 5, 3, 4, 2, 3, 5, 4, 2, 3, 5],
    }
    
    df = pd.DataFrame(data, index=date_headers)
    df = df.T  
    
    return df

def display_report(report_df):
    """Display a comprehensive report summary"""
    print("\n📊 TREND ANALYSIS REPORT")
    print("=" * 80)
    print(f"📅 Analysis Period: June 1, 2024 - June 30, 2024")
    print(f"📈 Total Topics Tracked: {len(report_df)}")
    print(f"📅 Days Analyzed: {len(report_df.columns)}")
    
    total_issues = report_df.sum().sum()
    print(f"🔢 Total Issues Found: {int(total_issues)}")
    
    print("\n🏆 TOP 15 TOPICS BY FREQUENCY:")
    print("-" * 50)
    
    topic_totals = report_df.sum(axis=1).sort_values(ascending=False)
    
    for i, (topic, count) in enumerate(topic_totals.items(), 1):
        percentage = (count / total_issues) * 100
        print(f"{i:2d}. {topic:<30} {int(count):>4} occurrences ({percentage:.1f}%)")
    
    print(f"\n📈 TREND ANALYSIS - TOP 3 TOPICS (Last 7 Days):")
    print("-" * 50)
    
    top_3_topics = topic_totals.head(3).index
    for topic in top_3_topics:
        last_7_days = report_df.loc[topic].tail(7)
        avg_trend = last_7_days.mean()
        trend_icon = "📈" if last_7_days.iloc[-1] > last_7_days.iloc[0] else "📉"
        
        print(f"\n{topic}:")
        print(f"  Last 7 days: {[int(x) for x in last_7_days.values]}")
        print(f"  Weekly average: {avg_trend:.1f} {trend_icon}")
    
    return topic_totals

def create_visualization(report_df, topic_totals):
    """Create visualization of the trends"""
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        print("\n📈 Generating visualizations...")
        
        plt.style.use('default')
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        top_5_topics = topic_totals.head(5).index
        trend_data = report_df.loc[top_5_topics].T
        
        trend_data.index = pd.to_datetime(trend_data.index, format='%b %d')
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
        for i, topic in enumerate(top_5_topics):
            ax1.plot(trend_data.index, trend_data[topic], 
                    marker='o', linewidth=2.5, label=topic, color=colors[i])
        
        ax1.set_title('Top 5 Topics - Daily Trend (June 2024)', 
                     fontsize=16, fontweight='bold', pad=20)
        ax1.set_xlabel('Date', fontsize=12)
        ax1.set_ylabel('Number of Occurrences', fontsize=12)
        ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis='x', rotation=45)
        
        top_10_topics = topic_totals.head(10)
        colors_bar = plt.cm.Set3(range(len(top_10_topics)))
        
        bars = ax2.barh(range(len(top_10_topics)), top_10_topics.values, color=colors_bar)
        ax2.set_yticks(range(len(top_10_topics)))
        ax2.set_yticklabels(top_10_topics.index, fontsize=10)
        ax2.set_xlabel('Total Occurrences (30 Days)', fontsize=12)
        ax2.set_title('Top 10 Topics - Total Frequency', 
                     fontsize=16, fontweight='bold', pad=20)
        ax2.grid(True, alpha=0.3, axis='x')
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax2.text(width + 5, bar.get_y() + bar.get_height()/2, 
                    f'{int(width)}', ha='left', va='center', 
                    fontweight='bold', fontsize=9)
        
        plt.tight_layout()
        
        os.makedirs('outputs', exist_ok=True)
        viz_file = "outputs/trend_analysis_visualization.png"
        plt.savefig(viz_file, dpi=300, bbox_inches='tight')
        print(f"💾 Visualization saved to: {viz_file}")
        
        plt.show()
        
    except Exception as e:
        print(f"📊 Visualization skipped: {e}")

def main():
    """Main function to run the analysis"""
    try:
        report_df = create_demo_report()
        
        topic_totals = display_report(report_df)
        
        os.makedirs('outputs', exist_ok=True)
        csv_file = "outputs/trend_analysis_report_june_2024.csv"
        report_df.to_csv(csv_file)
        print(f"\n💾 CSV report saved to: {csv_file}")
        
        create_visualization(report_df, topic_totals)
        
        print("\n🔍 KEY INSIGHTS:")
        print("-" * 40)
        
        volatility = report_df.std(axis=1)
        most_volatile = volatility.idxmax()
        print(f"• Most volatile topic: {most_volatile} (std: {volatility[most_volatile]:.1f})")
        
        trends = report_df.iloc[:, -7:].mean(axis=1) - report_df.iloc[:, :7].mean(axis=1)
        biggest_increase = trends.idxmax()
        print(f"• Biggest increase: {biggest_increase} (+{trends[biggest_increase]:.1f})")
        
        print(f"\n🎉 Analysis completed successfully!")
        print(f"📁 Check the 'outputs' folder for generated files")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()