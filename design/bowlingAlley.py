from typing import List

class BowlingAlleySimulator():
    
    def __init__(self):
        self.game_logs = [[' ', ' '] for _ in range(9)] + [[' ', ' ', ' ']]
        self.running_score = [' ' for _ in range(10)]
        self.current_game = 1
    
    def printGame(self):
        for i in range(1, 11):
            if i == 10: print('  ' + 3*' ' + str(i)  + 4*' ' + '  ', end='')
            else: print('  ' + 2*' ' + str(i)  + 2*' ' + '  ', end='')
        print()
        
        for log in self.game_logs:
            print('| ' + ' | '.join(log) + ' |', end='')
        print()
        c=1
        for score in self.running_score:
            if c == 10: print('| ' + (9-len(score))*' ' + score + ' |', end='')
            else: print('| ' + (5-len(score))*' ' + score + ' |', end='')
            c+=1
        print()
    
    def simulate(self, bowl1=0, bowl2=0, bowl3=0):
        def _translate(pins):
            if pins == 0: return '-'
            if pins == 10: return 'X'
            return str(pins)
        
        score = bowl1 + bowl2 + bowl3
            
        if self.current_game == 10:
            # Special Case Considerations
            log = [' ', ' ', ' ']
            log[0] = _translate(bowl1)
            log[1] = _translate(bowl2)
            log[2] = _translate(bowl3)
            if bowl1 == 10: # Strike First
                score += 10
                if bowl2 == 10:
                    score += 10 if bowl3 != 10 else 20                
                elif bowl2 + bowl3 == 10:
                    log[2] = '/'
                    score += 5
            else:
                if bowl1 + bowl2 == 10: 
                    log[1] = '/'
                    score += 5
                else:
                    log[2] = ' '
        else:
            log = [' ', ' ']
            if bowl1 == 10: # Strike
                score += 10
                log[1] = _translate(bowl1)
            else:
                log[0] = _translate(bowl1)
                log[1] = _translate(bowl2)
                if score == 10: 
                    log[1] = '/'
                    score += 5
        
        self.game_logs[self.current_game-1] = log
        self.running_score[self.current_game-1] = str(score + int(self.running_score[self.current_game-2])) if self.current_game > 1 else str(score)
        self.current_game += 1        
        
class Player():
    def __init__(self, name: str):
        self.name = name
    
    def getName(self):
        return self.name
        
class Game():
    def __init__(self, players: List[Player]):
        self.players = players
        self.bowlingGames = [BowlingAlleySimulator() for _ in range(len(players))]
        self.turn = 0
    
    def play(self, bowl1=0, bowl2=0, bowl3=0):
        print(self.players[self.turn].getName())
        self.bowlingGames[self.turn].simulate(bowl1, bowl2, bowl3)
        self.bowlingGames[self.turn].printGame()
        self.turn += 1 % len(self.players)

class Testing():       
    def __init__(self):
        pass
    
    def execute(self):
        self.test1()
    
    def test1(self):
        game = Game([Player("Yash"), Player("Tan")])
        game.play(0, 10)
        game.play(0, 10)
        
if __name__ == '__main__':
    test = Testing()
    test.execute()

