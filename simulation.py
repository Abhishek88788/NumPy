import sys
import time
import random

def human_type(text, min_speed=0.03, max_speed=0.12, mistake_chance=0.12, newline=True):
    """
    Simulate human typing with frequent mistakes and corrections.
    mistake_chance: probability of a random typo per character (higher = more mistakes)
    """
    for ch in text:
        # Random "thinking pause" to simulate hesitation
        if random.random() < 0.02:
            time.sleep(random.uniform(0.1, 0.5))

        # Introduce typos
        if random.random() < mistake_chance and ch.isalpha():
            wrong_char = random.choice("abcdefghijklmnopqrstuvwxyz")
            print(wrong_char, end="", flush=True)
            time.sleep(random.uniform(0.05, 0.15))
            # Backspace and correction
            print("\b \b", end="", flush=True)
            time.sleep(random.uniform(0.05, 0.2))

        print(ch, end="", flush=True)
        time.sleep(random.uniform(min_speed, max_speed))
    if newline:
        print()
    sys.stdout.flush()

def slow_output(lines, min_delay=0.02, max_delay=0.06, pause_before=0.5):
    """Simulate output appearing slowly, line by line."""
    time.sleep(pause_before)
    for line in lines:
        # Random hesitation before output line
        time.sleep(random.uniform(0.1, 0.3))
        for ch in line:
            print(ch, end="", flush=True)
            time.sleep(random.uniform(min_delay, max_delay))
        print()
        time.sleep(random.uniform(0.2, 0.5))

def main():
    # Start simulated Python session
    time.sleep(1)
    
    human_type(">>> print('Hello, World!')", mistake_chance=0.15)
    slow_output(["Hello, World!"])

    human_type(">>> import numpy as np", mistake_chance=0.12)
    time.sleep(random.uniform(0.5, 1.0))

    human_type(">>> data = np.array([1, 2, 3, 4, 5])", mistake_chance=0.12)
    time.sleep(random.uniform(0.4, 0.8))

    human_type(">>> print('Data:', data)", mistake_chance=0.15)
    slow_output(["Data: [1 2 3 4 5]"])

    human_type(">>> print('Mean:', np.mean(data))", mistake_chance=0.12)
    slow_output(["Mean: 3.0"])

    # For loop with more mistakes
    human_type(">>> for i in range(3):", mistake_chance=0.15)
    time.sleep(random.uniform(0.5, 0.9))
    human_type("...     print('Iteration', i, '->', data * (i + 1))", mistake_chance=0.18)

    slow_output([
        "Iteration 0 -> [1 2 3 4 5]",
        "Iteration 1 -> [ 2  4  6  8 10]",
        "Iteration 2 -> [ 3  6  9 12 15]"
    ], pause_before=0.8)

    human_type(">>> print('Simulation complete!')", mistake_chance=0.15)
    slow_output(["Simulation complete!"])

    time.sleep(random.uniform(0.8, 1.2))
    human_type(">>> exit()", mistake_chance=0.12)

if __name__ == "__main__":
    main()
