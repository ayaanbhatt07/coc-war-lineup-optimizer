"""
Clash of Clans - War Lineup Optimizer
-------------------------------------

This script helps Clash of Clans clan leaders optimize their war lineup
by ranking members using customizable weights for key stats.

Usage:
1. Get a Clash of Clans Developer API key:
   https://developer.clashofclans.com
2. Replace the placeholder API_KEY value below with your key.
3. Run the script:  python main.py
4. Enter your clan tag (with '#') and follow prompts.

Author: Your Name
GitHub: https://github.com/<your-username>/coc-war-lineup-optimizer
"""

import requests
import urllib.parse

# -------------------------------------
# CONFIGURATION
# -------------------------------------
# 👇 Replace this with your actual Clash of Clans API key.
#    (Keep your real key private — don't share publicly!)
API_KEY = "YOUR_API_KEY_HERE"

# -------------------------------------
# FUNCTIONS
# -------------------------------------
def get_clan_members(clan_tag):
    """Fetch clan members using the Clash of Clans API."""
    encoded_tag = urllib.parse.quote(clan_tag)
    api_url = f"https://cocproxy.royaleapi.dev/v1/clans/{encoded_tag}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("memberList", []), data.get("name", "Unknown Clan")
    else:
        print(f"Error fetching clan data: {response.status_code}")
        return [], "Unknown Clan"


def get_player_details(player_tag):
    """Fetch detailed player information."""
    encoded_tag = urllib.parse.quote(player_tag)
    url = f"https://cocproxy.royaleapi.dev/v1/players/{encoded_tag}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching player data for {player_tag}: {response.status_code}")
        return {}


def get_user_weights():
    """Ask user to rate importance of each stat."""
    print("\nRate the importance of each factor (0–10):")
    try:
        th_weight = int(input("Town Hall Level importance: "))
        donations_weight = int(input("Troops Donated importance: "))
        trophies_weight = int(input("Trophy Count importance: "))
        war_stars_weight = int(input("War Stars importance: "))
    except ValueError:
        print("Invalid input, defaulting all weights to 1.")
        return 1, 1, 1, 1

    return th_weight, donations_weight, trophies_weight, war_stars_weight


def best_war_lineup(members, war_size):
    """Compute the best war lineup based on weighted stats."""
    th_w, don_w, troph_w, war_w = get_user_weights()
    eligible = []

    for member in members:
        player = get_player_details(member["tag"])
        if player.get("warPreference", "out") == "in":
            member.update({
                "townHallLevel": player.get("townHallLevel", 0),
                "donations": member.get("donations", 0),
                "trophies": player.get("trophies", 0),
                "warStars": player.get("warStars", 0)
            })
            eligible.append(member)

    if not eligible:
        print("No members opted for war.")
        return []

    eligible.sort(key=lambda x: (
        x["townHallLevel"] * th_w +
        x["donations"] * don_w +
        x["trophies"] * troph_w +
        x["warStars"] * war_w
    ), reverse=True)

    return eligible[:war_size]


# -------------------------------------
# MAIN EXECUTION
# -------------------------------------
def main():
    print("=== Clash of Clans War Lineup Optimizer ===\n")
    clan_tag = input("Enter your clan tag (include #): ").strip()
    war_size = int(input("Enter war lineup size: "))

    members, clan_name = get_clan_members(clan_tag)
    if not members:
        print("Could not fetch clan members.")
        return

    lineup = best_war_lineup(members, war_size)
    print(f"\nBest War Lineup for {clan_name}:\n")

    if not lineup:
        print("No players selected for war.")
        return

    print("{:<20} {:<10} {:<10} {:<10} {:<10}".format(
        "Name", "TH", "Donations", "Trophies", "War Stars"))
    print("-" * 60)
    for player in lineup:
        print("{:<20} {:<10} {:<10} {:<10} {:<10}".format(
            player.get("name", "Unknown"),
            player.get("townHallLevel", "N/A"),
            player.get("donations", 0),
            player.get("trophies", 0),
            player.get("warStars", 0)
        ))


if __name__ == "__main__":
    main()
