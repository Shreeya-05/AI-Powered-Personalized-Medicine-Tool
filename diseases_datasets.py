import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Helper function to generate random genetic profiles
def generate_genetic_profile(n_samples, n_genes):
    return pd.DataFrame({
        f'gene_{i}': np.random.choice(['AA', 'AT', 'TT', 'CC', 'CG', 'GG'], n_samples)
        for i in range(1, n_genes + 1)
    })

# Generate datasets for each disease
n_samples = 100

# Diabetes dataset
diabetes_data = generate_genetic_profile(n_samples, 3)
diabetes_data['risk'] = np.random.choice(['Low', 'Medium', 'High'], n_samples)
diabetes_data['treatment'] = np.where(diabetes_data['risk'] == 'Low', 'Lifestyle changes',
                                      np.where(diabetes_data['risk'] == 'Medium', 'Metformin',
                                               'Insulin therapy'))

# Hypertension dataset
hypertension_data = generate_genetic_profile(n_samples, 3)
hypertension_data['risk'] = np.random.choice(['Low', 'Medium', 'High'], n_samples)
hypertension_data['treatment'] = np.where(hypertension_data['risk'] == 'Low', 'Lifestyle changes',
                                          np.where(hypertension_data['risk'] == 'Medium', 'ACE inhibitors',
                                                   'Combined therapy'))

# Hypercholesterolemia dataset
cholesterol_data = generate_genetic_profile(n_samples, 3)
cholesterol_data['risk'] = np.random.choice(['Low', 'Medium', 'High'], n_samples)
cholesterol_data['treatment'] = np.where(cholesterol_data['risk'] == 'Low', 'Dietary changes',
                                         np.where(cholesterol_data['risk'] == 'Medium', 'Statins',
                                                  'Intensive statin therapy'))

# Asthma dataset
asthma_data = generate_genetic_profile(n_samples, 3)
asthma_data['risk'] = np.random.choice(['Low', 'Medium', 'High'], n_samples)
asthma_data['treatment'] = np.where(asthma_data['risk'] == 'Low', 'Avoid triggers',
                                    np.where(asthma_data['risk'] == 'Medium', 'Inhaled corticosteroids',
                                             'Long-acting beta agonists'))

# Obesity dataset
obesity_data = generate_genetic_profile(n_samples, 3)
obesity_data['risk'] = np.random.choice(['Low', 'Medium', 'High'], n_samples)
obesity_data['treatment'] = np.where(obesity_data['risk'] == 'Low', 'Balanced diet and exercise',
                                     np.where(obesity_data['risk'] == 'Medium', 'Structured weight loss program',
                                              'Consider bariatric surgery'))

# Display the first few rows of each dataset
print("Diabetes Dataset:")
print(diabetes_data.head())
print("\nHypertension Dataset:")
print(hypertension_data.head())
print("\nHypercholesterolemia Dataset:")
print(cholesterol_data.head())
print("\nAsthma Dataset:")
print(asthma_data.head())
print("\nObesity Dataset:")
print(obesity_data.head())

# Save datasets to CSV files
diabetes_data.to_csv('diabetes_data.csv', index=False)
hypertension_data.to_csv('hypertension_data.csv', index=False)
cholesterol_data.to_csv('cholesterol_data.csv', index=False)
asthma_data.to_csv('asthma_data.csv', index=False)
obesity_data.to_csv('obesity_data.csv', index=False)

print("\nDatasets have been saved to CSV files.")