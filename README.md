# TIR
## Uruchamianie
1. Uruchomić server.py
2. Uruchomić device.py

Aby połączyć urządzenie z serwerem, należy kliknąć przycisk na urządzeniu.
Do jednego serwera można podłączyć wiele urządzeń, 
każdy uruchomiony skrypt device.py imituje jedno urządzenie.

## Pliki:
- sunposition.py - serwis zwracajacy dane na temat słońca.
Kąt padania promieni dla danych współrzędnych geograficznych i daty.

- Panel.py - klasa pojedynczego panelu słonecznego.

- device.py - Symulacja realnego urządzenia obsługującego panel.

Komunikacja pomiędzy serwerem, a klientem odbywa się przy użyciu protokołu MQTT.

- server.py - Server odbierający dane od paneli (napięcie i natężenie).

- client.py - Klasa, której używa urządzenie (device) do łączenia się z serwerem.

- diagrams.py - Skrypt rysujący diagramy z danych.

