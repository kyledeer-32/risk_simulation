from ast import Break
import numpy as np

#for rng, need to generate uniform distribution for range of dice events (1, 6) because each event has an equal probability of occuring.

class Battle():
    def __init__(self, attackers, defenders):
        self.attackers = attackers - 1 #one attacker must always remain in reserve
        self.defenders = defenders
        self.starting_attackers = attackers
        self.starting_defenders = defenders
        self.attackers_lost = 0
        self.defenders_lost = 0
        self.battle_count = 0
        self.winner = "Battle Incomplete"

    def outcome(self):
        battle_finished = False
        while battle_finished == False:
            if self.attackers == 0:
                battle_finished = True
                self.winner = "Defender"
                break
            if self.defenders == 0:
                battle_finished = True
                self.winner = "Attacker"
                break

            if self.attackers >= 3:
                a = 3
            else:
                a = self.attackers
            
            if self.defenders >= 2:
                d = 2
            else:
                d = self.attackers
            
            self.rolls(a, d)

            self.battle_count += 1
        
        print(
        """
        ______________________________
        ======= Battle Summary =======

            ~~ Starting Armies ~~
         Attackers: {}   Defenders: {}

           ~~ Number of Battles ~~
                      {}
        
              ~~ Armies Lost ~~
         Attackers: {}   Defenders: {} 

            ~~ Armies Remaining ~~
         Attackers: {}   Defenders: {} 
        
                *** WINNER ***
                 {}
        ______________________________
        """.format(self.starting_attackers, self.starting_defenders,
        self.battle_count, self.attackers_lost, self.defenders_lost,
        self.attackers, self.defenders,
        self.winner)
        )
  
    def rolls(self, a_rolls, d_rolls):
        attacks = []
        defends = []

        for roll in range(a_rolls):
            attacks.append(np.random.randint(1,6))

        for roll in range(d_rolls):
            defends.append(np.random.randint(1,6))

        for fight in range(d_rolls):
            if attacks.count == 0:
                Break
            a = max(attacks)
            attacks.remove(max(attacks))

            d = max(defends)
            defends.remove(max(defends))

            if d >= a:
                self.attackers -= 1
                self.attackers_lost += 1
                print('Attacker Roll: {} loses to Defender Roll: {}'.format(a, d))
            else:
                self.defenders -= 1
                self.defenders_lost += 1
                print('Attacker Roll: {} beats Defender Roll: {}'.format(a, d))
