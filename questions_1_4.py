# ras371@uw.edu
# Ryan Siu and Tyler Sverak
# 8 June 2019
# CSE 163 AC

# This file contains all the helper functions and main function answering
# question 1, "What makes a successful team?" and question 4,
# "How big (if any) of a factor is Home-Field advantage?"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

matches = pd.read_csv("matches.csv")
players = pd.read_csv("players.csv")
top30 = pd.read_csv("top30.csv")
tournaments = pd.read_csv("tournaments.csv")
top30Obj = {'Liquid': ['nitr0', 'NAF', 'EliGE', 'Stewie2K', 'Twistzz'],
            'Astralis': ['Xyp9x', 'dupreeh', 'gla1ve', 'device', 'Magisk'],
            'ENCE': ['allu', 'Aerial', 'xseveN', 'Aleksib', 'sergej'],
            'Vitality': ['NBK-', 'RpK', 'apEX', 'ALEX', 'ZywOo'],
            'FaZe': ['NEO', 'olofmeister', 'GuardiaN', 'NiKo', 'rain'],
            'Natus Vincere': ['Zeus', 'flamie', 's1mple', 'electronic',
                              'Edward'],
            'fnatic': ['Xizt', 'JW', 'twist', 'KRIMZ', 'Brollan'],
            'MIBR': ['FalleN', 'fer', 'coldzera', 'TACO', 'felps'],
            'NiP': ['f0rest', 'GeT_RiGhT', 'dennis', 'Lekr0', 'REZ'],
            'NRG': ['daps', 'tarik', 'Brehze', 'Ethan', 'CeRq'],
            'FURIA': ['arT', 'yuurih', 'VINI', 'KSCERATO', 'ableJ'],
            'Renegades': ['jks', 'AZR', 'jkaem', 'Gratisfaction', 'Liazz'],
            'G2': ['JaCkz', 'shox', 'kennyS', 'AmaNEk', 'Lucky'],
            'mousesports': ['karrigan', 'chrisJ', 'woxic', 'frozen', 'ropz'],
            'North': ['aizy', 'Kjaerbye', 'JUGi', 'gade', 'valde'],
            'AVANGAR': ['fitch', 'SANJI', 'buster', 'qikert', 'Jame'],
            'Valiance': ['huNter', 'LETN1', 'nexa', 'ottoNd', 'EspiranTo'],
            'Grayhound': ['Sico', 'dexter', 'erkaSt', 'malta', 'DickStacy'],
            'Windigo': ['bubble', 'v1c7oR', 'blocker', 'SHiPZ', 'poizon'],
            'Ghost': ['steel', 'freakazoid', 'koosta', 'WARDELL', 'neptune'],
            'OpTic': ['Snappi', 'MSL', 'k0nfig', 'niko', 'refrezh'],
            'BIG': ['gob b', 'tabseN', 'tiziaN', 'denis', 'XANTARES'],
            'Heroic': ['friberg', 'es3tag', 'NaToSaphiX', 'stavn', 'blameF'],
            'HellRaisers': ['ANGE1', 'oskar', 'loWel', 'ISSAA', 'nukkye'],
            'Cloud9': ['cajunb', 'RUSH', 'autimatic', 'vice', 'Golden'],
            'AGO': ['SZPERO', 'Furlan', 'GruBy', 'phr', 'kaper'],
            'Tricked': ['HUNDEN', 'Bubzkji', 'b0RUP', 'acoR', 'sjuush'],
            'MVP PK': ['zeff', 'XigN', 'HSK', 'xeta', 'stax'],
            'Sprout': ['syrsoN', 'Spiidi', 'mirbit', 'k1to', 'faveN'],
            'forZe': ['facecrack', 'almazer', 'FL1T', 'xsepower', 'Jerry']}

top30Players = top30Obj.values()
top30Teams = top30Obj.keys()

intl_teams = ['FaZe', 'mousesports', 'Valiance', 'HellRaisers']
dome_teams = ['Liquid', 'Astralis', 'ENCE', 'Vitality', 'Natus Vincere',
              'fnatic', 'MIBR', 'NiP', 'NRG', 'FURIA', 'Renegades', 'G2',
              'North', 'AVANGAR', 'Grayhound', 'Windigo', 'Ghost', 'OpTic',
              'BIG', 'Heroic', 'Cloud9', 'AGO', 'Tricked', 'MVP PK',
              'Sprout', 'forZe']

large_tourneys = ["FACEIT Major 2018",
                  'FACEIT Major 2018 Main Qualifier',
                  'ELEAGUE Major 2018',
                  'ELEAGUE Major 2018 Main Qualifier',
                  'IEM Katowice 2019 Main Qualifier',
                  'IEM Katowice 2019']

vowels = ["a", "e", "i", "o", "u"]


def get_current_lineups():
    """
    Returns a filtered DataFrame of player data that only includes data
    where a player is playing for the team they currently represent
    """
    out = []
    pf = players[players["team"].isin(top30Teams)]
    for index, row in pf.iterrows():
        # Make sure that we only use player data where a player is
        # playing for their current team
        if(row["name"] in top30Obj[row["team"]]):
            out.append(row)
    return pd.DataFrame(out)


current_lineups = get_current_lineups()


def main():

    plot_average_stat_per_team("kills")
    plot_average_stat_per_team("assists")
    plot_average_stat_per_team("deaths")
    plot_average_stat_per_team("adr")
    plot_average_stat_per_team("kast")
    plot_average_stat_per_team("hit_flashbangs")
    plot_average_stat_per_team("opening_kills")
    plot_average_stat_per_team("opening_deaths")
    plot_average_stat_per_team("headshots")

    plot_average_stat_total_per_team("clutches")

    plot_player_stats_dist_per_team("kills")
    plot_player_stats_dist_per_team("assists")
    plot_player_stats_dist_per_team("deaths")
    plot_player_stats_dist_per_team("adr")
    plot_player_stats_dist_per_team("kast")
    plot_player_stats_dist_per_team("hit_flashbangs")
    plot_player_stats_dist_per_team("opening_kills")
    plot_player_stats_dist_per_team("opening_deaths")

    plot_map_rate_per_team("Inferno")
    plot_map_rate_per_team("Mirage")
    plot_map_rate_per_team("Overpass")
    plot_map_rate_per_team("Train")
    plot_map_rate_per_team("Dust2")
    plot_map_rate_per_team("Nuke")

    compare_stats_intl_dom("kills")
    compare_stats_intl_dom("assists")
    compare_stats_intl_dom("deaths")
    compare_stats_intl_dom("adr")
    compare_stats_intl_dom("kast")
    compare_stats_intl_dom("assists")
    compare_stats_intl_dom("headshots")
    compare_stats_intl_dom("opening_kills")
    compare_stats_intl_dom("opening_deaths")
    compare_stats_intl_dom("hit_flashbangs")

    compare_stat_advantage_per_match("opening_kills")
    compare_stat_advantage_per_match("opening_deaths")
    compare_stat_advantage_per_match("adr")
    compare_stat_advantage_per_match("hit_flashbangs")
    compare_stat_advantage_per_match("kast")
    compare_stat_advantage_per_match("kills")
    compare_stat_advantage_per_match("assists")
    compare_stat_advantage_per_match("deaths")
    compare_stat_advantage_per_match("headshots")

    plot_victories_tournament("TYLOO", get_tournaments_by_location("China"))
    plot_victories_tournament("ENCE", get_tournaments_by_location("finland"))
    plot_victories_tournament("MIBR", get_tournaments_by_location("brazil"))
    plot_victories_tournament(
        "Renegades", ["IEM Sydney 2018", "IEM Sydney 2019"])
    plot_victories_tournament("Cloud9",
                              tour=["ELEAGUE Major 2018",
                                    "ELEAGUE Major 2018 Main Qualifier"],
                              spec=["StarSeries i-League Season 4",
                                    "IEM Katowice 2018",
                                    "WESG 2017 World Finals"], name="ELEAGUE")

    plot_country_representation()


def plot_average_stat_per_team(stat):
    """
    Plots a bar chart and regression line for a given stat average
    per team in the top 30 list
    """

    df = players.copy()

    # Ensure all our data is only top30 players
    df = df[df['team'].isin(top30["name"].unique())]

    # Edge case for KAST, must convert str 30% to float 30
    if stat == "kast":
        df["kast"] = df["kast"].apply(lambda x: float(x.strip("%")))

    # Groupby team stat averages
    df = df.groupby("team")[stat].mean()

    # Convert to DataFrame so we can merge with top30
    df = pd.DataFrame(df)
    df = df.merge(top30, left_on="team", right_on="name", how="outer")

    # Sort by ranking position
    df = df.sort_values(by="position")

    # Plotting
    fig, ax = plt.subplots()
    sns.barplot(data=df, x="name", y=stat, ax=ax)
    sns.regplot(data=df, x=np.arange(0, len(df["name"])), y=stat, ax=ax)
    ax.set_ylim(df[stat].min() - df[stat].mean()/30,
                df[stat].max() + df[stat].mean()/30)
    ax.set_title("Average " + stat + " Per Team")
    fig.set_size_inches(11.7, 8.27)
    plt.xticks(rotation=70)
    fig.savefig("stat_per_team/" + stat + ".png")


def plot_average_stat_total_per_team(stat):
    """
    Plots a bar chart and regression line for a given stat
    sum averaged over every match played for each top30 team
    """

    # Ensure that the team in question is a top 30 team
    d1 = matches[matches['team1'].isin(top30["name"].unique())]
    d2 = matches[matches['team2'].isin(top30["name"].unique())]

    # Group by average stat per match
    d1 = d1.groupby("team1")["team1_" + stat].mean()
    d2 = d2.groupby("team2")["team2_" + stat].mean()

    # Convert groupby series to DF for merge
    d1 = pd.DataFrame(d1)
    d2 = pd.DataFrame(d2)

    # Merge
    df = d1.merge(d2, left_on=d1.index, right_on=d2.index, how="inner")

    # Make New Column
    df["avg"] = (df["team1_" + stat] + df["team2_" + stat])/2

    # Rename merged column
    df = df.rename(columns={"key_0": "team"})

    # Merge with top30 so we can order the rows by ranking
    df = df.merge(top30, left_on="team", right_on="name", how="inner")

    # Order rows by ranking
    df = df.sort_values(by="position")

    # Plotting
    fig, ax = plt.subplots()
    sns.barplot(x="team", y="avg", data=df, ax=ax)
    sns.regplot(data=df, x=np.arange(
        0, len(df["team"])), y="avg", ax=ax)
    ax.set_ylim(df["avg"].min() - df["avg"].min()/5,
                df["avg"].max() + df["avg"].max()/8)
    ax.set_title("Average Total " + stat + " Per Match Per Team")
    fig.set_size_inches(11.7, 8.27)
    plt.xticks(rotation=70)
    fig.savefig("average_per_match/" + stat + ".png")


def plot_player_stats_dist_per_team(stat):
    """
    Plots a strip(dot) plot of every player on a team and their stat average
    over every match, with a pointplot illustrating probability distribution
    """
    pf = current_lineups.copy()

    # Edge case for KAST
    if stat == "kast":
        pf["kast"] = pf["kast"].apply(lambda x: float(x.strip("%")))

    # Group by average stat per player
    pf = pf.groupby("name")[stat].mean()

    # Creating a dataframe we will use to merge player stat avg with their
    # respective teams
    name_team = current_lineups.copy()

    # Remove duplicates since we only care about player and their team
    name_team = name_team.drop_duplicates(["name", "team"], keep="first")
    name_team = name_team[["name", "team"]]

    # Merge dataframes so we have player stat average and their team
    pf = pd.DataFrame(pf).merge(name_team, left_on="name",
                                right_on="name", how="inner")

    # Merge with top30 so we have ranking positions
    pf = pf.merge(top30, left_on="team", right_on="name")
    pf = pf.rename(columns={"name_x": "name"})

    # Sort by position
    pf = pf.sort_values(by="position")

    # Plotting
    fig, ax = plt.subplots()
    ax.set_ylim(pf[stat].min() - pf[stat].min()/5,
                pf[stat].max() + pf[stat].mean()/5)
    sns.stripplot(x="team", y=stat, data=pf, jitter=True, ax=ax, size=6)
    sns.pointplot(x="team", y=stat, data=pf,
                  color="black", dodge=True, join=False)
    ax.set_title("Top 30 " + stat + " Distribution")
    plt.xticks(rotation=60)
    fig.set_size_inches(20, 10)
    fig.savefig("stat_dist/" + stat + ".png")


def plot_map_rate_per_team(map):
    """
    Plots winrate on a given map for each team with a
    regression line over
    """
    m = matches.copy()

    # Only get matches where a top30 team is present
    m = m[m['team1'].isin(top30["name"].unique()) |
          m['team2'].isin(top30["name"].unique())]

    # These maps aren't in the competitive map pool anymore; matches on them
    # aren't reflective of current performance
    deprecated = (m["map"] != "Cobblestone") & (m["map"] != "Cache")

    # Get dataframes where we only have rows where a specific team won or lost
    won1 = m[(m["team1"] == m["winner"]) & deprecated]
    loss1 = m[(m["team1"] != m["winner"]) & deprecated]
    won2 = m[(m["team2"] == m["winner"]) & deprecated]
    loss2 = m[(m["team2"] != m["winner"]) & deprecated]

    # Group dataframe by team, map, and count the wins
    won1 = won1.groupby(["team1", "map"])["winner"].count()
    won2 = won2.groupby(["team2", "map"])["winner"].count()
    loss1 = loss1.groupby(["team1", "map"])["winner"].count()
    loss2 = loss2.groupby(["team2", "map"])["winner"].count()

    # Push team name and map into columns
    won1 = pd.DataFrame(won1).reset_index()
    won2 = pd.DataFrame(won2).reset_index()
    loss1 = pd.DataFrame(loss1).reset_index()
    loss2 = pd.DataFrame(loss2).reset_index()

    # Rename columns
    won1 = won1.rename(columns={"team1": "team", "winner": "won"})
    won2 = won2.rename(columns={"team2": "team", "winner": "won"})
    loss1 = loss1.rename(columns={"team1": "team", "winner": "lost"})
    loss2 = loss2.rename(columns={"team2": "team", "winner": "lost"})

    # merge the wins and losses of team1 and team2 to get totals
    wins = won1.merge(won2, left_on=["team", "map"], right_on=[
                      "team", "map"], how="outer")
    losses = loss1.merge(loss2, left_on=["team", "map"], right_on=[
                         "team", "map"], how="outer")

    # NaN should be 0, for 0 wins/losses
    wins = wins.fillna(0)
    losses = losses.fillna(0)

    # Aggregate wins and losses
    wins["wins"] = wins["won_x"] + wins["won_y"]
    losses["losses"] = losses["lost_x"] + losses["lost_y"]

    # remove useless information
    wins = wins[["team", "map", "wins"]]
    losses = losses[["team", "map", "losses"]]

    # Merge wins and losses
    data = wins.merge(losses, left_on=["team", "map"], right_on=[
                      "team", "map"], how="outer")
    data = data.fillna(0)

    # Create winrate column
    data["winrate"] = data["wins"] / (data["wins"] + data["losses"])

    # Merge win/loss data with top30 data to sort by position
    data = data.merge(top30, left_on="team",
                      right_on="name").sort_values(by="position")

    # Plotting
    fig, ax = plt.subplots(figsize=(15, 7), ncols=1)
    a = sns.barplot(x="team", y="winrate",
                    data=data[data["map"] == map], ax=ax)
    sns.regplot(data=data[data["map"] == map], x=np.arange(
        0, len(data[data["map"] == map])), y="winrate", ax=ax)
    a.set_xticklabels(a.get_xticklabels(), rotation=50)
    ax.set_title("Team Winrates: " + map)
    ax.set_ylim(0, 1)
    fig.savefig("map_winrate/" + map + ".png")


def compare_stats_intl_dom(stat):
    """
    Plots a bar graph comparing the top 4 international teams, the top 4
    single nationality teams, and the bottom 4 single nationality teams.
    (Of the top 30)
    """
    df = current_lineups.copy()

    # KAST edge case
    if stat == "kast":
        df["kast"] = df["kast"].apply(lambda x: float(x.strip("%")))

    # Splitting into 3 dataframes
    intl = df[df["team"].isin(intl_teams)]  # Top 4 international teams
    dome = df[df["team"].isin(dome_teams[:4])]  # Top 4 national teams
    dome_last = df[df["team"].isin(dome_teams[-4:])]  # Lowest 4 national teams

    # Grouping by avg of stat and coverting to dataframe
    intl = pd.DataFrame(intl.groupby("team")[stat].mean().reset_index())
    dome = pd.DataFrame(dome.groupby("team")[stat].mean().reset_index())
    dome_last = pd.DataFrame(dome_last.groupby("team")[
                             stat].mean().reset_index())

    # Adding team_type column to each dataframe
    intl["team_type"] = "International"
    dome["team_type"] = "Single Nationality (Top 4)"
    dome_last["team_type"] = "Single Nationality (Lowest 4)"

    # Combine all 3 dataframes
    stats = intl.append(dome).append(dome_last)

    # Plotting
    fig, ax = plt.subplots()
    ax.set_ylim(stats[stat].min() - stats[stat].mean()/5,
                stats[stat].max() + stats[stat].mean()/15)
    ax.set_title("Average " + stat + " by Team Type")
    fig.set_size_inches(15, 7)
    a = sns.barplot(x="team", y=stat, data=stats, hue="team_type", ax=ax)
    a.set_xticklabels(a.get_xticklabels(), rotation=30)
    fig.savefig("compare/" + stat + ".png")


def compare_stat_advantage_per_match(stat):
    # Get a copy of matches.csv with only the id and winner columns
    df = matches.copy()
    df = df[df["team1"].isin(top30["name"].unique()) |
            df["team2"].isin(top30["name"].unique())]
    df = df[["matchId", "winner"]]

    # Group by teams and matchId and sum up stats
    sum1 = players.groupby(["team", "matchId"])[stat].sum().reset_index()
    sum2 = sum1.copy()

    # The reason we have 2 sums is to ensure we get all the data, and avoid
    # duplicates
    sum1.columns = ["team1", "id", "team1_stat"]
    sum2.columns = ["team2", "id", "team2_stat"]

    # Merging sum1 and sum2 and removing duplicate matches
    sums = sum1.merge(sum2, left_on="id", right_on="id")
    sums = sums[sums["team1"] != sums["team2"]]
    sums = sums.drop_duplicates(subset="id", keep="first")

    # Merge in data from matches.csv so we know who won the match
    sums = sums.merge(df, left_on="id", right_on="matchId")

    won1 = sums[(sums["team1"] == sums["winner"]) & (
        sums["team1_stat"] > sums["team2_stat"])]
    loss1 = sums[(sums["team1"] != sums["winner"]) & (
        sums["team1_stat"] > sums["team2_stat"])]

    won2 = sums[(sums["team2"] == sums["winner"]) & (
        sums["team2_stat"] > sums["team1_stat"])]
    loss2 = sums[(sums["team2"] != sums["winner"]) & (
        sums["team2_stat"] > sums["team1_stat"])]

    # Group dataframe by team, map, and count the wins
    won1 = won1.groupby("team1")["winner"].count()
    won2 = won2.groupby("team2")["winner"].count()
    loss1 = loss1.groupby("team1")["winner"].count()
    loss2 = loss2.groupby("team2")["winner"].count()

    # Push team name into columns
    won1 = pd.DataFrame(won1).reset_index()
    won2 = pd.DataFrame(won2).reset_index()
    loss1 = pd.DataFrame(loss1).reset_index()
    loss2 = pd.DataFrame(loss2).reset_index()

    won1 = won1.rename(columns={"team1": "team", "winner": "won"})
    won2 = won2.rename(columns={"team2": "team", "winner": "won"})
    loss1 = loss1.rename(columns={"team1": "team", "winner": "lost"})
    loss2 = loss2.rename(columns={"team2": "team", "winner": "lost"})

    # merge the wins and losses of team1 and team2 to get totals
    wins = won1.merge(won2, left_on=["team"], right_on=["team"], how="outer")
    losses = loss1.merge(loss2, left_on=["team"], right_on=[
                         "team"], how="outer")
    wins = wins.fillna(0)
    losses = losses.fillna(0)

    # Aggregate win/loss data
    wins["wins"] = wins["won_x"] + wins["won_y"]
    losses["losses"] = losses["lost_x"] + losses["lost_y"]

    # Calculate winrates
    data = wins.merge(losses, left_on="team", right_on="team", how="outer")
    data["winrate"] = data["wins"] / (data["wins"] + data["losses"])

    # Merge with top30 for positional data
    data = data.merge(top30, left_on="team",
                      right_on="name").sort_values(by="position")

    # Plotting
    fig, ax = plt.subplots()
    ax.set_ylim(data["winrate"].min() - data["winrate"].mean()/7,
                data["winrate"].max() + data["winrate"].mean()/15)

    pre = "a" if stat[0] not in vowels else "an"
    ax.set_title("Team Winrate with " + pre + " " + stat + " Advantage")
    fig.set_size_inches(15, 7)
    a = sns.barplot(x="team", y="winrate", data=data, ax=ax)
    sns.regplot(data=data, x=np.arange(
        0, len(data["team"])), y="winrate", ax=ax)
    a.set_xticklabels(a.get_xticklabels(), rotation=45)
    fig.savefig("advantage_winrate/" + stat + ".png")


def get_tournaments_by_location(loc):
    """
    Takes a location name and returns a list of tournaments that took place
    at that location
    """
    return set(tournaments[tournaments[" location"].str.lower() == loc.lower()]
               ["name"].unique())


def plot_victories_tournament(team, tour, spec=None, name=None):
    """
    Takes a team name and a list of tournaments and plots that team's winrate
    at those tournaments versus their winrates at other tournaments per map. If
    spec if set not to None, the "away" matches will be those defined in spec
    as to all matches not in the tournament list
    """
    df = matches.copy()

    # These maps aren't played recently, matches on them aren't reflective of
    # current performance
    df = df[(df["map"] != "Cobblestone") & (df["map"] != "Cache")]

    # Ensure that we only look the specified team
    isTeam = (df["team1"] == team) | (df["team2"] == team)

    # Boolean series for whether or not the match was a win for the team
    winner = df["winner"] == team
    loser = df["winner"] != team

    # If spec is defined, we use spec as the "away" group
    if spec is None:
        at = df["tournament"].isin(tour)
        away = ~df["tournament"].isin(tour)
    else:
        at = df["tournament"].isin(tour)
        away = df["tournament"].isin(spec)

    # Mask and groupby to get counts of won and lost matches at home
    won_home = df[at & isTeam & winner]
    loss_home = df[at & isTeam & loser]
    won_home = (won_home.groupby("map")['winner'].count())
    loss_home = (loss_home.groupby("map")['winner'].count())

    # Mask and groupby to get counts of won and lost matches away from home
    won_away = df[away & isTeam & winner]
    loss_away = df[away & isTeam & loser]
    won_away = (won_away.groupby("map")['winner'].count())
    loss_away = (loss_away.groupby("map")['winner'].count())

    # Create subplots for plotting
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, figsize=(20, 12), ncols=2)
    if spec is None:
        ax1.set_title(team + ": At Home")
        ax2.set_title(team + ": Away From")
        ax3.set_title(team + ": Winrate At Home")
        ax4.set_title(team + ": Winrate Away From")
    else:
        ax1.set_title(team + ": At " + name)
        ax2.set_title(team + ": Away From " + name)
        ax3.set_title(team + ": Winrate At " + name)
        ax4.set_title(team + ": Winrate After " + name)

    # Plot win/loss per map at home
    total_home = pd.concat([won_home, loss_home], axis=1, sort=True)
    total_home.columns = ["won", "lost"]
    total_home.plot.bar(stacked=True, ax=ax1)

    # Plot winrate per map at home
    total_home = total_home.fillna(0)
    total_home["winrate"] = total_home["won"] / \
        (total_home["won"] + total_home["lost"])
    total_home = total_home["winrate"]
    total_home.plot.bar(ax=ax3, ylim=(0, 1), color="#43bc43")

    # Plot win/loss away from home
    total_away = pd.concat([won_away, loss_away], axis=1, sort=True)
    total_away.columns = ["won", "lost"]
    total_away.plot.bar(stacked=True, ax=ax2)

    # Plot winrate away from home
    total_away = total_away.fillna(0)
    total_away["winrate"] = total_away["won"] / \
        (total_away["won"] + total_away["lost"])
    total_away = total_away["winrate"]
    total_away.plot.bar(ax=ax4, ylim=(0, 1), color="#43bc43")

    plt.subplots_adjust(hspace=0.5)
    fig.savefig("tournament_winrates/" + team + ".png")


def plot_country_representation():
    """
    Plots bar graphs of number of players from each country in our entire
    dataset, top30 teams only, and at the large tournaments
    """

    # Get all player data, drops duplicates
    all_players = players.copy().drop_duplicates(subset="name", keep="first")
    # Groupy origin, count unique names (unique since there are no duplicates)
    all_players = all_players.groupby("origin")["name"].count()
    # Push name and origin into columns
    all_players = pd.DataFrame(all_players.reset_index())

    # Get all top30 player data, drop duplicates
    top30_players = current_lineups.drop_duplicates(
        subset="name", keep="first")
    # Groupy origin, count unique names (unique since there are no duplicates)
    top30_players = top30_players.groupby("origin")["name"].count()
    # Push name and origin into columns
    top30_players = pd.DataFrame(top30_players.reset_index())

    # Get all player data
    majors = players.copy()
    # Filter so only players that have attended Major Tournaments are present
    majors = majors[majors["tournament"].isin(large_tourneys)]
    # Drop duplicates
    majors = majors.drop_duplicates(subset="name", keep="first")
    # Groupby origin, count names
    majors = majors.groupby("origin")["name"].count()
    # Add name and origin back to columns
    majors = pd.DataFrame(majors.reset_index())

    # Sort values by count of player
    all_players = all_players.sort_values(by="name", ascending=False)
    top30_players = top30_players.sort_values(by="name", ascending=False)
    majors = majors.sort_values(by="name", ascending=False)

    # Renaming columns to better describe data
    top30_players = top30_players.rename(
        columns={"name": "Number of Players", "origin": "Country"})
    all_players = all_players.rename(
        columns={"name": "Number of Players", "origin": "Country"})
    majors = majors.rename(
        columns={"name": "Number of Players", "origin": "Country"})

    # Plotting
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(20, 20))
    a = sns.barplot(x="Country", y="Number of Players",
                    data=all_players, ax=ax1)
    b = sns.barplot(x="Country", y="Number of Players",
                    data=top30_players, ax=ax2)
    c = sns.barplot(x="Country", y="Number of Players", data=majors, ax=ax3)
    ax1.set_title("Country Representation: All Players")
    ax2.set_title("Country Representation: Top 30 Teams")
    ax3.set_title("Country Representation: Last 3 Major Tournaments")
    a.set_xticklabels(a.get_xticklabels(), rotation=90)
    b.set_xticklabels(b.get_xticklabels(), rotation=90)
    c.set_xticklabels(c.get_xticklabels(), rotation=90)
    plt.subplots_adjust(hspace=1)

    fig.savefig("country_rep/country_rep.png")


if __name__ == '__main__':
    main()
