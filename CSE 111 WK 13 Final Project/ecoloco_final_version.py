import RPi.GPIO as GPIO
import time
import pyaudio
import numpy as np


def setup_gpio(trig_pin, echo_pin):
    """
    Set up GPIO pinout for the ultrasonic sensor to be used with a Raspberry Pi.
    Use the correct pins based on your hardware.

    Parameters:
    - trig_pin: GPIO pin for trigger
    - echo_pin: GPIO pin for echo
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)


def cleanup_gpio():
    """
    Clean up GPIO resources.
    """
    GPIO.cleanup()


def measure_distance(trig_pin, echo_pin):
    """
    Measure distance using an ultrasonic sensor.

    Parameters:
    - trig_pin: GPIO pin for trigger
    - echo_pin: GPIO pin for echo

    Returns:
    - Rounded distance to target in inches (dtt)
    """
    GPIO.output(trig_pin, 0)
    time.sleep(2E-6)
    GPIO.output(trig_pin, 1)
    time.sleep(10E-6)
    GPIO.output(trig_pin, 0)
    while GPIO.input(echo_pin) == 0:
        pass
    echo_start_time = time.time()
    while GPIO.input(echo_pin) == 1:
        pass
    echo_stop_time = time.time()

    # Calculates ping travel time (ptt).
    # Time it takes sound waves to return.
    ptt = echo_stop_time - echo_start_time
    distance = 767 * ptt * 5280 * 12 / 3600

    # Distance to target = dtt
    dtt = distance / 2
    return round(dtt, 1)


class ToneGenerator:
    def __init__(self):
        """
        Creates a ToneGenerator class and initializes PyAudio for tone generation.
        """
        self.sample_width = None
        self.channels = None
        self.samples = None
        self.p = pyaudio.PyAudio()
        self.stream = None

    def callback(self, in_data, frame_count, time_info, status):
        """
        Callback function for PyAudio stream. 
        Callback helps PyAudio manage the playback process,
        letting it know when the stram has completed

        Parameters:
        - in_data: Input audio data
        - frame_count: Number of frames
        - time_info: Time information
        - status: Stream status

        Returns:
        - Tuple of output audio data and status
        """
        if self.samples:
            data = self.samples[:frame_count *
                                self.channels * self.sample_width]
            self.samples = self.samples[frame_count *
                                        self.channels * self.sample_width:]
            return data, pyaudio.paContinue
        else:
            # b'\x00' is a byte with the hexadecimal value of 00, which corresponds to silence in audio data.
            return b'\x00' * frame_count * self.channels * self.sample_width, pyaudio.paComplete

    def play_samples(self, samples, channels, sample_width):
        """
        Play audio samples once.

        Parameters:
        - samples: Audio samples
        - channels: Number of channels
        - sample_width: Sample width
        """
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

    def play_samples_with_repetitions(self, samples, channels, sample_width, repetitions, time_between_tones,
                                      reduced_sleep=False):
        """
        Play audio samples with repetitions.

        Parameters:
        - samples: Audio samples
        - channels: Number of channels
        - sample_width: Sample width
        - repetitions: Number of repetitions
        - time_between_tones: Time between repetitions
        - reduced_sleep: Use reduced sleep time for faster repetitions
        """
        for _ in range(repetitions):
            self.play_samples(samples, channels, sample_width)
            if reduced_sleep:
                time.sleep(0.001)  # Adjusted sleep time for faster repetitions
            else:
                time.sleep(time_between_tones)

    def close(self):
        """
        Close PyAudio resources.
        """
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()


def main():
    trig_pin = 23
    echo_pin = 24
    setup_gpio(trig_pin, echo_pin)

    try:
        while True:
            # Measure distance and print result
            dtt = measure_distance(trig_pin, echo_pin)
            print(f"{dtt} Inches")

            # Create ToneGenerator instance and play tone based on distance
            generator = ToneGenerator()
            get_distance_to_target(dtt, generator)
            generator.close()

            time.sleep(0.2)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")

    finally:
        cleanup_gpio()


def generate_tone(frequency, volume, duration, sample_rate=44100):
    """
    Generate audio samples for a tone, using numpy.
    This allows for volume, frequency, and duration adjustment
    and creates a left and right sample for stereo sound.

    Parameters:
    - frequency: Tone frequency
    - volume: Tone volume
    - duration: Tone duration
    - sample_rate: Sample rate

    Returns:
    - Audio samples
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    left_samples = (volume * np.sin(2 * np.pi * frequency * t)
                    ).astype(np.float32)
    right_samples = (volume * np.sin(2 * np.pi * frequency *
                     t + np.pi)).astype(np.float32)
    stereo_samples = np.column_stack((left_samples, right_samples))
    return stereo_samples.tobytes()


def get_distance_to_target(dtt, generator):
    """
    Play a tone based on distance using a ToneGenerator instance.

    Parameters:
    - dtt: Distance to target in inches
    - generator: ToneGenerator instance
    """
    tone_settings = {
        (144, 180): {'frequency': 330, 'volume': 0.02, 'duration': 1.0, 'repetitions': 1, 'time_between_tones': 1.0},
        (96, 143): {'frequency': 440, 'volume': 0.2, 'duration': 0.7, 'repetitions': 2, 'time_between_tones': 0.2},
        (48, 95): {'frequency': 550, 'volume': 0.4, 'duration': 0.5, 'repetitions': 3, 'time_between_tones': 0.1},
        (24, 47): {'frequency': 660, 'volume': 0.6, 'duration': 0.2, 'repetitions': 4, 'time_between_tones': 0.01},
        (12, 23): {'frequency': 770, 'volume': 0.9, 'duration': 0.05, 'repetitions': 5, 'time_between_tones': 0.005}
    }

    for (lower, upper), settings in tone_settings.items():
        if lower <= dtt <= upper:
            samples = generate_tone(
                settings['frequency'], settings['volume'], settings['duration'])
            generator.play_samples_with_repetitions(samples, channels=2,
                                                    sample_width=generator.p.get_sample_size(
                                                        pyaudio.paFloat32),
                                                    repetitions=settings['repetitions'],
                                                    time_between_tones=settings['time_between_tones'],
                                                    reduced_sleep=(12 <= dtt <= 23))
            return

    # Default case when dtt is not in any range
    return


if __name__ == "__main__":
    main()
