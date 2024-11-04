def ontcijfer(tekst, toegelaten_tekens):
    boodschap = ""
    for teken in tekst:  # Overloop alle tekens
        if teken in toegelaten_tekens:  # Controleer of het teken in de toegelaten tekens voorkomt
            boodschap += teken
    return boodschap
