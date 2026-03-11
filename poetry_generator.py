import random

class PoetryGenerator:
    def __init__(self):
        self.lines = [
            ["In shadows deep", "where code dreams sleep", "a bug awakens."],
            ["Pixels whisper", "eternal glitch", "life's syntax error."],
            ["Void stares back", "at player's quest", "futile reload."],
            ["Ego's mirror", "shatters in bits", "simulation ends."]
        ]

    def generate_haiku(self):
        haiku = random.choice(self.lines)
        return "\n".join(haiku)

# Example usage (integrate into main.py)
if __name__ == "__main__":
    gen = PoetryGenerator()
    print(gen.generate_haiku())
