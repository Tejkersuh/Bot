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
def lose_streak(streak):
    count_losses = 0
    for game in streak:
        if game["result"] == "Loss":
            count_losses += 1
        else:
            count_losses = 0
    return count_losses

streak = lose_streak(matches)

if(streak > 2):
    print("Zaczął się lossstreak, trzymaj gardę wysoko")
else:
    print("Nie ma lossstreaka, pozdro")