print("Start of ml_model")
from sklearn.ensemble import RandomForestClassifier
print("RandomForestClassifier imported")


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

class GeneticTreatmentRecommender:
    def __init__(self, disease):
        self.disease = disease
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.le_genes = LabelEncoder()
        self.le_risk = LabelEncoder()
        
        # Load and preprocess data
        self.load_data()
        self.train_model()
    
    def load_data(self):
        # Load the combined dataset
        self.data = pd.read_csv(f'combined_{self.disease.lower()}_data.csv')
        
        # Encode genetic data
        for col in self.data.columns:
            if col.startswith('gene_'):
                self.data[col] = self.le_genes.fit_transform(self.data[col])
        
        # Ensure 'risk_level' column exists
        if 'risk_level' in self.data.columns:
            self.data['risk_level'] = self.le_risk.fit_transform(self.data['risk_level'])
        else:
            raise KeyError("Column 'risk_level' is missing in the dataset.")
        
        # Prepare features and target
        self.features = [col for col in self.data.columns if col.startswith('gene_')]
        self.X = self.data[self.features]
        self.y = self.data['risk_level']
    
    def train_model(self):
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        
        # Train the model
        self.model.fit(X_train, y_train)
        
        # Print model accuracy
        print(f"Model accuracy for {self.disease}: {self.model.score(X_test, y_test):.2f}")
    
    def recommend_treatment(self, genetic_profile):
        # Encode the input genetic profile
        encoded_profile = [self.le_genes.transform([genetic_profile[feature]])[0] for feature in self.features]
        
        # Predict risk level
        risk_level = self.model.predict([encoded_profile])[0]
        
        # Check if 'treatment_plan' column exists
        if 'treatment_plan' in self.data.columns:
            treatment_plan = self.data[self.data['risk_level'] == risk_level]['treatment_plan'].iloc[0]
        else:
            raise KeyError("Column 'treatment_plan' is missing in the dataset.")
        
        return self.le_risk.inverse_transform([risk_level])[0], treatment_plan

# Example usage
# recommender = GeneticTreatmentRecommender('Diabetes')
# profile = {'gene_1': 'AA', 'gene_2': 'AT', 'gene_3': 'TT'}
# risk_level, treatment_plan = recommender.recommend_treatment(profile)
# print(f"Risk Level: {risk_level}")
# print(f"Recommended Treatment Plan: {treatment_plan}")
