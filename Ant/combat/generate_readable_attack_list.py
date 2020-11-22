def generate_readable_attack_list(combat):
    print("""
            Available Attacks
==============================================
  Name            Description                                
    
    """)


    for attack in combat.worker.char_stats.attacks:
        attack_info = f"  {attack.name} ---------- {attack.description}"
        print(attack_info)

    print("""
    
==============================================
    
    """)
