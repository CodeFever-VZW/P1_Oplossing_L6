def ontcijfer(tekst, toegelaten_tekens):
    boodschap = ""
    for letter in tekst: # Overloop alle letters
        if letter in toegelaten_tekens: # Controleer of de letter in de toegelaten tekens voorkomt
            boodschap += letter
    return boodschap