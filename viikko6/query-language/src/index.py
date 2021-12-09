from statistics import Statistics
from player_reader import PlayerReader
from query_builder import query_builder as default_query_builder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = default_query_builder

    matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasFewerThan(10, "goals").build()

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
