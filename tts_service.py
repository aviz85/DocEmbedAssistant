import os
from gtts import gTTS
import base64
import tempfile

class TTSService:
    def __init__(self):
        self.language = 'he'  # Hebrew language code
        
    def text_to_speech(self, text: str) -> str:
        """Convert text to speech and return as base64 audio data"""
        try:
            # Create a temporary file to store the audio
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                # Generate speech
                tts = gTTS(text=text, lang=self.language, slow=False)
                tts.save(fp.name)
                
                # Read the file and convert to base64
                with open(fp.name, 'rb') as audio_file:
                    audio_data = base64.b64encode(audio_file.read()).decode()
                
                # Clean up the temporary file
                os.unlink(fp.name)
                
                return audio_data
                
        except Exception as e:
            print(f"Error generating speech: {e}")
            return None
