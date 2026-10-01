from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd
import time


# =========================================
# CHROME SETTINGS
# =========================================

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--use-fake-ui-for-media-stream")


# =========================================
# START CHROME
# =========================================

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)


# =========================================
# OPEN INDEX.HTML
# =========================================

website = f"file:///{getcwd()}\\index.html"

driver.get(website)


# =========================================
# INPUT FILE
# =========================================

rec_file = f"{getcwd()}\\input.txt"


# =========================================
# CONTINUOUS LISTENING
# =========================================

def listen():

    try:

        start_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, "startButton")
            )
        )

        # Start listening ONCE
        start_button.click()

        print("================================")
        print("       BHARATH AI")
        print("================================")
        print("Continuous listening started...")
        print("Speak normally.")
        print("Press CTRL+C to stop.")
        print("================================")

        last_text = ""

        while True:

            try:

                output_element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (By.ID, "output")
                    )
                )

                current_text = output_element.text.strip()

                # New speech detected
                if current_text and current_text != last_text:

                    last_text = current_text

                    print("\nYou:", current_text)

                    # Save latest speech
                    with open(
                        rec_file,
                        "w",
                        encoding="utf-8"
                    ) as file:

                        file.write(current_text)

                    # Wait for the browser recognition
                    # to finish this sentence
                    time.sleep(0.5)

                    # Automatically start listening again
                    try:

                        start_button.click()

                        print("Listening...")

                    except Exception:
                        pass

                time.sleep(0.2)

            except Exception as error:

                print("Listening error:", error)

                time.sleep(1)

                # Try to start listening again
                try:
                    start_button.click()
                except Exception:
                    pass

    except KeyboardInterrupt:

        print("\nBharath AI stopped.")

    except Exception as error:

        print("Error:", error)


# =========================================
# RUN
# =========================================

listen()


# =========================================
# CLOSE CHROME
# =========================================

driver.quit()