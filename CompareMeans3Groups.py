import numpy as np

# Define the data for each group
group1 = np.array([234, 244, 213, 225, 241])
group2 = np.array([322, 314, 325, 300, 317])
group3 = np.array([289, 144, 216, 200, 189])

# Calculate the means
mean_group1 = np.mean(group1)
mean_group2 = np.mean(group2)
mean_group3 = np.mean(group3)

# Compare the means
if mean_group1 > mean_group2 and mean_group1 > mean_group3:
    print("Group 1 has the highest mean:", mean_group1)
elif mean_group2 > mean_group1 and mean_group2 > mean_group3:
    print("Group 2 has the highest mean:", mean_group2)
else:
    print("Group 3 has the highest mean:", mean_group3)

# Print all means
print("Mean of Group 1:", mean_group1)
print("Mean of Group 2:", mean_group2)
print("Mean of Group 3:", mean_group3)
