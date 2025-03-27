from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

AI_MODELS = {
    "claude": {
        "provider": "Anthropic",
        "strengths": [
            "Nuanced reasoning",
            "Ethical AI",
            "Detailed technical tasks",
            "Long-context understanding"
        ],
        "best_for": [
            "Complex analysis",
            "Technical writing",
            "Research assistance",
            "Coding support"
        ],
        "versions": ["Claude 3 Haiku", "Claude 3 Sonnet", "Claude 3 Opus"],
        "context_window": "Up to 200K tokens",
        "pricing_tier": "Mid to High"
    },
    "chatgpt": {
        "provider": "OpenAI",
        "strengths": [
            "General conversation",
            "Creative writing",
            "Quick responses",
            "Broad knowledge base"
        ],
        "best_for": [
            "Content creation",
            "Brainstorming",
            "Basic coding",
            "Language translation"
        ],
        "versions": ["GPT-3.5", "GPT-4", "GPT-4 Turbo"],
        "context_window": "Up to 128K tokens",
        "pricing_tier": "Low to High"
    },
    "gemini": {
        "provider": "Google",
        "strengths": [
            "Multimodal capabilities",
            "Web search integration",
            "Real-time information",
            "Advanced reasoning"
        ],
        "best_for": [
            "Research",
            "Image analysis",
            "Multimedia tasks",
            "Complex problem-solving"
        ],
        "versions": ["Gemini Pro", "Gemini Ultra", "Gemini Advanced"],
        "context_window": "Up to 1M tokens",
        "pricing_tier": "Low to Mid"
    },
    "deepseek": {
        "provider": "DeepSeek",
        "strengths": [
            "Code generation",
            "Multilingual support",
            "Open-source models",
            "Cost-effective",
            "mathematical reasoning"
        ],
        "best_for": [
            "Programming tasks",
            "Code completion",
            "Technical documentation",
            "Multilingual projects"
        ],
        "versions": ["DeepSeek Coder", "DeepSeek LLM"],
        "context_window": "Up to 64K tokens",
        "pricing_tier": "Low"
    },
    "mistral": {
        "provider": "Mistral AI",
        "strengths": [
            "Open-source models",
            "High performance",
            "Efficient processing",
            "Strong reasoning"
        ],
        "best_for": [
            "Open-source projects",
            "Research",
            "Lightweight applications",
            "Custom fine-tuning"
        ],
        "versions": ["Mistral 7B", "Mistral Large", "Mixtral 8x7B"],
        "context_window": "Up to 32K tokens",
        "pricing_tier": "Low to Mid"
    }
}

@app.route('/recommend', methods=['POST'])
def recommend_model():
    """
    Recommend AI models based on user requirements
    """
    data = request.json
    use_case = data.get('use_case', '').lower()
    requirements = data.get('requirements', [])
    
    # Default recommendation
    if not use_case and not requirements:
        return jsonify({
            "recommendation": "Claude 3 Sonnet",
            "reason": "Balanced performance for general tasks",
            "details": AI_MODELS["claude"]
        })
    
    # Scoring mechanism
    scores = {model: 0 for model in AI_MODELS}
    
    # Score based on use case
    use_case_mapping = {
        "coding": ["claude", "deepseek", "chatgpt"],
        "writing": ["claude", "chatgpt", "gemini"],
        "research": ["claude", "gemini", "mistral"],
        "translation": ["chatgpt", "gemini", "claude"],
        "creative": ["chatgpt", "claude", "gemini"]
    }
    
    if use_case in use_case_mapping:
        for model in use_case_mapping[use_case]:
            scores[model] += 3
    
    # Score based on specific requirements
    requirement_mapping = {
        "multilingual": ["gemini", "deepseek"],
        "low_cost": ["deepseek", "mistral"],
        "high_context": ["claude", "gemini"],
        "code_generation": ["deepseek", "claude"],
        "open_source": ["mistral", "deepseek"]
    }
    
    for req in requirements:
        if req.lower() in requirement_mapping:
            for model in requirement_mapping[req.lower()]:
                scores[model] += 2
    
    # Find top recommendation
    top_model = max(scores, key=scores.get)
    
    return jsonify({
        "recommendation": top_model.capitalize(),
        "score": scores[top_model],
        "reason": f"Best suited for {use_case} with requirements {requirements}",
        "details": AI_MODELS[top_model]
    })

@app.route('/models', methods=['GET'])
def get_all_models():
    """
    Return details of all available AI models
    """
    return jsonify(AI_MODELS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
