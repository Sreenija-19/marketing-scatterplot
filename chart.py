# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --------------------------
# 1. Generate synthetic data
# --------------------------
np.random.seed(42)  # for reproducibility

n_samples = 100

# Simulate marketing campaign data
# 'ad_spend' in $1000s, 'conversion_rate' in %, 'channel' categorical
ad_spend = np.random.uniform(1, 20, n_samples)  # 1k to 20k
conversion_rate = 2 + 0.8 * ad_spend + np.random.normal(0, 3, n_samples)  # positive correlation
channels = np.random.choice(['Social Media', 'Email', 'Search', 'Display'], n_samples)

# Create DataFrame
data = pd.DataFrame({
    'Ad Spend ($k)': ad_spend,
    'Conversion Rate (%)': conversion_rate,
    'Channel': channels
})

# --------------------------
# 2. Set Seaborn styling
# --------------------------
sns.set_style("whitegrid")      # professional background
sns.set_context("talk")         # presentation-ready text sizes
palette = sns.color_palette("Set2")  # color palette for channels

# --------------------------
# 3. Create scatterplot
# --------------------------
plt.figure(figsize=(8, 8))  # 512x512 px with dpi=64

scatter = sns.scatterplot(
    data=data,
    x='Ad Spend ($k)',
    y='Conversion Rate (%)',
    hue='Channel',
    palette=palette,
    s=100,         # size of points
    edgecolor='black'
)

# Add title and labels
plt.title('Marketing Campaign Effectiveness', fontsize=16, weight='bold')
plt.xlabel('Ad Spend ($k)', fontsize=14)
plt.ylabel('Conversion Rate (%)', fontsize=14)

# Move legend outside plot
plt.legend(title='Channel', bbox_to_anchor=(1.05, 1), loc='upper left')

# --------------------------
# 4. Save chart
# --------------------------
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
