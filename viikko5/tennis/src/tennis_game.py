class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.game_count = {
            "0": "Love",
            "1": "Fifteen",
            "2": "Thirty",
            "3": "Forty"
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
            score = self.win_or_advantage(minus_result) + " " + self.winning_player()

        else:
            score = self.other_situation()

        return score
    
    def tie_situation(self):
        if str(self.m_score1) not in self.game_count:
            return "Deuce"
        return self.game_count[str(self.m_score1)] + "-All"
        
    def win_or_advantage(self, minus_result):
        if abs(minus_result) >= 2:
            return "Win for"
        return "Advantage"
    
    def winning_player(self):
        if self.m_score1 > self.m_score2:
            return "player1"
        return "player2"
    
    def other_situation(self):
        return self.game_count[str(self.m_score1)] + "-" + self.game_count[str(self.m_score2)]
