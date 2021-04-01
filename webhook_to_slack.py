import requests
import os, json

SLACK_WEBHOOK = os.environ.get("SLACK_WEBHOOK")
def send_to_slack(data):
    requests.post(SLACK_WEBHOOK, data=json.dumps({"text":f"Helium Price is: ${data}"}))


if __name__ == "__main__":
    send_to_slack(10)