def generate_invitations(template, attendees):
    # 🔍 Vérifier que le template est une chaîne
    if not isinstance(template, str):
        print("ERROR: Invalid input - template must be a string.")
        return

    # 🔍 Vérifier que attendees est une liste de dictionnaires
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("ERROR: Invalid input - attendees must be a list of dictionaries.")
        return

    # 📭 Gérer un template vide
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # 📭 Gérer une liste d'invités vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 🧠 Remplacer les champs et créer les fichiers
    for index, attendee in enumerate(attendees, start=1):
        personalized = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            personalized = personalized.replace(f"{{{key}}}", str(value))

        # 💾 Écrire dans le fichier output_X.txt
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(personalized)
            print(f"✅ File '{filename}' created.")
        except Exception as e:
            print(f"❌ Failed to write '{filename}': {e}")
