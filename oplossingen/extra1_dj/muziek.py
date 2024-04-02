import winsound
import time


def speel_noot(frequentie, duur):
    # Speelt een enkele noot met de opgegeven frequentie en duur.
    if frequentie is None:
        time.sleep(duur / 1000)
    else:
        winsound.Beep(frequentie, duur)


def speel_melodie(noten):
    # Speelt een reeks van noten.
    for noot in noten:
        frequentie = noot[0]
        duur = noot[1]
        speel_noot(frequentie, duur)