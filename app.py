from flask import Flask, request, jsonify, render_template
from ml_model import GeneticTreatmentRecommender

app = Flask(__name__)

# Initialize recommenders for each disease
recommenders = {
    'Diabetes': GeneticTreatmentRecommender('Diabetes'),
    'Hypertension': GeneticTreatmentRecommender('Hypertension'),
    'Hypercholesterolemia': GeneticTreatmentRecommender('Hypercholesterolemia'),
    'Asthma': GeneticTreatmentRecommender('Asthma'),
    'Obesity': GeneticTreatmentRecommender('Obesity')
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    genetic_profile = {f"gene_{i+1}": data[f"gene_{i+1}"] for i in range(3)}
    disease = data['disease']
    
    if disease not in recommenders:
        return jsonify({'error': 'Invalid disease specified'}), 400
    
    risk_level, treatment_plan = recommenders[disease].recommend_treatment(genetic_profile)
    
    return jsonify({
        'disease': disease,
        'risk_level': risk_level,
        'treatment_plan': treatment_plan
    })

if __name__ == '__main__':
    app.run(debug=True)