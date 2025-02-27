# Mines_game_Python-ML

This project implements a Mines Swapper game, a gambling application where players uncover gems while avoiding mines. It utilizes Python and machine learning (Logistic Regression) to provide predictive insights during gameplay.

## Project Description

The Mines Swapper game presents a 5x5 grid containing hidden mines and gems. Players click on cells to reveal their contents. Finding a gem doubles the player's bet, while hitting a mine ends the game. A Logistic Regression model is trained during gameplay to predict whether a cell is safe or contains a mine, providing players with strategic guidance.

## Features

* **5x5 Grid Gameplay:** A classic minesweeper-like experience with a 5x5 grid.
* **Gems and Mines:** Randomly generated gems and mines hidden within the grid.
* **Betting System:** Players start with a bet, which doubles with each gem found.
* **Machine Learning Prediction:** A Logistic Regression model predicts safe cells based on player actions.
* **Cheat Mode (Developer Option):** For testing purposes, all clicks result in mines.
* **Clear Game Logic:** Easy-to-understand game mechanics and user interface.

## Technologies Used

* **Python:** Core programming language.
* **Scikit-learn (sklearn):** For the Logistic Regression machine learning model.
* **Random:** For generating random mine and gem placements.

## How to Run

1.  **Prerequisites:**
    * Python 3.x installed.
    * Scikit-learn library installed (`pip install scikit-learn`).

2.  **Clone the Repository (if applicable):**
    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

3.  **Run the Script:**
    ```bash
    python mines_swapper.py
    ```

4.  **Gameplay:**
    * Follow the on-screen prompts to enable cheat mode (optional), set the number of mines, and enter your starting bet.
    * Enter the X and Y coordinates (1-5) of the cell you want to reveal.
    * The machine learning model will provide a prediction before the cell is revealed.
    * If you find a gem, your bet doubles, and you can choose to cash out or continue.
    * If you hit a mine, the game ends.

## Game Logic

1.  **Initialization:**
    * The game board is created with randomly placed mines and gems.
    * A Logistic Regression model is initialized and trained on a small initial dataset.
    * The player enters their starting bet.

2.  **Gameplay Loop:**
    * The player enters coordinates to reveal a cell.
    * The machine learning model predicts whether the cell is safe.
    * If the cell contains a gem:
        * The player's bet doubles.
        * The player can choose to cash out or continue.
        * The model is trained with the new safe cell data.
    * If the cell contains a mine:
        * The game ends.
    * If the cell was already checked, it will say "Already Checked!".

3.  **Machine Learning:**
    * The Logistic Regression model is trained with player actions, classifying cells as safe (1) or mine (0).
    * The model's predictions provide players with strategic guidance.

## Contributing

Contributions are welcome! Please feel free to:

* Suggest improvements to the game logic and user interface.
* Enhance the machine learning model's accuracy.
* Add new features, such as different grid sizes or game modes.
* Report bugs and issues.

## License

This project is licensed under the [License Name] License.

## Author

[Your Name/GitHub Username]
