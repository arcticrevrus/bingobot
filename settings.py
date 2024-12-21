file = open("settings.cfg", "r")
for line in file:
    pair = line.split("=")
    setting_name = pair[0].strip(" ")
    match setting_name:
        case "discord_key":
            discord_key = pair[1].strip(" ")
        case _:
            continue

try:
    discord_key
except NameError:
    print("No discord key provided")
    exit()
