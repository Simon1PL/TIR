import paho.mqtt.client as mqtt


class Machine:
    def __init__(self, name):
        self._name = name
        self.mqttc = mqtt.Client(name)
        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.start_data = []

    def do_work(self):
        print("work")
        data = self.start_data.pop()
        self.mqttc.publish("data/from_machine/1", data, 0, False)

    def load_data(self, command):
        self.start_data.extend(command)

    def on_message(self, msg):
        command = msg.payload.decode("utf-8")
        print("received: " + msg.topic + " " + command)
        if "startData" in msg.topic:
            self.load_data(command)
        else:
            print("Unavailable command: " + msg.topic)

    def on_connect(self, rc):
        print(self._name + " connected with result code " + str(rc))
        self._mqttc.subscribe("data/startData")


def main():
    machine1 = Machine("machine1")
    while len(machine1.start_data):
        machine1.do_work()


if __name__ == '__main__':
    main()
