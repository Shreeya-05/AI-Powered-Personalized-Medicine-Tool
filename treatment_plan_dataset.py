import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Helper function to generate treatment plans
def generate_treatment_plans(n_samples, disease):
    risk_levels = np.random.choice(['Low', 'Medium', 'High'], n_samples)
    
    if disease == 'Diabetes':
        treatments = np.where(risk_levels == 'Low', 
                              'Lifestyle changes: Balanced diet, Regular exercise, Weight management',
                              np.where(risk_levels == 'Medium',
                                       'Metformin 500mg daily, Blood glucose monitoring, Lifestyle changes',
                                       'Insulin therapy, Metformin 1000mg daily, Strict diet, Regular check-ups'))
    elif disease == 'Hypertension':
        treatments = np.where(risk_levels == 'Low',
                              'Reduce sodium intake, Regular exercise, Stress management',
                              np.where(risk_levels == 'Medium',
                                       'ACE inhibitors: Lisinopril 10mg daily, Low-sodium diet, Exercise program',
                                       'Combined therapy: ACE inhibitor + Calcium channel blocker, Dietary counseling'))
    elif disease == 'Hypercholesterolemia':
        treatments = np.where(risk_levels == 'Low',
                              'Heart-healthy diet, Increase physical activity, Quit smoking if applicable',
                              np.where(risk_levels == 'Medium',
                                       'Statins: Atorvastatin 20mg daily, Mediterranean diet, Regular lipid panel tests',
                                       'Intensive statin therapy: Rosuvastatin 40mg daily, Strict diet, Frequent monitoring'))
    elif disease == 'Asthma':
        treatments = np.where(risk_levels == 'Low',
                              'Identify and avoid triggers, Create an asthma action plan, Short-acting beta agonists as needed',
                              np.where(risk_levels == 'Medium',
                                       'Inhaled corticosteroids: Fluticasone 250mcg twice daily, Regular peak flow monitoring',
                                       'Long-acting beta agonists + High-dose inhaled corticosteroids, Allergy testing'))
    elif disease == 'Obesity':
        treatments = np.where(risk_levels == 'Low',
                              'Balanced diet (1500-1800 calories/day), 150 minutes of moderate exercise per week',
                              np.where(risk_levels == 'Medium',
                                       'Structured weight loss program, Consider medications like Orlistat, Behavioral therapy',
                                       'Evaluate for bariatric surgery, Very low calorie diet under medical supervision'))
    
    return pd.DataFrame({
        'risk_level': risk_levels,
        'treatment_plan': treatments
    })

# Generate treatment plan datasets
n_samples = 100
diseases = ['Diabetes', 'Hypertension', 'Hypercholesterolemia', 'Asthma', 'Obesity']

treatment_plans = {}
for disease in diseases:
    treatment_plans[disease] = generate_treatment_plans(n_samples, disease)
    print(f"\n{disease} Treatment Plans:")
    print(treatment_plans[disease].head())
    
    # Save to CSV
    treatment_plans[disease].to_csv(f'{disease.lower()}_treatment_plans.csv', index=False)

print("\nTreatment plan datasets have been saved to CSV files.")

# Example of combining genetic profile with treatment plan for Diabetes
diabetes_genetic = pd.read_csv('diabetes_data.csv')
diabetes_treatment = treatment_plans['Diabetes']

combined_diabetes_data = pd.concat([diabetes_genetic, diabetes_treatment], axis=1)
print("\nCombined Diabetes Data (Genetic Profile + Treatment Plan):")
print(combined_diabetes_data.head())

# Save combined data
combined_diabetes_data.to_csv('combined_diabetes_data.csv', index=False)
print("\nCombined Diabetes data has been saved to 'combined_diabetes_data.csv'")