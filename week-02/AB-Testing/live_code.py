# ==============================================================================
# A/B TESTING LIVE DEMO: E-Commerce Checkout Conversion Analysis
# ==============================================================================
# This notebook demonstrates an end-to-end A/B test pipeline:
# 1. Loading and cleaning open-source experimental data.
# 2. Calculating baseline metrics and conversion rates.
# 3. Running a Two-Sample Hypothesis Test (Z-Test).
# 4. Computing 95% Confidence Intervals.
# 5. Visualizing results for presentation slides.
# ==============================================================================

# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

# Set styling for clean presentation graphics
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12})

print("✅ Libraries imported successfully.")

# ------------------------------------------------------------------------------
# Step 2: Load Open-Source Dataset
# ------------------------------------------------------------------------------
# Fetching public A/B test dataset hosted on GitHub (294k+ user sessions)
DATA_URL = "https://raw.githubusercontent.com/beery4010/Analyze-AB-Test-Results/master/ab_data.csv"

print("\n📥 Fetching dataset from URL...")
df = pd.read_csv(DATA_URL)

print(f"Dataset Loaded: {len(df):,} total records.")
print("\nFirst 5 Rows:")
print(df.head())
# ------------------------------------------------------------------------------
# Step 3: Data Cleaning & Preprocessing
# ------------------------------------------------------------------------------
# Ensure unique users to maintain independent, identically distributed (i.i.d.) observations.
user_counts = df['user_id'].value_counts()
multiple_users = user_counts[user_counts > 1].index

df_clean = df[~df['user_id'].isin(multiple_users)].copy()
print(f"\n🧹 Data Cleaned: Removed {len(df) - len(df_clean):,} duplicate session records.")
print(f"Final Unique Users: {len(df_clean):,}")

# ------------------------------------------------------------------------------
# Step 4: Summary Aggregations
# ------------------------------------------------------------------------------
summary = df_clean.groupby('group').agg(
    total_users=('converted', 'count'),
    conversions=('converted', 'sum'),
    conversion_rate=('converted', 'mean')
).reset_index()

# Add formatted percentage string for clear reading
summary['conversion_pct'] = summary['conversion_rate'].map(lambda x: f"{x:.2%}")

print("\n📊 Summary Statistics by Group:")
print(summary.to_string(index=False))

# ------------------------------------------------------------------------------
# Step 5: Statistical Hypothesis Testing (Two-Sample Z-Test)
# ------------------------------------------------------------------------------
# Extract counts for control (A) and treatment (B)
ctrl_conv = summary.loc[summary['group'] == 'control', 'conversions'].values[0]
ctrl_n = summary.loc[summary['group'] == 'control', 'total_users'].values[0]

treat_conv = summary.loc[summary['group'] == 'treatment', 'conversions'].values[0]
treat_n = summary.loc[summary['group'] == 'treatment', 'total_users'].values[0]

counts = [treat_conv, ctrl_conv]
nobs = [treat_n, ctrl_n]

# Perform Z-test for proportions
z_stat, p_val = proportions_ztest(counts, nobs)

# Compute 95% Confidence Intervals
(ci_lower_treat, ci_lower_ctrl), (ci_upper_treat, ci_upper_ctrl) = proportion_confint(
    counts, nobs, alpha=0.05
)

# Relative Lift Calculation
rate_ctrl = ctrl_conv / ctrl_n
rate_treat = treat_conv / treat_n
relative_lift = (rate_treat - rate_ctrl) / rate_ctrl

print("\n" + "="*50)
print("              STATISTICAL VERDICT              ")
print("="*50)
print(f"Control Conversion Rate (A):   {rate_ctrl:.4%}")
print(f"Treatment Conversion Rate (B): {rate_treat:.4%}")
print(f"Relative Difference (Lift):   {relative_lift:.2%}")
print(f"Z-Score Statistic:            {z_stat:.4f}")
print(f"P-Value:                      {p_val:.5f}")
print("-" * 50)

alpha = 0.05
if p_val < alpha:
    print("RESULT: Statistically Significant Difference Detected (p < 0.05).")
    print("Action: Reject H0. Roll out the Variant (B).")
else:
    print("RESULT: No Statistically Significant Difference Detected (p >= 0.05).")
    print("Action: Fail to reject H0. Do not roll out Variant (B).")
print("="*50 + "\n")

# ------------------------------------------------------------------------------
# Step 6: Visualizations for Live Demo
# ------------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Bar Chart Comparison
sns.barplot(
    data=summary,
    x='group',
    y='conversion_rate',
    palette=['#34495e', '#e74c3c'],
    ax=axes[0]
)
axes[0].set_title('Conversion Rate by Group', fontweight='bold', pad=12)
axes[0].set_xlabel('Group', fontweight='bold')
axes[0].set_ylabel('Conversion Rate', fontweight='bold')
axes[0].set_ylim(0, 0.15)

# Annotate exact bar values
for p in axes[0].patches:
    axes[0].annotate(
        f"{p.get_height():.2%}",
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='bottom',
        fontsize=11, fontweight='bold',
        xytext=(0, 5), textcoords='offset points'
    )

# Plot 2: 95% Confidence Intervals
groups = ['Control (A)', 'Variant (B)']
means = [rate_ctrl, rate_treat]
yerr = [
    [rate_ctrl - ci_lower_ctrl, rate_treat - ci_lower_treat],
    [ci_upper_ctrl - rate_ctrl, ci_upper_treat - rate_treat]
]

axes[1].errorbar(
    groups, means, yerr=yerr,
    fmt='o', color='#2c3e50', ecolor='#e74c3c',
    elinewidth=2.5, capsize=8, markersize=8
)
axes[1].set_title('95% Confidence Intervals', fontweight='bold', pad=12)
axes[1].set_ylabel('Conversion Proportion', fontweight='bold')
axes[1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()