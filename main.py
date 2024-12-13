import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Load your Slack token and channel from environment variables
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

# Define the message you want to post
MESSAGE = os.getenv("SLACK_MESSAGE", "Hello from the Docker container!")

if not SLACK_TOKEN or not SLACK_CHANNEL:
    raise ValueError("SLACK_TOKEN and SLACK_CHANNEL environment variables must be set.")

# Create a Slack client
client = WebClient(token=SLACK_TOKEN)

try:
    # Post the message to the specified channel
    response = client.chat_postMessage(channel=SLACK_CHANNEL, text=MESSAGE)
    print(f"Message posted successfully: {response['message']['text']}")
except SlackApiError as e:
    print(f"Error posting message: {e.response['error']}")