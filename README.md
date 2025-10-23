# Clash of Clans – War Lineup Optimizer ⚔️

A Python-based tool designed for **Clash of Clans clan leaders** to optimize war lineups using real-time data from the official **Clash of Clans API**.  
This script ranks players based on customizable weights (Town Hall level, donations, trophies, and war stars) to create the most competitive lineup for any war size.

---

## 🚀 Features

- **Real-time Data:** Fetches live clan and player data from the Clash of Clans API.
- **Customizable Strategy:** Assign custom weightages for different stats.
- **Automatic Ranking:** Generates and displays a ranked war lineup.
- **Clean Output:** Presents results in a readable tabular format.
- **Dynamic Input:** Works with any clan tag entered by the user.
- **API Proxy Integration:** Uses RoyaleAPI’s proxy to stabilize IP issues on Colab.

---

## 🧩 Tech Overview

| Concept | Description |
|----------|-------------|
| **API Interaction** | Fetches and parses JSON data from Clash of Clans API endpoints. |
| **Data Processing** | Aggregates player stats and computes weighted rankings. |
| **User Input Handling** | Accepts clan tag and metric weights dynamically. |
| **Rate Limit Management** | Uses RoyaleAPI proxy to bypass IP-based key invalidation on Google Colab. |
| **Output Formatting** | Displays ranked player data in clean tabular format. |

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/coc-war-lineup-optimizer.git
cd coc-war-lineup-optimizer
````

### 2. Install Dependencies

Make sure you have Python 3.x installed. Then run:

```bash
pip install requests
```

---

## 🔑 Getting Your Clash of Clans API Key

1. Go to the official [Clash of Clans Developer Portal](https://developer.clashofclans.com/#/).
2. Sign in with your Supercell ID.
3. Click **“My Account” → “Create New Key.”**
4. For **name and description**, enter something like:

   ```
   Name: CoC War Lineup Optimizer
   Description: Local testing for Clash War Lineup project
   ```
5. For **allowed IP addresses**, enter your current IP or use RoyaleAPI (see below for static IP setup).
6. Copy the **API Key** generated — it looks like a long string of characters.

---

## 🛰 Using RoyaleAPI for a Static IP (Recommended)

When using Google Colab, your IP address changes frequently, which can invalidate your Clash API key.
To fix this, you can route all API requests through **RoyaleAPI’s public proxy** which uses a **stable IP**.

### Steps:

1. Visit the RoyaleAPI proxy documentation:
   🔗 [https://docs.royaleapi.com/proxy.html#community-support](https://docs.royaleapi.com/proxy.html#community-support)
2. Replace your API URLs:

   * Instead of

     ```
     https://api.clashofclans.com/v1/clans/
     ```

     use

     ```
     https://cocproxy.royaleapi.dev/v1/clans/
     ```
3. You can use the same Bearer Token (your Clash API key) with the proxy.
   RoyaleAPI will handle the IP routing for you, keeping your key valid even when Colab changes IPs.

✅ **Example:**

```python
API_URL = f"https://cocproxy.royaleapi.dev/v1/clans/{ENCODED_CLAN_TAG}"
player_url = f"https://cocproxy.royaleapi.dev/v1/players/{encoded_tag}"
```

---

## 🧠 How It Works

### Flow

1. The user inputs a clan tag (e.g., `#2YPYG2LRQ`).
2. The program fetches clan members from the Clash of Clans API.
3. For each player, additional stats like Town Hall level and war preference are retrieved.
4. The user assigns weights (1–10) to each metric:

   * Town Hall Level
   * Donations
   * Trophies
   * War Stars
5. The program ranks all players “in war” and selects the top N based on the war size.

---

## 🖥 Example Output

```
Enter Clan Tag (with #): #2PP
Enter the number of players for the war lineup: 15
Rate the importance of each factor (out of 10):
How important is Town Hall Level?: 10
How important are Troops Donated?: 5
How important is Trophy Count?: 3
How important are War Stars?: 7

Best War Lineup for Elite Warriors:
Name                 TH         Donations  Trophies   War Stars
------------------------------------------------------------
A                    15         600        5200       150
B                    14         450        4800       110
... and so on ...
```

---

## 🧩 Challenges Faced

* **War Preference Unavailable:** Required a separate API call for each player.
* **Rate Limits:** Handled 30–40 requests/sec limit efficiently.
* **Dynamic IP Issues:** Solved via RoyaleAPI’s proxy integration.
* **Key Regeneration:** Eliminated need to recreate API keys every session on Colab.

---

## ✅ Status

✔️ Project completed and fully functional
🚧 Future updates may include:

* GUI or web dashboard
* Weighted auto-calibration based on past war performance
* Export to CSV or Excel

---

## 👤 Author

**Ayaan Bhatt**

University of Michigan

https://www.linkedin.com/in/ayaan-bhatt/

```
