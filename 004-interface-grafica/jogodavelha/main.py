import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QLayout
from PySide6.QtCore import QSize

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jogo da Velha")
        self.setFixedSize(400, 400)
        self.board = [' '] * 9
        self.current_player = 'X'

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(20)
        self.central_widget.setLayout(self.grid_layout)

        self.status_label = QLabel("Jogo da Velha")
        self.grid_layout.addWidget(self.status_label, 0, 0, 1, 3)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(300, 100)
                button.clicked.connect(lambda _, row=i, col=j: self.make_move(row, col))
                self.grid_layout.addWidget(button, i + 1, j)
                row.append(button)
            self.buttons.append(row)

        self.new_game_button = QPushButton("Novo Jogo")
        self.new_game_button.clicked.connect(self.new_game)
        self.grid_layout.addWidget(self.new_game_button, 4, 0, 1, 3)

    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            if self.check_winner():
                self.status_label.setText(f"Vitória do jogador {self.current_player}")
                self.disable_buttons()
            elif ' ' not in self.board:
                self.status_label.setText("Empate!")
                self.disable_buttons()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.setText(f"Vez do jogador: {self.current_player}")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
            (0, 4, 8), (2, 4, 6)              # Diagonais
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

    def new_game(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        for row in self.buttons:
            for button in row:
                button.setText('')
                button.setEnabled(True)
        self.status_label.setText("Vez do jogador: X")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())