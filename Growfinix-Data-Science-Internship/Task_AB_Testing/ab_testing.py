import pandas as pd
from scipy.stats import ttest_ind

# Sample data
group_A = [45, 50, 47, 52, 49, 51, 48, 46, 50, 49]
group_B = [55, 60, 58, 57, 59, 61, 56, 58, 60, 57]

# Perform t-test
t_stat, p_value = ttest_ind(group_A, group_B)

# Create DataFrame
result = pd.DataFrame({
    "Group A": group_A,
    "Group B": group_B
})

# Save CSV
result.to_csv("Task_AB_Testing/results.csv", index=False)

# Print output
print(result)
print("\nT-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("\nResult: Statistically Significant")
else:
    print("\nResult: Not Statistically Significant")

print("\nTask 5 Completed Successfully!")