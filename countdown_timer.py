import time

def countdown(total_seconds):
    """Display a countdown timer in MM:SS format."""

    if total_seconds < 0:
        raise ValueError("Time cannot be negative.")

    try:
        while total_seconds >= 0:
            minutes, seconds = divmod(total_seconds, 60)
            print(f"\rTime Left: {minutes:02d}:{seconds:02d}", end="", flush=True)

            if total_seconds == 0:
                break

            time.sleep(1)
            total_seconds -= 1

        print("\n⏰ Time's up!")

    except KeyboardInterrupt:
        print("\nCountdown stopped by user.")


def main():
    while True:
        try:
            seconds = int(input("Enter countdown time (in seconds): "))

            if seconds < 0:
                print("Please enter a positive number.")
                continue

            countdown(seconds)
            break

        except ValueError:
            print("Invalid input! Please enter a whole number.")


if __name__ == "__main__":
    main()