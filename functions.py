import requests
import json

def slak_send_webhook(text, channel, **kw):

    data = {
        "channel": channel,
        "text": text
    }

    data.update(kw)

    response = requests.post(
        url = SLACK_WEBHOOL_INC,
        data = json.dumps(data),
        headers = {'content-type': 'application/json'}
    )

