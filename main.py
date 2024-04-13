import random
import os, time

print("DOS-DOS, Python")
print("")

print("""Which game do you want to play? 
      TRPSG(The Rock Paper Scissors Game)
      TRPG(TextRPG)
      COC(Coin Clicker)
      FLAB(Flappy bird)
      CRR(Crossy Road)""")
game = input("> ")

if game == 'TRSPG':
    os.system('cls' if os.name == 'nt' else 'clear')

    i = "" # i is used for alignment
    againY = "Yes" # It's used for score saving
    AIScore = 0 # For Player 2 Score
    YourScore = 0 # Your Score
    Points = 0 # Points
    PowerUps = [] # PowerUps Have
    Settings = "N"

    while True:
        # Title:
        def menu():
            if againY == 'No' or againY == 'Yes':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                print(f"{i: ^70} The Rock, Paper, Scrissors Game!")
                print("")
                menu = input("""▶️  S to Start, 
                ❌ Q to quit, 
                👍 P to PowerUps
                🔄 SS to Settings: """)
                os.system('cls' if os.name == 'nt' else 'clear')
        menu()
        if menu == 'S':
            AIScore = 0
            YourScore = 0
            if againY == 'Yes':
                def main_elements():
                    AiChoose = random.randint(1, 3)
                    # MAIN Elements:
                        # Choose:
                    print("""What do you want to choose?
                        🪨 (Rock), 🧻(Paper), ✂️ (Scissors)""")
                    # Chooses
                    if 'CHEAT PAPER' in PowerUps:
                        choose = input("Choose as R(Rock) P(Paper) S(Scissors) CP(Cheat Paper)< ")
                    elif 'PLAYER 2 SCORE' in PowerUps:
                        choose = input("Choose as R(Rock) P(Paper) S(Scissors) P2S(Player 2 Score)< ")
                    elif 'INVINCIBE' in PowerUps:
                        choose = input("Choose as R(Rock) P(Paper) S(Scissors) IN(Invincibe)< ")
                    else:
                        choose = input("Choose as R(Rock) P(Paper) S(Scissors)< ")
                    global AIScore   
                    global YourScore

                    time.sleep(0.5)
                    if choose == 'CP':
                        print("Rock Paper Scissors Cheat!")
                        
                    elif choose == 'P2S':
                        print("Rock Paper Scissors -1!")
                    else:
                        print("Rock Paper Scissors Shoot!")
                    print("")

                    time.sleep(0.3)
                    if choose == 'CP':
                        print(AiChoose)
                        print("1 = Rock, 2 = Paper, 3 = Scissors")
                        choose = input("Choose as R(Rock) P(Paper) S(Scissors)< ")
                        time.sleep(0.5)
                        print("Rock Paper Scissors Shoot!")
                        PowerUps.remove("CHEAT PAPER")
                        print("")

                    elif choose == 'P2S':
                        AIScore -= 1
                        PowerUps.remove("PLAYER 2 SCORE")

                    if choose == 'IN':
                        time.sleep(0.5)
                        print("Rock Paper Scissors Shoot!")
                        print("")

                        print("Invincibe!")
                        print("")
                        print(f"Your Score: {YourScore}")
                        print(f"Player 2 Score: {AIScore}")
                        PowerUps.remove("INVINCIBE")

                    if choose == 'R' and AiChoose == 2:
                        print("Player 2's Paper Smoothered Your's Rock!")
                        AIScore += 1
                        if Settings == 'H' or Settings == 'HH':
                            AITrick = random.randint(1, 2)
                            if AITrick == 1:
                                AiChoose == 1

                    elif choose == 'P' and AiChoose == 1:
                        print("Your Paper Smoothered Player 2's Rock!")
                        YourScore += 1
                        Points += 1
                        if Settings == 'N':
                            AIRevenge = random.randint(1, 2)
                            if AIRevenge == 1:
                                AiChoose == 2

                    elif choose == 'P' and AiChoose == 3:
                        print("Player 2's Scissors Cuts Your's Paper!")
                        AIScore += 1
                        if Settings == 'H' or Settings == 'HH':
                            AITrick = random.randint(1, 2)
                            if AITrick == 1:
                                AiChoose == 1

                    elif choose == 'S' and AiChoose == 2:
                        print("Your Scissors Cuts Player 2's Paper!")
                        YourScore += 1
                        Points += 1
                        if Settings == 'N':
                            AIRevenge = random.randint(1, 2)
                            if AIRevenge == 1:
                                AiChoose == 2

                    elif choose == 'S' and AiChoose == 1:
                        print("Player 2's Rock Breaks Your's Scissors!")
                        AIScore += 1
                        if Settings == 'H' or Settings == 'HH':
                            AITrick = random.randint(1, 2)
                            if AITrick == 1:
                                AiChoose == 1

                    elif choose == 'R' and AiChoose == 3:
                        print("Your Rock Breaks Player 2's Scissors!")
                        YourScore += 1
                        Points += 1
                        if Settings == 'N':
                            AIRevenge = random.randint(1, 2)
                            if AIRevenge == 1:
                                AiChoose == 2
                    else:
                        print("Is a Tie!")
                    print("")

                    print(f"Your Score: {YourScore}")
                    print(f"Player 2 Score: {AIScore}")
                    
            def main_system():
                while True:
                    main_elements()
                    # Again
                    again = input("Again? Y/N: ")
                    if again == 'Y':
                        againY = "Yes"
                        os.system('cls' if os.name == 'nt' else 'clear')
                        YourScore == 0
                        AIScore == 0
                        main_elements()
                        continue

                    elif again == 'N':
                        # When the var again equals to 'N'
                        againY = "No"
                        menu()
                        
                    else:
                        print("Use Upper Case")

            main_system()
        elif menu == 'Q':
            exit()# Exits the Game

        elif menu == 'SS':
            print(f"Current:-{Settings}")
            Settings = input("""Settings:-
                Difficulty-
                Easy:
                            In Easy mode, Player 2 is not smart or revenge.
                Normal:
                            In Normal mode, Player 2 is not smart but, its does revenge.
                Hard:
                            In Hard mode, Player 2 is smart and revenge.
                Hard+:
                            In Hard+ mode, Player 2 is the same as Hard mode but you dont have any powerups.
                            
                Which do you want to choose?
                            E(Easy) N(Normal) H(Hard) HH(Hard+): """)
            
            if Settings == 'E':
                print("Set! to Easy")

                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif Settings == 'N':
                print("Set! to Normal")

                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif Settings == 'H':
                print("Set! to Hard")

                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif Settings == 'HH':
                print("Set! to Hard+")

                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            else:
                print("Pls you Uppe case or enter a different one")
                print("Back to Start menu")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
        elif menu == 'P':
                    if Settings != 'HH':
                        agained = 'No'
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(Points)
                        if Settings == 'H':
                            print("""PowerUps:-
                                1: 📰 Cheat Paper - The Cheat Paper helps to find what the other Player Move. Cost:- 15
                                2: 👍Boost Score - The Boost Score add a extra Point. Cost:- 18
                                3: 💯 Player2 Score - The Player2 Score -1 Point to Player 2. Cost:- 30
                                4: 🤞Invincible - The Invincible can make you win. Cost:- 50""")
                            
                        elif Settings == 'E':
                            print("""PowerUps:-
                                1: 📰 Cheat Paper - The Cheat Paper helps to find what the other Player Move. Cost:- 3
                                2: 👍Boost Score - The Boost Score add a extra Point. Cost:- 6
                                3: 💯 Player2 Score - The Player2 Score -1 Point to Player 2. Cost:- 10
                                4: 🤞Invincible - The Invincible can make you win. Cost:- 13""")
                            
                        elif Settings == 'N':
                            print("""PowerUps:-
                                1: 📰 Cheat Paper - The Cheat Paper helps to find what the other Player Move. Cost:- 10
                                2: 👍Boost Score - The Boost Score add a extra Point. Cost:- 8
                                3: 💯 Player2 Score - The Player2 Score -1 Point to Player 2. Cost:- 15
                                4: 🤞Invincible - The Invincible can make you win. Cost:- 30""")
                            
                        buy = input(""""Do you want to buy CP(Cheat Paper),
                                    BS(Boost Score), P2S(Player 2 Score) or IN(Invincibe) N(Exit)?""")
                            
                        if buy == "CP": # Cheat Paper
                            if Points >= 10 and Settings == 'N' or Points >= 15 and Settings == 'H' or Points >= 3 and Settings == 'E':
                                print("You have buyed The Cheat Paper")
                                print("In game, Enter CP to access the Cheat Paper")
                                print("")
                                print(f"{i: ^70} The Rock, Paper, Scrissors Game!")
                                print("")
                                PowerUps.append("CHEAT PAPER")
                                Points -= 5
                                Amount = PowerUps.count("CHEAT PAPER")
                                print(f"you have {Amount} of Cheat Papers")
                                continue
                            else:
                                print("Sorry you don't have the Points")
                                continue

                        elif buy == "BS": # Boost Score
                            if Points >= 8 and Settings == 'N' or Points >= 18 and Settings == 'H' or Points >= 6 and Settings == 'E':
                                print("You have buyed the Boost Score")
                                print("Point added")
                                print(Points)
                                Points += 1
                                continue
                            else:
                                print("Sorry you don't have the Points")
                                continue

                        elif buy == "P2S": # Player 2 Score
                            if Points >= 15 and Settings == 'N' or Points >= 30 and Settings == 'H' or Points >= 10 and Settings == 'E':
                                print("You have buyed the Player 2 Score")
                                print("In game, Enter P2S to access the Player 2 Score")
                                print("")
                                PowerUps.append("PLAYER 2 SCORE")
                                Amount = PowerUps.count("PLAYER 2 SCORE")
                                print(f"you have {Amount} of Player 2 Score")
                                Points -= 20
                                continue
                            else:
                                print("Sorry you don't have the Points")
                                continue

                        elif buy == "IN": # Invincibe
                            if Points >= 30 and Settings == 'N' or Points >= 50 and Settings == 'H' or Points >= 13 and Settings == 'E':
                                print("You have buyed the Invicibe")
                                print("In game, Enter IN to access the Player Invincibe")
                                print("")
                                PowerUps.append("INVINCIBE")
                                Amount = PowerUps.count("INVINCIBE")
                                print(f"you have {Amount} of Invincibe")
                                Points -= 50
                                continue
                            else:
                                print("Sorry you don't have the Points")
                                continue
                    else:
                        print("You are in Hard+, so the Powerups are not available.")
                        continue

elif game == 'TRPG':
    points = random.randint(5, 10)
    Health = random.randint(35, 100)
    Strength = random.randint(20, 200)
    i = ""
    SwordsName = ["Stone Sword", "Ruby Sword", "Steel Sword", "Platinum Sword", "Gold Sword", "Diamond Sword"]
    CostsofSwords = {"Stone Sword": 15, "Ruby Sword": 29, "Steel Sword": 45, "Platinum Sword": 75, "Gold Sword": 100, "Diamond Sword": 150}

    SpellsName = ["Poison Spell", "Affect Spell", "Strength Spell"]
    CostsofSpells = {"Poison Spell": 12, "Affect Spell": 20, "Strength Spell": 30}

    typeofSword = ["Default Sword"]
    typeofSpell = []

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{i: ^65}TextRPG")
    print("""S(Start)➡️
        Q(Quit)❌""")
    menu = input("> ")

    if menu == 'S':
        name = input("Name: ")
        print("")

        print(f"""Name: {name}
        Health: {Health}
        Strength: {Strength}""")

        print("Game Starts!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            def game_loop():
                mainStart = 'Yes'
                if mainStart == 'Yes':
                    print("Where do you want to go?W(Store🏪), S(Forest🌲), A(Next Side◀️), D(Next Side▶️)")
                    go = input("> ")

                mainStart = 'No'
                if go == 'W':
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Points: {points}")
                        print(f"""Welcome to the Store!🏬
                            want do you want to buy?
                            
                            SWORDS:
                                1. {SwordsName[0]}(SS): Strength- 35, Cost: {CostsofSwords['Stone Sword']} 
                                2. {SwordsName[1]}(RS): Strength- 50, Cost: {CostsofSwords['Ruby Sword']}
                                3. {SwordsName[2]}(STS): Strength- 75, Cost: {CostsofSwords['Steel Sword']}
                                4. {SwordsName[3]}(PS): Strength- 100, Cost: {CostsofSwords['Platinum Sword']}
                                5. {SwordsName[4]}(GS): Strength- 150, Cost: {CostsofSwords['Gold Sword']}
                                6. {SwordsName[5]}(DS): Strength- 200, Cost: {CostsofSwords['Diamond Sword']}
                            
                            SPELLS:
                                1. {SpellsName[0]}(PS): Strength- 20, Cost: {CostsofSpells['Poison Spell']}
                                2. {SpellsName[1]}(AS): Can affect you or the enemy, Cost: {CostsofSpells['Affect Spell']}
                                3. {SpellsName[2]}(SSS): Strength Power- 35, Cost: {CostsofSpells['Strength Spell']}
                            """)
                        
                        buy = input("N(Exit)> ")
                        if buy == 'N':
                            mainStart = 'Yes'

                        elif not points >= min(CostsofSwords.values()):
                            if buy == CostsofSwords:
                                print("Sorry but, you don't have enough points for a sword.")
                                time.sleep(0.5)
                                print("Buy something else")
                                continue

                        elif not points >= min(CostsofSpells.values()):
                            if buy == CostsofSpells:
                                print("Sorry but, you don't have enough points for a spell.")
                                time.sleep(0.5)
                                print("Buy something else")
                                continue

                        elif points >= CostsofSwords["Stone Sword"]:
                            print("You have buyed the Stone Sword!")
                            typeofSword.append("Stone Sword")
                            print("Contiuning...")
                            continue

                        elif points >= CostsofSwords["Ruby Sword"]:
                            print("You have buyed the Ruby Sword!")
                            typeofSword.append("Ruby Sword")
                            print("Contiuning...")
                            continue

                        elif points >= CostsofSwords["Steel Sword"]:
                            print("You have buyed the Steel Sword!")
                            typeofSword.append("Steel Sword")
                            print("Contiuning...")
                            continue
                        
                        elif points >= CostsofSwords["Platinum Sword"]:
                            print("You have buyed the Platinum Sword!")
                            typeofSword.append("Platinum Sword")
                            print("Contiuning...")
                            continue
                        
                        elif points >= CostsofSwords["Gold Sword"]:
                            print("You have buyed the Gold Sword!")
                            typeofSword.append("Gold Sword")
                            print("Contiuning...")
                            continue

                        elif points >= CostsofSwords["Diamond Sword"]:
                            print("You have buyed the Diamond Sword!")
                            typeofSword.append("Diamond Sword")
                            print("Contiuning...")
                            continue


                        if points >= CostsofSpells["Poison Spell"]:
                            print("You have buyed the Poison Spell!")
                            typeofSword.append("Diamond Sword")
                            print("Contiuning...")
                            continue

                        elif points >= CostsofSpells["Affect Spell"]:
                            print("You have buyed the Affect Spell!")
                            typeofSpell.append("Affect Spell")
                            print("Contiuning...")
                            continue

                        elif points >= CostsofSpells["Strength Spell"]:
                            print("You have buyed the Strength Spell!")
                            typeofSpell.append("Strength Spell")
                            print("Contiuning...")
                            continue

                        elif points >= CostsofSpells["Invincible Spell"]:
                            print("You have buyed the Invincible Spell!")
                            typeofSpell.append("Invincible Spell")
                            print("Contiuning...")
                            continue


                elif go == 'S':
                    os.system('cls' if os.name == 'nt' else 'clear')

                    print("You are in the forest")
                    while True:
                        print("Where do you want to move? W(up), S(Exit), A(left), D(right)")
                        move = input("> ")

                        if move not in ['A', 'S', 'W', 'D']:
                            print("Invalid move. Please enter W, A, S, or D.")
                            continue
                        if move == 'S':
                            print("Exiting Forest")
                            time.sleep(1)

                            os.system('cls' if os.name == 'nt' else 'clear')
                            game_loop()

                        elif move == 'A':
                            print("Entering Battle...")
                            time.sleep(1.5)
                            os.system('cls' if os.name == 'nt' else 'clear')

                            enemy_names = [
            "Malgorth the Malevolent", "the Abyssal",
            "Vorax the Venomous",
            "Drakoth the Dreaded",
            "Syraxis the Shadowlord",
            "Sylvaan the Sinister"
        ]                   
                            
                            random_enemy_names = random.choice(enemy_names)
                            enemy_Health = random.randint(6, 150)
                            enemy_Strength = random.random(15, 100)
                            print(f"""Name: {random_enemy_names}
                                Health: {enemy_Health}
                                Strength: {enemy_Strength}""")
                            print("ATTACK START!")
                            if random.randint(1, 3) == 1:
                                print(f"{random_enemy_names} attacks with a sword.")
                                if enemy_Strength >= 100:
                                    Health -= random.randint(5*4, 5*8)

                                elif enemy_Strength <= 100:
                                    Health -= random.randint(5*2, 5*4)

                                elif enemy_Strength <= 35:
                                    Health -= random.randint(3*4, 3*8)

                            elif random.randint(1, 3) == 2:
                                print(f"{random_enemy_names} blows fire.")
                                if enemy_Strength >= 100:
                                    Health -= random.randint(5*6, 5*8)

                                elif enemy_Strength <= 100:
                                    Health -= random.randint(5*4, 5*6)

                                elif enemy_Strength <= 35:
                                    Health -= random.randint(3*5, 3*8)

                            elif random.randint(1, 3) == 3:
                                print(f"{random_enemy_names} puts a spell on you.")
                                if enemy_Strength >= 100:
                                    Health -= random.randint(5*3, 5*5)

                                elif enemy_Strength <= 100:
                                    Health -= random.randint(5*2, 5*4)

                                elif enemy_Strength <= 35:
                                    Health -= random.randint(3*2, 3*6)

                                print("What do you want to attack with? Sword(WS), Spell(S), Exit(E)")
                                attack = input("> ")
                                    
                                if attack == 'WS':
                                    print("You have: ")
                                    for Swords in typeofSword:
                                        print(Swords)
                                    enter = input("Enter a Sword name: ")
                                    print("You attack with a sword.")

                                    if enter == "Default Sword":
                                        enemy_Health -= Strength*5/20 or Strength*5/40
                                        
                                    elif enter == "Stone Sword":
                                        enemy_Health -= round(Strength*7/27) or round(Strength*7/47)
                                        
                                    elif enter == "Ruby Sword":
                                        enemy_Health -= round(Strength*10/30) or Strength*10/40

                                    elif enter == "Steel Sword":
                                        enemy_Health -= Strength*15/45 or Strength*7/40

                                    elif enter == "Platinum Sword":
                                        enemy_Health -= round(Strength*20/65) or Strength*20/60

                                    elif enter == "Gold Sword":
                                        enemy_Health -= round(Strength*30/95) or Strength*30/90

                                    elif enter == "Diamond Sword":
                                        enemy_Health -= round(Strength*40/135) or Strength*40/130
                                        
                                    elif attack == 'S':
                                        print("You attack with a spell of poison.")
                                        enemy_Health -= max(Strength*7/20, Strength*7/40)

                                elif attack == "S":
                                    print("You have: ")
                                    for Spells in typeofSpell:
                                        print(Spells)
                                    enter = input("Enter a Spell name: ")
                                    print("You attack with a sword.")

                                    if enter == "Poison Spell":
                                        enemy_Health -= round(Strength*5/10) or Strength*5/10

                                    elif enter == "Affect Spell":
                                        if random.randint(1, 2) == 1:
                                            enemy_Health -= round(Strength*5/10) or Strength*5/10
                                        elif random.randint(1, 2) == 2:
                                            Health -= 10 or 20

                                    elif enter == "Strength Power":
                                        Strength += 20 or 30
                                    
                                print(f"Enemy Health: {enemy_Health}")
                                print(f"Your Health: {Health}")
                                    
                                if Health <= 0 or enemy_Health <= 0:
                                    continue
                                    
                                elif Health > 0:
                                    game_loop()

                            elif enemy_Health >= 0:
                                print("You win!")
                                print("You get ", random.randint(15, 30), " points!")
                                os.system('cls' if os.name == 'nt' else 'clear')
                                game_loop()

                elif go == 'A' or go == 'D':
                    game_loop()  
            game_loop()      

elif game == 'COC':
    i = ""
    score = 0
    Costs_of_Auto = {"Auto Money x1": 15, "Auto Money x5": 25, "Auto Money x10": 30, "Auto Money x20": 40, "Auto Money x50": 70, "Auto Money x70": 100, "Auto Money x90": 150, "Auto Money x100": 170}
    buyed_of_Auto = []
    AutoAmount = 0

    Costs_of_Click = {"Click Amount +1": 10, "Click Amount +5": 15, "Click Amount +10": 25, "Click Amount +15": 30, "Click Amount +25": 45, "Click Amount +40": 60, "Click Amount +70": 80, "Click Amount +90": 100, "Click Amount +100": 150}
    buyed_of_Click = []
    ClickAmount = 1

    SrNo = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    def menu():
        print(f"{i: ^125}💰Coin Clicker!💰")
        print("""What do you want to Enter?
            C(Click)👆, S(Shop)🛒, E(Exit)❌""")
        
        global Enter
        Enter = ""
        Enter = input("Enter: ")
    menu()

    if Enter == 'C':
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Score: ", score)
        
            EnterClick = input("CL(Click)👆,E(Exit)❌, Buyed Powerups(BP)👍")
            score += AutoAmount

            if EnterClick == 'CL':
                score += ClickAmount
                time.sleep(0.3)
                continue

            elif EnterClick == 'E':
                print("Back to Menu...")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear') 
                menu()

            elif EnterClick == 'BP':
                print("Opening....")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear') 
                for index in buyed_of_Auto:
                    SrNo += 1
                    print("AUTO CLICKS")
                    print(f" {SrNo}: " + index)

                print("""
    """)    

                for index in buyed_of_Click:
                    SrNo += 1
                    print("CLICKS")
                    print(f" {SrNo}: " + index)


    elif Enter == 'S':
        while True:
            print(f"""Welcome to the Shop!
                Score: {score}

                AUTO CLICKS:
                    1. Auto Money x1: Cost- {Costs_of_Auto['Auto Money x1']}
                    2. Auto Money x5: Cost- {Costs_of_Auto['Auto Money x5']}
                    3. Auto Money x10: Cost- {Costs_of_Auto['Auto Money x10']}
                    4. Auto Money x20: Cost- {Costs_of_Auto['Auto Money x20']}
                    5. Auto Money x50: Cost- {Costs_of_Auto['Auto Money x50']}
                    6. Auto Money x70: Cost- {Costs_of_Auto['Auto Money x70']}
                    7. Auto Money x90: Cost- {Costs_of_Auto['Auto Money x90']}
                    8. Auto Money x100: Cost- {Costs_of_Auto['Auto Money x100']}
                    
                CLICKS:
                    1. Click Amount +1: Cost- {Costs_of_Click['Click Amount +1']}
                    2. Click Amount +5: Cost- {Costs_of_Click['Click Amount +5']}
                    3. Click Amount +10: Cost- {Costs_of_Click['Click Amount +10']}
                    4. Click Amount +15: Cost- {Costs_of_Click['Click Amount +15']}
                    5. Click Amount +25: Cost- {Costs_of_Click['Click Amount +25']}
                    6. Click Amount +40: Cost- {Costs_of_Click['Click Amount +40']}
                    7. Click Amount +70: Cost- {Costs_of_Click['Click Amount +70']}
                    8. Click Amount +90: Cost- {Costs_of_Click['Click Amount +90']}
                    9. Click Amount +100: Cost- {Costs_of_Click['Click Amount +100']}
                    """)
            
            EnterShop = input("N(Exit)> ")

            if not min(Costs_of_Auto.values()) >= score:
                if EnterShop == Costs_of_Auto.keys():
                    print("You dont have the amount of points")
            
            elif EnterShop == 'N':
                menu()

            elif min(Costs_of_Auto.values()) >= score or min(Costs_of_Click.values()) >= score:
                if EnterShop == Costs_of_Auto.keys() or EnterShop == Costs_of_Click.keys():
                    print("Buyed!")
                    continuing = input("Continue?(Y/N)> ")
                    if continuing == 'Y':
                        continue
                    elif continuing == 'N':
                        menu()

            elif not min(Costs_of_Click.values()) >= score:
                if EnterShop == Costs_of_Click.keys():
                    print("You dont have the amount of points")


            elif min(Costs_of_Auto['Auto Money x1']) >= score:
                if EnterShop == 'Auto Money x1':
                    AutoAmount += 1
                    buyed_of_Auto.append('Auto Money x1')

            elif min(Costs_of_Auto['Auto Money x5']) >= score:
                if EnterShop == 'Auto Money x5':
                    AutoAmount += 5
                    buyed_of_Auto.append('Auto Money x5')

            elif min(Costs_of_Auto['Auto Money x10']) >= score:
                if EnterShop == 'Auto Money x10':
                    AutoAmount += 10
                    buyed_of_Auto.append('Auto Money x10')

            elif min(Costs_of_Auto['Auto Money x20']) >= score:
                if EnterShop == 'Auto Money x20':
                    AutoAmount += 20
                    buyed_of_Auto.append('Auto Money x20')

            elif min(Costs_of_Auto['Auto Money x50']) >= score:
                if EnterShop == 'Auto Money x50':
                    AutoAmount += 50
                    buyed_of_Auto.append('Auto Money x50')

            elif min(Costs_of_Auto['Auto Money x70']) >= score:
                if EnterShop == 'Auto Money x70':
                    AutoAmount += 70
                    buyed_of_Auto.append('Auto Money x70')

            elif min(Costs_of_Auto['Auto Money x90']) >= score:
                if EnterShop == 'Auto Money x90':
                    AutoAmount += 90
                    buyed_of_Auto.append('Auto Money x90')

            elif min(Costs_of_Auto['Auto Money x100']) >= score:
                if EnterShop == 'Auto Money x100':
                    AutoAmount += 100
                    buyed_of_Auto.append('Auto Money x100')



            elif min(Costs_of_Click['Click Amount +1']) >= score:
                if EnterShop == 'Click Amount +1':
                    ClickAmount += 1
                    buyed_of_Click.append('Click Amount +1')

            elif min(Costs_of_Click['Click Amount +5']) >= score:
                if EnterShop == 'Click Amount +5':
                    ClickAmount += 5
                    buyed_of_Click.append('Click Amount +5')

            elif min(Costs_of_Click['Click Amount +10']) >= score:
                if EnterShop == 'Click Amount +10':
                    ClickAmount += 10
                    buyed_of_Click.append('Click Amount +10')

            elif min(Costs_of_Click['Click Amount +15']) >= score:
                if EnterShop == 'Click Amount +15':
                    ClickAmount += 15
                    buyed_of_Click.append('Click Amount +15')

            elif min(Costs_of_Click['Click Amount +25']) >= score:
                if EnterShop == 'Click Amount +25':
                    ClickAmount += 25
                    buyed_of_Click.append('Click Amount +25')

            elif min(Costs_of_Click['Click Amount +40']) >= score:
                if EnterShop == 'Click Amount +40':
                    ClickAmount += 40
                    buyed_of_Click.append('Click Amount +40')

            elif min(Costs_of_Click['Click Amount +70']) >= score:
                if EnterShop == 'Click Amount +70':
                    ClickAmount += 70
                    buyed_of_Click.append('Click Amount +70')

            elif min(Costs_of_Click['Click Amount +90']) >= score:
                if EnterShop == 'Click Amount +90':
                    ClickAmount += 90
                    buyed_of_Click.append('Click Amount +90')

            elif min(Costs_of_Click['Click Amount +100']) >= score:
                if EnterShop == 'Click Amount +100':
                    ClickAmount += 100
                    buyed_of_Click.append('Click Amount +100')

elif game == "FLAB":
    os.system('cls' if os.name == 'nt' else 'clear')

    # Generate a random number between -50 and 50 for the initial pipe height
    pipeHeight = random.randint(0, 50)

    # Initialize variables
    flap = 0
    move = 0
    score = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    def game_loop():

        global pipeHeight
        global score
        global move
        global flap

        print("Flappy Bird!🐦")
        menu = input("""S(Start)▶️,
    Q(Quit)❌:""")
        

        if menu == "S":
            while True:
            
                print("Score: ", score)
                # Prompt the user to flap or fall
                flapOrNot = input("Flap (Fl) or Fall (Fa)?> ")

                # If the user chooses to fall
                if flapOrNot == "Fa":
                    print("Continue falling...")
                    flap -= 10
                    move += 1
                    continue

                # If the user chooses to flap
                elif flapOrNot == "Fl":
                    print("Flap!")
                    flap += 10
                    move += 1

                
                # If the pipe height is 0, generate a new random height
                if pipeHeight == 0:
                    pipeHeight = random.randint(-50, 50)
                    continue

                # Check if the player touched the pipe
                if pipeHeight <= flap:
                    print("You touched the pipe, Game over!")
                    playAgain = input("Again (Y(Yes) / N(No))?> ")

                    # If the player wants to play again
                    if playAgain == "Y":
                        pipeHeight = random.randint(-50, 50)
                        flap = 0
                        move = 0
                        continue

                    # If the player doesn't want to play again
                    elif playAgain == "N":
                        exit()

                # Check if the player passed a pipe
                elif not pipeHeight == flap and move == 6:
                    print("You passed a pipe, 1 point added!")
                    score += 1
                    move = 0
                    continue
                os.system('cls' if os.name == 'nt' else 'clear')

        elif menu == "Q":
            exit()

    game_loop()

elif game == "CRR":
    import random, time
import os

score = 0

os.system('cls' if os.name == 'nt' else 'clear')

def game_loop():

    global score

    print("Crossy Road🃏")
    menu = input("""S(Start)▶️
Q(Quit)❌""")

    if menu == "S":
        while True:
            car = random.randint(0, 1)
            print("Score: ", score)
            move = input("Move?Y/N: ")

            if car == 1:
                print("You crashed!")
                again = input("Again?N/Y: ")
                if again == "Y":
                    continue

                elif again == "N":
                    exit()

            if move == "Y":
                print("move")
                score += 1
                continue

            elif move == "N":
                print("Same...")
                continue

    elif menu == "Q":
        exit()

game_loop()