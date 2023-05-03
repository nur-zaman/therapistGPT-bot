
# TherapistGPT-Bot

This project is a Discord bot that utilizes the power of OpenAI's ChatGPT model to simulate a conversation with a world-famous psychiatrist. The bot acts as the psychiatrist, providing professional advice and guidance based on the user's input.

## Prerequisites

To run the Discord bot, you will need the following:

- Python 3.7 or higher installed on your machine
- Discord API token
- OpenAI ChatGPT API token. [How?](https://github.com/aaam/revChatGPT)

## Installation

1. Clone this repository to your local machine or download the project files.

2. Create a virtual environment (optional but recommended) and activate it.

3. Install the required Python packages by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

4. Obtain the required tokens:

   - Discord API token: Create a new Discord application and generate a bot token. Visit the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application. Then, navigate to the "Bot" tab and click on "Add Bot" to generate the token.
   - OpenAI ChatGPT API token: Sign up for the OpenAI GPT-3 API and obtain your API token.

5. Set up environment variables:

   - Rename the `.env.example` file to `.env`.
   - Open the `.env` file and replace the values of `CHATGPT_TOKEN` and `DISCORD_TOKEN` with your respective tokens obtained in the previous step.

## Usage

1. Run the bot:

   ```bash
   python bot.py
   ```

2. Invite the bot to your Discord server:

   - Visit the [Discord Developer Portal](https://discord.com/developers/applications) and select your application.
   - Navigate to the "OAuth2" tab.
   - In the "Scopes" section, select "bot".
   - In the "Bot Permissions" section, choose the necessary permissions based on your requirements (e.g., read messages, send messages, mention everyone).
   - Copy the generated OAuth2 URL and open it in your web browser.
   - Select the server where you want to add the bot and authorize the bot.

3. Interact with the bot:

   - Once the bot is running and added to your Discord server, you can start a conversation by sending a message to the bot.
   - The bot will respond to your messages as a psychiatrist, providing advice and guidance based on the conversation prompt and your responses.
   - Remember that the bot will pretend to be a real person, so it will ask questions, and you should answer them honestly.


## Acknowledgements

This project utilizes the following technologies and libraries:

- [Discord.py](https://discordpy.readthedocs.io/) - A Python wrapper for the Discord API, providing easy integration of Discord functionality into the bot.
- [OpenAI API](https://platform.openai.com/) - The powerful language model used to simulate the conversation with the psychiatrist.

## Disclaimer

Please note that this Discord bot is purely for educational and entertainment purposes. The bot's responses should not be considered as a substitute for professional therapy, psychiatric advice, or medical treatment.

- The bot is an AI language model and does not have the ability to diagnose or provide personalized treatment plans.
- The bot's responses are generated based on patterns and information available on the internet, and they may not always be accurate, up-to-date, or applicable to your specific situation.
- The bot cannot provide real-time feedback, assess non-verbal cues, or understand complex emotions like a human therapist would.

If you are experiencing mental health issues or have concerns about your well-being, it is important to consult a qualified mental health professional or healthcare provider. They can provide personalized and evidence-based support tailored to your specific needs.

By using this Discord bot, you acknowledge and understand that:

- The bot's responses are not a substitute for professional advice or treatment.
- The bot's responses may not always be accurate or suitable for your situation.
- The developers and maintainers of this bot are not liable for any consequences or damages arising from the use of the bot.

If you are in crisis or experiencing a medical emergency, please contact your local emergency services or a helpline immediately.

Remember to prioritize your well-being and seek appropriate professional help when needed.