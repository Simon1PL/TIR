import json
import paho.mqtt.client as mqtt


class Client:
    def __init__(self, client_id):
        self.client_id = client_id
        self.mqttc = mqtt.Client(client_id)
        self.connected = False

    def is_connected(self):
        return self.connected

    def connect(self):
        print('connecting...')
        self.mqttc.connect("test.mosquitto.org", 1883, 60)
        # self.mqttc.loop_forever()
        print('cpnnected')
        self.connected = True

    def send_data(self, data):
        self.mqttc.publish("data/from_panel/" + self.client_id, payload=json.dumps(data), qos=0, retain=False)
