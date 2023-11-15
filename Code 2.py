import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read data from the CSV file
data = pd.read_csv('data.csv')

# Define significance threshold (you can adjust this based on your data)
threshold = 1.3

# Perform analysis (you can customize this based on your specific requirements)
significant_upregulated = data['Fold Change'] > 0.5
significant_downregulated = data['Fold Change'] < -0.5
significant = np.logical_or(significant_upregulated, significant_downregulated)

# Create the volcano plot
plt.scatter(data['Fold Change'][significant], data['P-values'][significant], color='red', label='Significant')
plt.scatter(data['Fold Change'][~significant], data['P-values'][~significant], color='blue', label='Not Significant')

# Highlight points above the significance threshold
plt.axhline(y=threshold, color='black', linestyle='--', label='Significance Threshold')

# Add vertical lines to separate blue and red dots
plt.axvline(x=0.5, color='black', linestyle='--', linewidth=0.8, label='Threshold')
plt.axvline(x=-0.5, color='black', linestyle='--', linewidth=0.8)

# Customize the plot
plt.title('Volcano Plot')
plt.xlabel('Log2(Fold Change)')
plt.ylabel('-log10(p-value)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Show the plot
plt.show()
