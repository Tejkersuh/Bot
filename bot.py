matches = [
{
    "champion_name": "Gwen",
    "result": "Win",
    "stats": {"damage_delt": 16823, "kills": 12, "deaths": 2, "assists": 15}
  
},
{
    "champion_name": "Gwen",
    "result": "Loss",
    "stats": {"damage_delt": 21765, "kills": 8, "deaths": 3, "assists": 8}
  
},
{
    "champion_name": "Gwen",
    "result": "Loss",
    "stats": {"damage_delt": 12644, "kills": 6, "deaths": 8, "assists": 3}
  
}

]

choose = input("Podaj co chcesz zrobić (KDA/STREAK/COUNT)")
choose = choose.upper()

def lose_streak(streak): #funkcja obliczajaca loss streak
    count_losses = 0
    for game in streak:
        if game["result"] == "Loss":
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
    killratio = (k + a) / d
    return killratio

def count(ammount): #funkcja liczaca ilosc gier
   game_ammount = len(ammount)
   return game_ammount

action =  {
    "KDA": stats,
    "STREAK": lose_streak,
    "COUNT": count
} 

if choose in action: #if sprawdzjacy wybor
    actionchoose = action[choose]
    result = actionchoose(matches)

if choose == "KDA": #if sprawdzajcy czy wybor to KDA
    ratio = result
    print("Twoje KDA to", ratio)

if choose == "STREAK": #if sprawdzjacy czy wybor to STREAK
    streak = result

    if(streak > 2):
        print("Zaczął się lossstreak, trzymaj gardę wysoko")
    else:
        print("Nie ma losestreaka, pozdro")
    
if choose == "COUNT": #if sprawdzajacy czy wybor to COUNT
    total_games = result
    print("Zagrałeś", total_games, "gier")