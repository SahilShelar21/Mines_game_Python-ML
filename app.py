import random
from sklearn.linear_model import LogisticRegression

class MinesTableManager:
    def __init__(self):
        self.cheat_mode = False
        self.model = LogisticRegression()
        self.training_data = []
        self.training_labels = []
        initial_data = [[0, 0, 0, 3], [1, 1, 0, 3], [2, 2, 0, 3], [0, 1, 0, 3], [1, 0, 0, 3],
                          [2, 0, 0, 3], [0, 2, 0, 3], [1, 2, 0, 3], [2, 1, 0, 3]]
        initial_labels = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.model.fit(initial_data, initial_labels)

    def create_mines_table(self, mines_amount: int):
        self.mines_table = [["" for _ in range(5)] for _ in range(5)]
        positions = [(x, y) for x in range(5) for y in range(5)]
        random.shuffle(positions)
        for _ in range(mines_amount):
            x, y = positions.pop()
            self.mines_table[x][y] = "💣"
        for x in range(5):
            for y in range(5):
                if self.mines_table[x][y] != "💣":
                    self.mines_table[x][y] = "？"
        self.already_checked = 0
        self.mines_amount = mines_amount
        return self.mines_table

    def return_table(self):
        return self.mines_table

    def check_bomb(self, x: int, y: int, bet_amount: float):
        if self.cheat_mode:
            return False, "💣 You Lost! Your balance is now 0.", 0
        position = self.mines_table[x][y]
        if position == "💣":
            return False, "💣 You Lost! Your balance is now 0.", 0
        elif position == "💎":
            return False, "Already Checked!", bet_amount
        else:
            self.already_checked += 1
            self.mines_table[x][y] = "💎"
            bet_amount *= 2
            self.training_data.append([x, y, self.already_checked, self.mines_amount])
            self.training_labels.append(1)  # 1 for safe
            if len(self.training_data) > 8:
                self.model.fit(self.training_data, self.training_labels)
            return self.mines_table, f"✅ Safe! Your new balance: ${bet_amount}", bet_amount

    def predict_safe(self, x, y):
        try:
            prediction = self.model.predict([[x, y, self.already_checked, self.mines_amount]])
            return prediction[0]
        except ValueError:
            return None

if __name__ == "__main__":
    mines = MinesTableManager()
    cheat_input = input("Enable Developer Cheat Mode? (yes/no): ").strip().lower()
    if cheat_input == "yes":
        mines.cheat_mode = True
        print("🔴 Developer Cheat Mode Activated: Every click will be a mine!")
    mines_amount = int(input("How many Mines? >> "))
    table = mines.create_mines_table(mines_amount)
    bet_amount = float(input("Enter your starting bet amount: $"))
    print("Initial Mines Table:")
    for row in table:
        print(row)
    while True:
        try:
            x = int(input("Enter X coordinate (1-5): ")) - 1
            y = int(input("Enter Y coordinate (1-5): ")) - 1
            prediction = mines.predict_safe(x, y)
            if prediction is not None:
                if prediction == 1:
                    print("ML predicts this spot is safe.")
                else:
                    print("ML predicts this spot is NOT safe.")
            else:
                print("ML model could not make a prediction.")
            result = mines.check_bomb(x, y, bet_amount)
            if isinstance(result[0], list) and "Safe" in result[1]:
                bet_amount = result[2]
                for row in result[0]:
                    print(row)
                print(f"You are safe. Your current balance is ${bet_amount}")
                cashout = input("Cash out now? (yes/no): ").strip().lower()
                if cashout == "yes":
                    print(f"Congratulations! You won ${bet_amount}")
                    break
                else:
                    continue
            else:
                print(result[1])
                break
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 1 and 5.")