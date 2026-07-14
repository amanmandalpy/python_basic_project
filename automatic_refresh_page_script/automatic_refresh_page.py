from selenium import webdriver
import time

website = input("Enter Website URL: ")
refresh_time = int(input("Refresh after how many seconds? "))

driver = webdriver.Chrome()
driver.get(website)

while True:
    time.sleep(refresh_time)
    driver.refresh()
    print("Page Refreshed")


# from selenium import webdriver
# import time
# from datetime import datetime

# # User Input
# website = input("Enter Website URL: ")
# refresh_time = int(input("Refresh every how many seconds? "))

# # Open Chrome
# driver = webdriver.Chrome()
# driver.get(website)

# refresh_count = 0

# print("\nWebsite Opened Successfully!")
# print("Press Ctrl + C to Stop.\n")

# try:
#     while True:

#         # Countdown
#         for i in range(refresh_time, 0, -1):
#             print(f"\rRefreshing in {i} seconds...", end="")
#             time.sleep(1)

#         driver.refresh()
#         refresh_count += 1

#         current_time = datetime.now().strftime("%H:%M:%S")

#         print(
#             f"\n[{current_time}] Page Refreshed Successfully | Total Refresh: {refresh_count}"
#         )

# except KeyboardInterrupt:
#     print("\n\nScript Stopped by User.")
#     driver.quit()
