#!/usr/bin/env python3
"""
============================================================
 Program:      Dramatic Hello World Printer v1.3b
 Author:       Example Script
 Created:      2026-04-08

 Description:
     This script demonstrates a stylized and slightly theatrical
     approach to printing the classic "Hello World" message.
     Instead of simply outputting text, it simulates a progress
     sequence with timing delays and formatted terminal output.

 Features:
     - Prints "Hello World" multiple times (default: 5)
     - Displays a progress counter for each iteration
     - Uses time delays to create a dynamic visual effect
     - Structured with functions for readability and reuse

 Disclaimer:
     This is purely a demonstration script designed to look
     impressive and well-documented. It is intentionally
     more complex than necessary for educational purposes.

 Usage:
     Run directly in a terminal:
         python3 script_name.py
============================================================
"""

# Import standard library modules
import time      # Used for adding delays between prints
import sys       # Used for low-level output control (stdout)


def dramatic_print(message, repetitions=5, delay=0.3):
    """
    Prints a message multiple times with a progress indicator
    and a slight delay between each output.

    Parameters:
        message (str): The message to be printed
        repetitions (int): Number of times to print the message
        delay (float): Time delay (in seconds) between prints
    """

    # Loop through the number of requested repetitions
    for i in range(1, repetitions + 1):

        # Write output to the same line using carriage return
        # This creates a "live updating" effect in the terminal
        sys.stdout.write(f"\r[{i}/{repetitions}] ➤ {message}")

        # Force the output buffer to flush immediately
        # (ensures real-time display rather than delayed output)
        sys.stdout.flush()

        # Pause execution briefly to simulate processing time
        time.sleep(delay)

        # Move to the next line after each iteration
        print()


def main():
    """
    Main entry point for the script.
    Handles initialization, user-facing output, and execution flow.
    """

    # Create a visual banner for cleaner terminal presentation
    banner = "=" * 40

    # Display initialization header
    print(banner)
    print("   Initializing Output Sequence...")
    print(banner)

    # Short pause before starting main output
    time.sleep(0.5)

    # Call the core function to print the message repeatedly
    dramatic_print("Hello World 🚀", repetitions=5)

    # Final status message indicating completion
    print("\nProcess complete. ✔")


# Standard Python entry point check
# Ensures that main() runs only when the script is executed directly
if __name__ == "__main__":
    main()