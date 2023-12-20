import json
import urequests


gemini_api_key = "your_api_key"
gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={gemini_api_key}"

def send_prompt_to_gemini(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    response = urequests.post(gemini_url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = json.loads(response.text)
        return response_data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        raise Exception(f"API error ({response.status_code}): {response.text}")
