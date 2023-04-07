lines = open("input", "r", encoding='utf-8').read().strip().split(', ')
# Anweisungen in eine Liste von Tupeln konvertieren
anweisungen = [('R' if i[0] == 'R' else 'L', int(i[1:])) for i in lines]
# Startposition und Startausrichtung
position = [0, 0]
ausrichtung = 0  # 0 = Norden, 1 = Osten, 2 = Süden, 3 = Westen

# Bereits besuchte Positionen
besucht = set()
besucht.add(tuple(position))

# Schleife durch die Anweisungen
for richtung, schritte in anweisungen:
    # Ausrichtung aktualisieren
    ausrichtung = (ausrichtung + (1 if richtung == 'R' else -1)) % 4
    # Schritte in x- und y-Richtung berechnen
    dx, dy = [(0, 1), (1, 0), (0, -1), (-1, 0)][ausrichtung]
    # Neue Position berechnen
    for _ in range(schritte):
        position[0] += dx
        position[1] += dy
        # Prüfen, ob die Position bereits besucht wurde
        if tuple(position) in besucht:
            # Manhattan-Entfernung berechnen und ausgeben
            print(abs(position[0]) + abs(position[1]))
            exit()
        # Position zu den bereits besuchten hinzufügen
        besucht.add(tuple(position))
