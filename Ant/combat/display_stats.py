def display_stats(combat):

    health = combat.worker.char_stats.health
    endurance = combat.worker.char_stats.endurance

    print("""
    ______________________________________________
              CURRENT HEALTH AND ENDURANCE    
    """)

    print(f"          HEALTH: /{'-' * round(health * 0.1)}{(' ' * (10 - (round(health * 0.1))))}/ {health}%")
    print(f"       ENDURANCE: /{'-' * round(endurance * 0.1)}{(' ' * (10 - (round(endurance * 0.1))))}/ {endurance}%")

    print("""
    ______________________________________________

    """)