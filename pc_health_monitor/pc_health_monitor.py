import psutil
import os
import time
from datetime import datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


while True:

    clear_screen()

    print("=" * 60)
    print("        PC HEALTH MONITOR")
    print("=" * 60)

    # CPU
    cpu = psutil.cpu_percent(interval=1)

    # RAM
    ram = psutil.virtual_memory()

    # Disk
    disk = psutil.disk_usage("/")

    # Battery
    battery = psutil.sensors_battery()

    # Boot Time
    boot = datetime.fromtimestamp(psutil.boot_time())

    print(f"CPU Usage          : {cpu}%")

    print(f"RAM Usage          : {ram.percent}%")
    print(f"RAM Used           : {round(ram.used / (1024**3),2)} GB")
    print(f"RAM Total          : {round(ram.total / (1024**3),2)} GB")

    print()

    print(f"Disk Usage         : {disk.percent}%")
    print(f"Disk Used          : {round(disk.used / (1024**3),2)} GB")
    print(f"Disk Total         : {round(disk.total / (1024**3),2)} GB")

    print()

    if battery:

        print(f"Battery            : {battery.percent}%")

        if battery.power_plugged:
            print("Charging           : Yes")
        else:
            print("Charging           : No")

    else:

        print("Battery            : Not Available")

    print()

    print(f"System Boot Time   : {boot}")

    print()

    print("Refreshing every 2 seconds...")
    print("Press CTRL + C to Exit")

    time.sleep(2)
