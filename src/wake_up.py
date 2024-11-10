import pvporcupine
import pyaudio
import struct

class WakeWordDetector:
    def __init__(self, access_key, keywords=["picovoice"], sensitivities=[0.5]):
        self.access_key = access_key
        self.keywords = keywords
        self.sensitivities = sensitivities
        self.porcupine = pvporcupine.create(access_key=self.access_key, keywords=self.keywords, sensitivities=self.sensitivities)
        self.audio_stream = None

    def start(self):
        self.audio_stream = pyaudio.PyAudio().open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def listen(self):
        pcm = self.audio_stream.read(self.porcupine.frame_length)
        pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
        result = self.porcupine.process(pcm)
        return result >= 0

    def stop(self):
        if self.audio_stream is not None:
            self.audio_stream.close()
        self.porcupine.delete()