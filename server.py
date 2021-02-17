import json
import paho.mqtt.client as mqtt


def load_panel_data(data):
    for k in range(len(data['I'])):
        print(data['I'][k], data['V'][k])
    print("Panel name: " + data["panel_name"])


def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    print("received: " + msg.topic + " " + data)
    if "from_panel" in msg.topic:
        load_panel_data(json.loads(data))
    else:
        print("Unavailable command: " + msg.topic)


def on_connect(client, userdata, flags, rc):
    print("server started")
    mqttc.subscribe("data/from_panel/#")   # odbieranie wiadomosci od paneli


mqttc = mqtt.Client("server")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect("test.mosquitto.org", 1883, 60)

mqttc.loop_forever()
