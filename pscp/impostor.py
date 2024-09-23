"""Impostor"""
import json
def spaceship():
    """Find left/alive member in the spaceship"""
    member = {}
    dead_member = {}
    while True:
        new_member = input()
        if new_member == "Start":
            break
        member.update(json.loads(new_member))
    while True:
        dead_person = input()
        if dead_person == "End":
            break
        dead_member.update({dead_person: member[dead_person]})
        member.pop(dead_person)
    impos_remain = list(member.values()).count("Impostor")
    print(f"{impos_remain} Impostor Remains")
    print("***Alive***")
    for key, value in sorted(member.items()):
        print(f"{key} : {value}")
    print("***Dead***")
    for key, value in sorted(dead_member.items()):
        print(f"{key} : {value}")
spaceship()
