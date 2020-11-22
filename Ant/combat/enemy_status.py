from time import sleep


def enemy_status(combat):
    health = combat.enemy.health
    print(" ")
    if health <= 25:
        print(f"{combat.enemy.display_name} looks like it's about to faint!")
        sleep(3)
    elif health <= 50:
        print(f"{combat.enemy.display_name} seems beat down, but it's still kicking!")
        sleep(3)
    elif health <= 75:
        print(f"{combat.enemy.display_name} looks a bit hurt!")
        sleep(3)
    else:
        pass
