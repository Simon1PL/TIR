import json
from math import cos
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from sunposition import sunpos
import random

s = 2  # rozmiar panela (m²)
direction = 180
tilt = 30
latitude = 50.049683
longitude = 19.944544


def calculate_g(direction, tilt, latitude, longitude, time):
    if time is None:
        time = datetime.utcnow()
    azimuth, zenith, _, _, _ = sunpos(time, [latitude], [longitude], 0)[0]

    factor = cos((zenith - tilt) * 0.017453)
    if factor < 0 or zenith > 90:
        factor = 0
    factor *= cos((azimuth - direction) * 0.017453)
    if factor < 0:
        factor = 0
    return 1000 * factor


class Panel:
    def __init__(self, name, current, voltage):
        self._name = name
        self.factor = 0
        self.current = current
        self.voltage = voltage
        #self.mqttc = mqtt.Client(name)
        #self.mqttc.connect("test.mosquitto.org", 1883, 60)

        print("Hello panel: " + self.name)

    @property
    def name(self):
        return self._name

    def send_data_to_server(self, data):
        self.mqttc.publish("data/from_panel/" + self._name, payload=json.dumps(data), qos=0, retain=False)

    def get_power_stats(self, g):
        random_losses = random.uniform(0.7, 0.8)
        I = g * self.current * random_losses / 1000
        V = self.voltage + g * random_losses / 500 - 1
        return I, V

    def calculate_data(self):
        now = datetime.now()
        g = calculate_g(direction, tilt, latitude, longitude, now)
        print(now, self.get_power_stats(g))
        i, v = self.get_power_stats(calculate_g(direction, tilt, latitude, longitude, now))
        data = {"panel_name": self.name, "I": i, "V": v, "G": g, "S": s, "Time": now.__str__()}
        return data

    # def getT(self):
    #     np.random.seed(19680801)
    #     y = np.random.normal(loc=55, scale=1.0, size=50)
    #     y = np.sin(y) * 5 + 50
    #     for i in range(30, 33):
    #         y[i] -= 10.0
    #     for i in range(10, 12):
    #         y[i] -= 10.0
    #     for i in range(45, 48):
    #         y[i] -= 10.0
    #     T = np.random.normal(loc=1.0, scale=0.05, size=200)
    #     for i in range(0, T.size):
    #         T[i] = T[i] * y[int(i / 4)]
    #
    #     return T


def myplot(T, V):
    x = np.arange(len(V))
    plt.plot(x, V, 'tab:blue', x, T, 'tab:red')
    plt.ylim(0, 5)
    plt.show()


def main():
    panel_first = Panel("1", 5, 80)  # Uwaga, name panelu musi byc unikalny, bo uzywamy go jako id clienta servera mqtt
    # T = panel_first.getT()
    # V = panel_first.getV(T)
    # I = panel_first.getI(V)
    I = []
    V = []
    # myplot(T, V, I)
    for k in range(24):
        for j in range(0, 60, 5):
            now = datetime(2021, 2, 14, k, j, 0)
            g = calculate_g(direction, tilt, latitude, longitude, now)
            print(now, panel_first.get_power_stats(g))
            i, v = panel_first.get_power_stats(calculate_g(direction, tilt, latitude, longitude, now))
            # panel_first.mqttc.publish("data/from_panel/" + panel_first.name,
            #                           str(i) + ',' + str(v) + ',' + str(g) + ',' + str(s))
            panel_first.send_data_to_server(
                {"panel_name": panel_first.name, "I": i, "V": v, "G": g, "S": s, "Time": now.__str__()})
            I.append(i)
            V.append(v)
    myplot(I, V)


if __name__ == '__main__':
    main()
