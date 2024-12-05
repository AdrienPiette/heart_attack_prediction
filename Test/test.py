#

import pickle

encoder_path = r'C:\Users\pieta\OneDrive\Bureau\Heart_attack_model\heart_attack_prediction\Model_training\encoders.pkl'
encoder = pickle.load(open(encoder_path, 'rb'))

print(type(encoder))  # Vérifiez le type
print(encoder) 
