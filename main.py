import json

def handler(event, context):
    return {
        "body":json.dumps({
            "version":"1"
        })
    }