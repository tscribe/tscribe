import scipy.stats as stats

# Example data (replace with your actual data)
group_A = [89, 89, 88, 78, 79]  # Treatment group A
group_B = [93, 92, 94, 89, 88]  # Treatment group B
group_C = [89, 88, 89, 93, 90]  # Treatment group C

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(group_A, group_B, group_C)

# Interpret the results
alpha = 0.05  # Set your significance level (commonly 0.05)
if p_value < alpha:
    print("Statistically significant difference exists among groups.")
else:
    print("No significant difference detected among groups.")

print(f"P-value: {p_value:.4f}")
