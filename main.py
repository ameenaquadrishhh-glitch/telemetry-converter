import json
from datetime import datetime


def convertFromFormat1(jsonObject):
    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": int(
            datetime.strptime(
                jsonObject["timestamp"],
                "%Y-%m-%dT%H:%M:%S.%fZ"
            ).timestamp() * 1000
        ),
        "data": {
            "temperature": jsonObject["data"]["temperature"],
            "humidity": jsonObject["data"]["humidity"]
        }
    }


def convertFromFormat2(jsonObject):
    return {
        "deviceID": jsonObject["id"],
        "deviceType": jsonObject["type"],
        "timestamp": int(
            datetime.strptime(
                jsonObject["timestamp"],
                "%d-%m-%Y %H:%M:%S"
            ).timestamp() * 1000
        ),
        "data": {
            "temperature": jsonObject["temp"],
            "humidity": jsonObject["humid"]
        }
    }


# ==============================
# DO NOT MODIFY BELOW THIS LINE
# ==============================

def runTests():
    with open("data-1.json") as f:
        format1 = json.load(f)

    with open("data-2.json") as f:
        format2 = json.load(f)

    with open("data-result.json") as f:
        expected = json.load(f)

    result1 = convertFromFormat1(format1)
    result2 = convertFromFormat2(format2)

    assert result1 == expected, "Format 1 conversion failed"
    assert result2 == expected, "Format 2 conversion failed"

    print("All tests passed!")


if __name__ == "__main__":
    runTests()
