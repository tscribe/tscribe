import scipy.stats as stats

# Example data (replace with your actual data)
control_group = [10, 12, 15, 14, 11]  # Group 1
test_group1 = [13, 16, 18, 17, 14]   # Group 2

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(control_group, test_group1)

if p_value < 0.05:
    print("Statistically significant difference exists.")
else:
    print("No significant difference detected.")

print(f"P-value: {p_value:.4f}")
