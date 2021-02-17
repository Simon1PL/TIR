# TIR
## Uruchamianie
1. odaplic server.py
2. odpalic Panel.py

## Pliki:
- sunposition.py - serwis zwracajacy dane na temat słońca.
Kąt padania promieni dla danych współrzędnych geograficznych i daty.

- inverter.py - 

- Panel.py - klasa pojedynczego panelu słonecznego.
W mainie odpalamy panele skrypty emitujące działanie paneli słonecznych.
    - send_data_to_server(data) - metoda panelu przyjmująca obiekt z danymi dla servera
    
- server.py - server odbierający dane od paneli (napięcie i natężenie).
TO DO: rysowanie wykresów otrzymanych danych.
    - load_panel_data(data) - funkcja przyjmująca dane od panelu. W niej napisać co robić z danymi.