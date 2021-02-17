from time import sleep
from VirtualCopernicusNG import TkCircuit
from datetime import datetime

configuration = {
    "name": "Panel",
    "sheet": "solar1.png",
    "width": 332,
    "height": 250,
    "leds": [
        {"x": 200, "y": 40, "name": "LED 1", "pin": 21}
    ],
    "buttons": [
        {"x": 242, "y": 146, "name": "Button 1", "pin": 11}
    ]
}
circuit = TkCircuit(configuration)
client_id = "1"

s = 2  # rozmiar panela (m²)
direction = 180
tilt = 30
latitude = 50.049683
longitude = 19.944544


@circuit.run
def main():
    from client import Client
    client = Client(client_id)

    from gpiozero import LED, Button
    led1 = LED(21)

    def button1_pressed():
        led1.on()
        client.connect()
        # for k in range(0, 24):
        #     for j in range(0, 60):
        #         now = datetime(2020, 6, 22, k, j, 0)
        #         if client.is_connected():
        #             print('connected')
        #             data = panel.calculate_data(now)
        #             client.send_data(data)

    button1 = Button(11)
    button1.when_pressed = button1_pressed

    from Panel import Panel
    panel = Panel("1", 5, 80)

    while True:
        if client.is_connected():
            print('connected')
            data = panel.calculate_data(None)
            client.send_data(data)
            sleep(3)
