import json

with open("data.json", "r") as file:
    matches = json.load(file)

def lose_streak(streak): #funkcja obliczajaca loss streak
    count_losses = 0
    for game in streak:
        if game["result"].capitalize() == "Loss":
            count_losses += 1
        else:
            count_losses = 0
    return count_losses

def stats(kda): #funkcja obliczajaca kda
    k = 0
    d = 0
    a = 0
    for game in kda:
        k += game["stats"]["kills"]
        d += game["stats"]["deaths"]
        a += game["stats"]["assists"]
    if d == 0:
        return k + a
    else:
        return(k + a) / d

def count(ammount): #funkcja liczaca ilosc gier
   game_ammount = len(ammount)
   return game_ammount

def get_champs(data): #funckja sprawdzajaca rozne postacie
    diffrent_champs = []
    for game in data:
        diffrent_champs.append(game["champion_name"])
    unique_champs = set(diffrent_champs)
    return ", ".join(unique_champs)

action =  {
    "KDA": stats,
    "STREAK": lose_streak,
    "COUNT": count,
    "CHAMPIONS": get_champs
} 
while True:
    choose = input("Podaj co chcesz zrobić (KDA/STREAK/COUNT/CHAMPIONS)")
    choose = choose.upper()
    if choose in action: #if sprawdzjacy wybor
        actionchoose = action[choose]
        result = actionchoose(matches)
        break
    else:
        print("Nie ma takiej opcji")

if choose == "KDA": #if sprawdzajcy czy wybor to KDA
    ratio = result
    print("Twoje KDA to", round(ratio, 2))

if choose == "STREAK": #if sprawdzjacy czy wybor to STREAK
    streak = result

    if(streak > 2):
        print("Zaczął się lossstreak, trzymaj gardę wysoko")
    else:
        print("Nie ma losestreaka, pozdro")
    
if choose == "COUNT": #if sprawdzajacy czy wybor to COUNT
    total_games = result
    print("Zagrałeś", total_games, "gier")

if choose == "CHAMPIONS": #if sprawdzajacy czy wybor to CHAMPIONS
    champion = result
    print("Grasz postaciami:", result)
