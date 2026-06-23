import sys
import time
import os

# Enable ANSI escape codes on Windows cmd/PowerShell
if os.name == 'nt':
    os.system("")

# Dictionary of ANSI color codes
COLORS = {
    "red": "\033[91m",
    "yellow": "\033[93m",
    "green": "\033[92m",
    "cyan": "\033[96m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "reset": "\033[0m"
}

# Create a sequence of just the colors for looping
rainbow_sequence = list(COLORS.values())[:-1] 

def clear_screen():
    """Clears the terminal screen for a fresh canvas."""
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_spinner(duration=2.5):
    """Animation 1: A smooth loading spinner."""
    spinners = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{COLORS['cyan']}Booting up terminal magic... {spinners[i % len(spinners)]}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * 40 + "\r") # Clear the line when done

def type_rainbow(text, speed=0.05):
    """Animation 2: Types text out character by character in rainbow colors."""
    for i, char in enumerate(text):
        if char == " ":
            sys.stdout.write(char)
        else:
            color = rainbow_sequence[i % len(rainbow_sequence)]
            sys.stdout.write(f"{color}{char}")
        sys.stdout.flush()
        time.sleep(speed)
    print(COLORS["reset"])

def color_wave(text, loops=30, speed=0.08):
    """Animation 3: Creates a continuous sliding rainbow wave effect."""
    for offset in range(loops):
        sys.stdout.write("\r")
        for i, char in enumerate(text):
            if char == " ":
                sys.stdout.write(char)
            else:
                color = rainbow_sequence[(i + offset) % len(rainbow_sequence)]
                sys.stdout.write(f"{color}{char}")
        sys.stdout.flush()
        time.sleep(speed)
    print(COLORS["reset"])

def main():
    clear_screen()
    
    # 1. Play the spinner
    loading_spinner()
    
    # 2. Type out the initial greeting
    print("\n")
    type_rainbow(">>> H E L L O ,  W O R L D ! <<<", speed=0.08)
    time.sleep(1)
    
    # 3. Play the color wave
    print("\nInitiating color wave...\n")
    time.sleep(0.5)
    color_wave("    H E L L O   W O R L D    ", loops=40, speed=0.06)
    
    # Sign off
    print(f"\n\n{COLORS['green']}Animation complete. Have a great day!{COLORS['reset']}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Gracefully handle the user pressing Ctrl+C mid-animation
        print(f"\n{COLORS['reset']}Animation halted by user.")
        sys.exit()
