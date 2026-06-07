import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Platform': ['Instagram', 'Facebook', 'Twitter', 'LinkedIn', 'TikTok', 'YouTube'],
    'Daily_Users': [1200, 980, 750, 430, 1500, 2100],
    'Avg_Time_Min': [45, 32, 28, 22, 58, 65],
    'Engagement_Rate': [8.5, 6.2, 5.1, 4.8, 9.2, 7.9]
}
df = pd.DataFrame(data)

# Style set
sns.set_style("whitegrid")
plt.figure(figsize=(15, 10))

# Graph 1: Daily Users by Platform - Bar chart
plt.subplot(2, 2, 1)
sns.barplot(x='Platform', y='Daily_Users', data=df, palette='viridis')
plt.title('Daily Active Users by Platform', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.ylabel('Daily Users')
plt.xlabel('')

# Graph 2: Average Time Spent - Bar chart
plt.subplot(2, 2, 2)
sns.barplot(x='Platform', y='Avg_Time_Min', data=df, palette='magma')
plt.title('Average Time Spent per User', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.ylabel('Minutes per Day')
plt.xlabel('')

# Graph 3: Engagement Rate - Bar chart
plt.subplot(2, 2, 3)
sns.barplot(x='Platform', y='Engagement_Rate', data=df, palette='coolwarm')
plt.title('Engagement Rate by Platform', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.ylabel('Engagement Rate %')
plt.xlabel('Platform')

# Graph 4: Correlation - Scatter plot
plt.subplot(2, 2, 4)
sns.scatterplot(x='Avg_Time_Min', y='Engagement_Rate', data=df, hue='Platform', s=200, palette='Set2')
plt.title('Time Spent vs Engagement Rate', fontsize=14, fontweight='bold')
plt.xlabel('Avg Time Spent (Min)')
plt.ylabel('Engagement Rate %')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.suptitle('Social Media Analytics Dashboard', fontsize=18, fontweight='bold', y=1.02)
plt.tight_layout()

# Dashboard save
plt.savefig('dashboard.png', dpi=300, bbox_inches='tight')
print("Dashboard saved successfully")

plt.show()