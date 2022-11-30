from player import Player

class StubPlayerReader:
    def __init__(self):
        self._file = "src/tests/players.txt"

    def get_players(self):
        players_file = open(self._file, "r")
        players = []

        for line in players_file:
            parts = line.split(";")

            if len(parts) > 3:
                player = Player(
                    parts[0].strip(),
                    parts[1].strip(),
                    int(parts[3].strip()),
                    int(parts[4].strip())
                )

                players.append(player)

        return players
