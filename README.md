# AI Model Recommendation API

## Overview
A Flask-based API that helps users find the most suitable AI model for their specific use cases and requirements.

## Features
- Recommend AI models based on use cases
- Retrieve detailed information about various AI models
- Support for multiple prominent AI models
- Flexible scoring mechanism

## Supported Models
- Claude (Anthropic)
- ChatGPT (OpenAI)
- Gemini (Google)
- DeepSeek
- Mistral

## API Endpoints

### 1. Model Recommendation
- **URL**: `/recommend`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "use_case": "coding",
    "requirements": ["low_cost", "code_generation"]
  }
  ```
- **Response**: Recommended model with details

### 2. All Models
- **URL**: `/models`
- **Method**: GET
- **Response**: Details of all AI models

