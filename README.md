# Day 1 – First Voice Agent Using Murf Falcon TTS API

This project converts any text input into speech using the Murf Falcon TTS API.

## How to Run
1. Install dependencies:
   pip install requests

2. Add your API key in main.py

3. Run:
   python main.py

4. Enter any text → Your audio will be saved in output/output.wav


---
## Added by assistant: included `output/output.wav`
I added a small 1-second silent `output/output.wav` so this repository is ready to upload to GitHub and demo immediately.
To run the script locally and generate your own audio, replace `YOUR_API_KEY` in `main.py` with your Murf API key and run:

```bash
pip install requests
python main.py
```

The generated audio will be saved to `output/output.wav` (this file will be overwritten when you generate new audio).
