

import RPi.GPIO as GPIO
import time
import pyaudio
import numpy as np
import time
GPIO.setmode(GPIO.BCM)


trigPin = 23
echoPin = 24
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)


try:
    while True:
        GPIO.output(trigPin, 0)
        time.sleep(2E-6)
        GPIO.output(trigPin, 1)
        time.sleep(10E-6)
        GPIO.output(trigPin, 0)
        while GPIO.input(echoPin) == 0:
            pass
        echoStartTime = time.time()
        while GPIO.input(echoPin) == 1:
            pass
        echoStopTime = time.time()
        ptt = echoStopTime - echoStartTime

        distance = 767 * ptt * 5280 * 12 / 3600
        dtt = distance / 2
        print(round(dtt, 1), "Inches")
        time.sleep(.2)

except KeyboardInterrupt:  # If CTRL + C is pressed exit cleanly
    print("Keyboard Interrupt")
    GPIO.cleanup()  # Clean up all GPIO


def main():
    #     distance_to_target = int(input("Enter the distance to target (dtt): "))
    get_distance_to_target(dtt)


def generate_tone(frequency, volume, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    left_samples = (volume * np.sin(2 * np.pi * frequency * t)
                    ).astype(np.float32)
    right_samples = (volume * np.sin(2 * np.pi * frequency *
                     t + np.pi)).astype(np.float32)
    stereo_samples = np.column_stack((left_samples, right_samples))
    return stereo_samples.tobytes()


class ToneGenerator:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = None

    def callback(self, in_data, frame_count, time_info, status):
        if self.samples:
            data = self.samples[:frame_count *
                                self.channels * self.sample_width]
            self.samples = self.samples[frame_count *
                                        self.channels * self.sample_width:]
            return (data, pyaudio.paContinue)
        else:
            return (b'\x00' * frame_count * self.channels * self.sample_width, pyaudio.paComplete)

    def play_samples(self, samples, channels, sample_width):
        self.samples = samples
        self.channels = channels
        self.sample_width = sample_width

        if self.stream is not None and self.stream.is_active():
            self.stream.stop_stream()
            self.stream.close()

        self.stream = self.p.open(format=self.p.get_format_from_width(sample_width),
                                  channels=channels,
                                  rate=44100,
                                  output=True,
                                  stream_callback=self.callback)
        self.stream.start_stream()

        while self.stream.is_active():
            time.sleep(0.1)  # Default sleep time

    def play_samples_with_repetitions(self, samples, channels, sample_width, repetitions, time_between_tones, reduced_sleep=False):
        for _ in range(repetitions):
            self.play_samples(samples, channels, sample_width)
            if reduced_sleep:
                time.sleep(0.01)  # Adjusted sleep time for faster repetitions
            else:
                time.sleep(time_between_tones)

    def close(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()


def get_distance_to_target(dtt):
    generator = ToneGenerator()

    tone_duration = 1.0
    time_between_tones = 1.0

    if 144 <= dtt <= 180:
        volume = 0.02
        samples = generate_tone(440, volume, tone_duration)
        generator.play_samples(
            samples, channels=2, sample_width=generator.p.get_sample_size(pyaudio.paFloat32))
    else:
        # Adjust tone_duration, time_between_tones, and volume based on dtt
        if 96 <= dtt <= 143:
            tone_duration = 0.7
            time_between_tones = 0.2
            volume = 0.2
            repetitions = 2
        elif 48 <= dtt <= 95:
            tone_duration = 0.5
            time_between_tones = 0.1
            volume = 0.4
            repetitions = 3
        elif 24 <= dtt <= 47:
            tone_duration = 0.2
            time_between_tones = 0.01
            volume = 0.6
            repetitions = 4
        elif 12 <= dtt <= 23:
            tone_duration = 0.05
            time_between_tones = 0.005  # Reduced time between repetitions
            volume = 0.9
            repetitions = 5

        samples = generate_tone(440, volume, tone_duration)
        generator.play_samples_with_repetitions(samples, channels=2, sample_width=generator.p.get_sample_size(
            pyaudio.paFloat32), repetitions=repetitions, time_between_tones=time_between_tones, reduced_sleep=(12 <= dtt <= 23))

    generator.close()


if __name__ == "__main__":
    main()
