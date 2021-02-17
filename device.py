from time import sleep
from VirtualCopernicusNG import TkCircuit
configuration = {
    "name": "Panel",
    "sheet": "sheet_smarthouse.png",
    "width": 332,
    "height": 300,
    "leds": [
        {"x": 112, "y": 70, "name": "LED 1", "pin": 21}
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
        print('pressed')
        client.connect()
        led1.on()

    button1 = Button(11)
    button1.when_pressed = button1_pressed

    from Panel import Panel
    panel = Panel("1", 5, 80)

    while True:
        pass

    while True:
        if client.is_connected():
            data = panel.calculate_data()
            client.send_data(data)
            sleep(3)