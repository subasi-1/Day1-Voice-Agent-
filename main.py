import requests

API_KEY = "YOUR_API_KEY"
URL = "https://api.murf.ai/v1/speech/generate"

def generate_voice(text):
    payload = {
        "voice": "en-US-murf-falcon",
        "text": text,
        "format": "wav"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "api-key": API_KEY
    }

    response = requests.post(URL, json=payload, headers=headers)

    if response.status_code == 200:
        output_url = response.json()["audioUrl"]
        audio_data = requests.get(output_url).content

        with open("output/output.wav", "wb") as f:
            f.write(audio_data)

        print("Audio generated successfully! Saved at output/output.wav ✔️")
    else:
        print("Error:", response.text)

# Run the function
if __name__ == "__main__":
    text = input("Enter text to convert into speech: ")
    generate_voice(text)
