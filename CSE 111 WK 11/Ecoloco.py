
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)
# import pyaudio


# trigPin=23
# echoPin=24
# GPIO.setup(trigPin, GPIO.OUT)
# GPIO.setup(echoPin, GPIO.IN)


# try:
#     while True:
#         GPIO.output(trigPin, 0)
#         time.sleep(2E-6)
#         GPIO.output(trigPin, 1)
#         time.sleep(10E-6)
#         GPIO.output(trigPin, 0)
#         while GPIO.input(echoPin) == 0:
#             pass
#         echoStartTime = time.time()
#         while GPIO.input(echoPin) == 1:
#             pass
#         echoStopTime =t ime.time()
#         pingTravelTime = echoStopTime - echoStartTime
#         print(int(pingTravelTime*1E6))

#         distance = 767 * ptt * 5280 * 12 / 3600
#         dtt = distance / 2
#         print(round(dtt, 1), "Inches")
#         time.sleep(.2)

# except KeyboardInterrupt():
#     GPIO.cleanup()
#     print("GPIO Good to Go")


# import numpy as np
# import pysine
# import time
# pysine.sine(frequency=330.0, duration=1)


# import numpy as np
# import sounddevice as sd


# def main():
#     # Set parameters
#     frequency_left = 330  # Frequency for the left channel (Hz)
#     frequency_right = 330  # Frequency for the right channel (Hz)
#     duration = 1  # Duration in seconds
#     volume_left = .5  # Volume for the left channel (adjust as needed)
#     volume_right = .5  # Volume for the right channel (adjust as needed)
#     pan = 'center'  # 'left', 'right', or 'center'

#     # Generate stereo sine wave with adjustable volume and pan
#     stereo_wave = generate_stereo_sine_wave(
#         frequency_left, frequency_right, duration, volume_left, volume_right, pan)

#     # Play the stereo sine wave using sounddevice
#     sd.play(stereo_wave, samplerate=44100, blocking=True)


# def generate_stereo_sine_wave(frequency_left, frequency_right, duration, volume_left, volume_right, pan):
#     # Generate time values
#     t = np.linspace(0, duration, int(duration * 44100), endpoint=False)

#     # Generate left and right channel sine waves
#     left_channel = volume_left * np.sin(2 * np.pi * frequency_left * t)
#     right_channel = volume_right * np.sin(2 * np.pi * frequency_right * t)

#     # Adjust panning
#     if pan == 'left':
#         left_channel *= 1.0
#         right_channel *= 0.0
#     elif pan == 'right':
#         left_channel *= 0.0
#         right_channel *= 1.0
#     else:
#         # Default to center if pan is not specified or invalid
#         left_channel *= 1.0
#         right_channel *= 1.0

#     # Combine the left and right channels
#     stereo_wave = np.column_stack((left_channel, right_channel))

#     return stereo_wave


# def get_distance_to_target(dtt):

#     if 109 <= dtt <= 144:
#         duration = 1
#         volume = .02
#     elif 73 <= dtt <= 108:
#         duration = .8
#         volume = .1
#     elif 37 <= dtt <= 72:
#         duration = .6
#         volume = .4
#     elif 25 <= dtt <= 36:
#         duration = .4
#         volume = .8
#     elif 12 <= dtt <= 24:
#         duration = .2
#         volume = 1


# if __name__ == "__main__":
#     main()


# import numpy as np
# import sounddevice as sd


# def main():
#     # Set parameters
#     frequency_left = 330  # Frequency for the left channel (Hz)
#     frequency_right = 330  # Frequency for the right channel (Hz)

#     # Example distance to target (replace this with your actual distance value)
#     dtt = 72

#     # Get duration and volume based on distance to target
#     duration, volume = get_distance_to_target(dtt)

#     # Generate stereo sine wave with adjustable volume and pan
#     stereo_wave = generate_stereo_sine_wave(
#         frequency_left, frequency_right, duration, volume, 'center')

#     # Play the stereo sine wave using sounddevice
#     sd.play(stereo_wave, samplerate=44100, blocking=True)


# def generate_stereo_sine_wave(frequency_left, frequency_right, duration, volume, pan):
#     # Generate time values
#     t = np.linspace(0, duration, int(duration * 44100), endpoint=False)

#     # Generate left and right channel sine waves
#     left_channel = volume * np.sin(2 * np.pi * frequency_left * t)
#     right_channel = volume * np.sin(2 * np.pi * frequency_right * t)

#     # Adjust panning
#     if pan == 'left':
#         left_channel *= 1.0
#         right_channel *= 0.0
#     elif pan == 'right':
#         left_channel *= 0.0
#         right_channel *= 1.0
#     else:
#         # Default to center if pan is not specified or invalid
#         left_channel *= 1.0
#         right_channel *= 1.0

#     # Combine the left and right channels
#     stereo_wave = np.column_stack((left_channel, right_channel))

#     return stereo_wave


# def get_distance_to_target(dtt):
#     if 109 <= dtt <= 144:
#         duration = 1
#         volume = 0.02
#     elif 73 <= dtt <= 108:
#         duration = 0.8
#         volume = 0.1
#     elif 37 <= dtt <= 72:
#         duration = 0.6
#         volume = 0.4
#     elif 25 <= dtt <= 36:
#         duration = 0.4
#         volume = 0.8
#     elif 12 <= dtt <= 24:
#         duration = 0.2
#         volume = 1.0
#     else:
#         # Default values if distance is outside the specified ranges
#         duration = 1
#         volume = 0.5

#     return duration, volume


# if __name__ == "__main__":
#     main()


# import numpy as np
# import sounddevice as sd


# def generate_stereo_sine_wave(frequency_left, frequency_right, duration, volume):
#     # Generate time values
#     t = np.linspace(0, duration, int(duration * 44100), endpoint=False)

#     # Generate left and right channel sine waves
#     left_channel = volume * np.sin(2 * np.pi * frequency_left * t)
#     right_channel = volume * np.sin(2 * np.pi * frequency_right * t)

#     # Combine the left and right channels
#     stereo_wave = np.column_stack((left_channel, right_channel))

#     return stereo_wave


# def callback(outdata, frames, time, status):
#     if status:
#         print(status)
#     outdata[:frames] = generate_stereo_sine_wave(
#         frequency_left, frequency_right, duration, volume)
#     # Update distance to target for the next iteration (replace with actual method to update dtt)
#     dtt -= 10


# # Set parameters
# frequency_left = 330  # Frequency for the left channel (Hz)
# frequency_right = 330  # Frequency for the right channel (Hz)
# duration = 1.0
# volume = 0.5
# dtt = 120

# # Create stream
# with sd.OutputStream(callback=callback, channels=2):
#     # Sleep to allow time for the callback to execute
#     sd.sleep(int(duration * 1000))

# # Repeat the above code block as needed for the desired number of repetitions


# import sounddevice as sd
# import numpy as np
# import time


# def generate_tone(frequency, volume, duration):
#     sample_rate = 44100
#     t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
#     samples = (volume * np.sin(2 * np.pi * frequency * t)).astype(np.float32)
#     sd.play(samples, sample_rate)
#     sd.wait()


# def play_tone(dtt):
#     if 109 <= dtt <= 144:
#         generate_tone(440, 0.02, 1)  # Frequency of 440 Hz for one second
#     elif 73 <= dtt <= 108:
#         # Adjust the volume based on distance
#         volume = 0.02 + (144 - dtt) * 0.01
#         # Adjust the duration based on distance
#         duration = 1 - (144 - dtt) * 0.01
#         generate_tone(440, volume, duration)


# # Example usage
# distance_to_target = int(input("Enter the distance to target: "))
# play_tone(distance_to_target)


# import sounddevice as sd
# import numpy as np
# import time


# def generate_tone(frequency, volume, duration):
#     sample_rate = 44100
#     t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
#     samples = (volume * np.sin(2 * np.pi * frequency * t)).astype(np.float32)
#     sd.play(samples, sample_rate)
#     sd.wait()


# def play_tone(dtt):
#     repetitions = 1  # Initialize repetitions variable
#     tone_duration = 1.0  # Initialize tone_duration variable
#     time_between_tones = 1.0  # Initialize time_between_tones

#     if 109 <= dtt <= 144:
#         generate_tone(440, .02, 1)  # Frequency of 440 Hz for one second
#     elif 73 <= dtt <= 108:
#         repetitions = 2
#         time_between_tones = 0.9  # Reduced time between tones
#         tone_duration = 0.8  # Shorter duration for each tone
#     elif 36 <= dtt <= 72:
#         repetitions = 3
#         time_between_tones = 0.4  # Standard time between tones
#         tone_duration = 0.75  # Standard duration for each tone
#     elif 24 <= dtt <= 35:
#         repetitions = 4
#         time_between_tones = 0.4  # Increased time between tones
#         tone_duration = .6  # Longer duration for each tone
#     elif 12 <= dtt <= 23:
#         repetitions = 5
#         time_between_tones = 0.3  # Further increased time between tones
#         tone_duration = .3  # Further longer duration for each tone
#     elif 1 <= dtt <= 11:
#         repetitions = 6
#         time_between_tones = 0.01  # Rapid time between tones
#         tone_duration = 0.3  # Very short duration for each tone
#     else:
#         return  # Do nothing if not in any range

#     # Play the tone with the specified repetitions, time between tones, and tone duration
#     for _ in range(repetitions):
#         generate_tone(440, 0.02, tone_duration)
#         time.sleep(time_between_tones)


# # Example usage
# distance_to_target = int(input("Enter the distance to target: "))
# play_tone(distance_to_target)


# import sounddevice as sd
# import numpy as np
# import time


# def main():
#     # Example usage
#     distance_to_target = int(input("Enter the distance to target: "))
#     play_tone(distance_to_target)


# def generate_tone(frequency, volume, duration):
#     sample_rate = 44100
#     t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
#     samples = (volume * np.sin(2 * np.pi * frequency * t)).astype(np.float32)
#     sd.play(samples, sample_rate)
#     sd.wait()


# def play_tone(dtt):
#     tone_duration = 1.0  # Initialize tone_duration variable
#     time_between_tones = 1.0  # Initialize time_between_tones
#     volume = .02  # Initialize volume

#     if 144 <= dtt <= 180:
#         tone_duration = 1
#     elif 96 <= dtt <= 143:
#         repetitions = 2
#         time_between_tones = 0.6  # Reduced time between tones
#         tone_duration = 0.7  # Shorter duration for each tone
#         volume = .05
#     elif 48 <= dtt <= 95:
#         repetitions = 3
#         time_between_tones = 0.2  # Standard time between tones
#         tone_duration = 0.5  # Standard duration for each tone
#         volume = .1
#     elif 24 <= dtt <= 47:
#         repetitions = 4
#         time_between_tones = 0.05  # Increased time between tones
#         tone_duration = 0.4  # Longer duration for each tone
#         volume = .2
#     elif 12 <= dtt <= 23:
#         repetitions = 5
#         time_between_tones = 0.01  # Further increased time between tones
#         tone_duration = 0.3  # Further longer duration for each tone
#         volume = .7
#     # elif 1 <= dtt <= 11:
#     #     repetitions = 6
#     #     time_between_tones = 0.01  # Rapid time between tones
#     #     tone_duration = 0.3  # Very short duration for each tone
#     else:
#         return  # Do nothing if not in any range

#     # Play the tone with the specified repetitions, time between tones, and tone duration
#     if 144 <= dtt <= 180:
#         generate_tone(440, 0.02, tone_duration)
#     else:
#         for _ in range(repetitions):
#             generate_tone(440, volume, tone_duration)
#             time.sleep(time_between_tones)


# if __name__ == "__main__":
#     main()


import numpy as np
import time
import pyaudio


def generate_tone(frequency, volume, duration):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generate separate samples for left and right channels
    left_samples = (volume * np.sin(2 * np.pi * frequency * t)
                    ).astype(np.float32)
    right_samples = (volume * np.sin(2 * np.pi * frequency *
                     t + np.pi)).astype(np.float32)

    # Combine left and right channels
    stereo_samples = np.column_stack((left_samples, right_samples))
    return stereo_samples


def get_distance_to_target(dtt):
    tone_duration = 1.0  # Initialize tone_duration variable
    time_between_tones = 1.0  # Initialize time_between_tones
    volume = 0.04  # Initialize volume

    if 144 <= dtt <= 180:
        tone_duration = 1
    elif 96 <= dtt <= 143:
        repetitions = 2
        time_between_tones = 0.2  # Reduced time between tones
        tone_duration = 0.7  # Shorter duration for each tone
        volume = 0.07
    elif 48 <= dtt <= 95:
        repetitions = 3
        time_between_tones = 0.2  # Standard time between tones
        tone_duration = 0.5  # Standard duration for each tone
        volume = 0.2
    elif 24 <= dtt <= 47:
        repetitions = 4
        time_between_tones = 0.05  # Increased time between tones
        tone_duration = 0.4  # Longer duration for each tone
        volume = 0.4
    elif 12 <= dtt <= 23:
        repetitions = 5
        time_between_tones = 0.02  # Further increased time between tones
        tone_duration = 0.3  # Further longer duration for each tone
        volume = 0.7
    else:
        return  # Do nothing if not in any range

    # Play the stereo tone with the specified repetitions, time between tones, and tone duration
    if 144 <= dtt <= 180:
        play_stereo_sound(generate_tone(440, 0.02, tone_duration))
    else:
        for _ in range(repetitions):
            play_stereo_sound(generate_tone(440, volume, tone_duration))
            time.sleep(time_between_tones)


def play_stereo_sound(stereo_samples):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=2,  # Two channels for stereo
                    rate=44100,
                    output=True)
    stream.write(stereo_samples.tobytes())
    stream.close()
    p.terminate()


def main():
    # Example usage
    distance_to_target = int(input("Enter the distance to target: "))
    get_distance_to_target(distance_to_target)


if __name__ == "__main__":
    main()
