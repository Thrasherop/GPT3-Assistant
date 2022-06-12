from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from configs import secrets, config

print("running")

def speak(text):
    authenticator = IAMAuthenticator(secrets.IBM)
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/d480862a-60ee-45e1-a585-8e640d85efff')

    with open(config.PHILO_FILE,'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(text,voice=config.PHILO_VOICE,accept='audio/mp3').get_result().content)


speak("helllo captain america")
