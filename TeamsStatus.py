import websocket
import _thread
import time
import rel
import json
import requests

machine = "xxxxx:xxxx"
key = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
pi = "xxx.xxx.xxx.xxx:xxxx"


def on_message(ws, message):
    #print(message)
    msg_json=json.loads(message)
    isInMeeting = msg_json['meetingUpdate']['meetingState']['isInMeeting'] 
    print("isInMeeting:" + str(isInMeeting))
    if isInMeeting:
       requests.get("http://" + pi + "/leds?r=32&g=0&b=0&desc=Free")
    else:
        requests.get("http://" + pi + "/leds?r=0&g=32&b=0&desc=Busy")

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://" + machine + "?token=" + key + "&protocol-version=1.0.0&manufacturer=ABC&device=ABC&app=ABC&app-version=1.0",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    
    ws.send('{"apiVersion":"1.0.0","service":"query-meeting-state","action":"query-meeting-state","manufacturer":"Elgato","device":"StreamDeck","timestamp":' + str(time.time()) + '}')
    
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()