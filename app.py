from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        user_preferences = request.json.get('preferences')
        if user_preferences is None:
            return jsonify({'error': 'Invalid JSON format or missing preferences'}), 400
        
        recommendations = get_recommendations(user_preferences)
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_recommendations(preferences):
    # Placeholder logic to generate recommendations based on user preferences
    return ["recipe1", "recipe2", "recipe3"]

if __name__ == '__main__':
    app.run(debug=True)
