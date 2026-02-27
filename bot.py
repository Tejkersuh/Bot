import json

with open("data.json", "r") as file:
    data = json.load(file)
    matches = data["matches"]
    ranking = data["player_ranking"]

def lose_streak(streak): #funkcja obliczajaca loss streak
    count_losses = 0
    for game in streak:
        if game["result"].capitalize() == "Loss":
            count_losses += 1
        else:
            count_losses = 0
    if(count_losses > 2):
         print("Zaczął się lossstreak, trzymaj gardę wysoko")
    else:
        print("Nie ma losestreaka, pozdro")

def stats(kda): #funkcja obliczajaca kda
    k = 0
    d = 0
    a = 0
    for game in kda:
        k += game["stats"]["kills"]
        d += game["stats"]["deaths"]
        a += game["stats"]["assists"]
    if d == 0:
        print("Twoje KDA to:", k+a)
    else:
        print("Twoje KDA to:", (k+a)/d)

def count(ammount): #funkcja liczaca ilosc gier
   game_ammount = len(ammount)
   return len(ammount)

def get_champs(data): #funckja sprawdzajaca rozne postacie
    diffrent_champs = []
    for game in data:
        diffrent_champs.append(game["champion_name"])
    unique_champs = set(diffrent_champs)
    print("Grasz postaciami:", ", " .join(unique_champs))

def total_dmg(dmg): #funckja obliczajaca calkowity damage 
    added_dmg = 0
    for game in dmg:
       added_dmg += game["stats"]["damage_delt"]
    return added_dmg

def average_dmg(dmg): #funkcja obliczajaca sredni damage
    if not dmg:
        return 0
    print("Średnia twoich obrażeń to:", (round(total_dmg(dmg) / count(dmg))))

def most_played(played): #funkcja wyswietaljaca postac ktora zagrano najwiecej
    counts = {}
    for game in played:
        name = game["champion_name"]
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    if not counts:
        print("Brak gier")
    else:
        print("Najwięcej zagrałeś:", max(counts, key = counts.get))

def player_ranking(ranking): #funkcja wyswietalaca 5 najlepszych osob z rankingu
    for player in ranking[0:5]:
        name = player["nickname"]
        wr = player["winratio"]
        place = player["place"]
        print("Nr.", place, "ma", wr ,"% winratio")



action =  { #mozliwe akcje
    "KDA": stats,
    "STREAK": lose_streak,
    "COUNT": count,
    "CHAMPIONS": get_champs,
    "TOTALDMG": total_dmg,
    "AVERAGEDMG": average_dmg,
    "MOSTPLAYED": most_played,
    "RANKING": player_ranking
} 
data_map = { #mapa przypisywania akcji
    "KDA": matches,
    "STREAK": matches,
    "COUNT": matches,
    "CHAMPIONS": matches,
    "TOTALDMG": matches,
    "AVERAGEDMG": matches,
    "MOSTPLAYED": matches,
    "RANKING": ranking
}


while True: #petla wyboru opcji
    choose = input("Podaj co chcesz zrobić (KDA/STREAK/COUNT/CHAMPIONS/TOTALDMG/AVERAGEDMG/MOSTPLAYED/RANKING)")
    choose = choose.upper()
    if choose in action: #if sprawdzjacy wybor
        actionchoose = action[choose]
        payload = data_map[choose]
        result = actionchoose(payload)
        break
    else:
        print("Nie ma takiej opcji")


if choose == "COUNT":
    allgames = result
    print("Zagrałeś", allgames, "gier")

if choose == "TOTALDMG":
    totaldmg = result
    print("Twój łączny damage to", totaldmg)