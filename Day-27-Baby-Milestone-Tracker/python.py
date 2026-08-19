# Day 27: Baby Nephew Milestone & Celebration Script

def celebrate_nephew(name="Junior"):
    print("========================================")
    print("      CELEBRATING A SPECIAL DAY!        ")
    print("========================================")
    print(f"Alhamdulillah! Welcoming our baby nephew {name} to the world! 👶🎉\n")

    milestones = {
        0: "Born today! Welcome to the family.",
        1: "First smile and eye contact.",
        3: "Starting to roll over.",
        6: "First solid baby foods.",
        9: "Crawling around the house.",
        12: "First birthday and first steps! 🎂"
    }

    print("--- Nephew's First-Year Milestones Tracker ---")
    for month, milestone in milestones.items():
        if month == 0:
            print(f"[*] Day 1  : {milestone}")
        else:
            print(f"[*] Month {month:02d}: {milestone}")

    print("\nStatus: Best Chacha duty officially activated! ❤️")

if __name__ == "__main__":
    celebrate_nephew("Baby Nephew")