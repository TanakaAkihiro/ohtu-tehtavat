class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.tie_game = {
            "0": "Love-All",
            "1": "Fifteen-All",
            "2": "Thirty-All",
            "3": "Forty-All"
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            score = self.tie_situation()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2
            score = self.after_four_points(minus_result)

        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
    
    def tie_situation(self):
        if str(self.m_score1) not in self.tie_game:
            return "Deuce"
        return self.tie_game[str(self.m_score1)]
    
    def after_four_points(self, minus_result):
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"