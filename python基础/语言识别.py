import os
import time
from google.cloud import speech, translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service_account_key.json"  # 替换为你的服务账户密钥文件路径
language_code = "en"  # 目标语言代码，这里以英文为例

def transcribe_speech():
    client = speech.SpeechClient()

    config = {
        "encoding": speech.RecognitionConfig.AudioEncoding.LINEAR16,
        "sample_rate_hertz": 16000,
        "language_code": "en-US",
    }

    streaming_config = {
        "config": config,
        "interim_results": True,
    }

    audio_generator = get_audio_stream()   # 从麦克风获取实时音频流

    requests = (
        speech.StreamingRecognizeRequest(audio_content=content)
        for content in audio_generator
    )

    responses = client.streaming_recognize(streaming_config, requests)

    for response in responses:
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))
            translate_text(result.alternatives[0].transcript)

def get_audio_stream():
    # 在这个函数中，你需要实现从麦克风获取实时音频流的逻辑
    # 你可以使用相关库（如PyAudio）来实现这个功能
    # 返回音频流的生成器

def translate_text(text):
    client = translate.TranslationServiceClient()

    parent = client.location_path("global", "us-central1")
    target_language = language_code

    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type="text/plain",  # MIME类型
        source_language_code="en-US",
        target_language_code=target_language,
    )

    for translation in response.translations:
        print("Translation: {}".format(translation.translated_text))

if __name__ == "__main__":
    transcribe_speech()