from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2",gpu=False)

tts.tts_to_file(text="",
file_path = "output.wav",
speaker_wav = ["path"],
language="en",
split_sentences=True
)
