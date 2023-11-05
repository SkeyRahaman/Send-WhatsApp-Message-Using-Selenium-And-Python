# WhatsApp Message Sender with Selenium

This Python script allows you to send messages on WhatsApp using the Selenium web automation framework. It opens the WhatsApp web, logs in, and sends a message to a specified contact. You can also send multiple messages if desired.

## Prerequisites

Before using this script, make sure you have the following installed on your system:

- [Python](https://www.python.org/) (version 3.x)
- [Selenium](https://pypi.org/project/selenium/)
- [Chrome WebDriver](https://chromedriver.chromium.org/)

You can install the required Python libraries using pip:

```bash
pip install selenium
```

Download the appropriate Chrome WebDriver for your Chrome browser version and ensure it's in your system's PATH.

## Usage

1. Clone this repository or download the script to your local machine.

2. Open the script in a text editor or IDE and update the following variables as needed:
   - `name`: The name of the contact you want to send messages to.
   - You can customize the `message()` function to format your message as desired.

3. Run the script using Python:

```bash
python whatsapp_message_sender.py
```

4. Follow the instructions in the script:
   - You will need to scan the QR code to log in to WhatsApp Web.
   - Enter "Y" if you want to send 10 more messages (optional).

## Disclaimer

This script is provided for educational and demonstration purposes only. Use it responsibly and in accordance with WhatsApp's terms of service. Automated messaging can potentially violate WhatsApp's policies, so be cautious about excessive use.

## Credits

This script was created by MD SHAKIB MONDAL on  14 Feb,2022.

Please feel free to reach out if you have any questions or need assistance using this script.
