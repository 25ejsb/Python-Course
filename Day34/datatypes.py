age: int
name: str
height: float
human: bool

# -> means its expected to return a specific type
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(19):
    print("You may pass")
else:
    print("You're going to jail")