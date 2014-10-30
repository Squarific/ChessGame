import Board

class ChessGame:
	def __init__ (self):
		self.board = Board.Board()
		self.int_turn = 0
		self.history = []

	def save_history (self):
		""" Save the history to the file history.txt """
		file_history = open("history.txt", "w")
		string_history = ""
		color = "White"

		for move in self.history:
			string_history += color + ":\t" + move[0][0] + str(move[0][1]) + " " + move[1][0] + str(move[1][1])

			if not move[2]:
				string_history += " (invalid)"
			else:
				color = self.toggle_color(color)

			string_history += "\n"

		file_history.write(string_history)

	def toggle_color (self, color):
		""" Give back the opposite color """
		if color == "White":
			return "Black"
		return "White"

	def next_color (self):
		""" Return the color that has to do the next move """
		if self.int_turn % 2 == 0:
			return "White"
		return "Black"

	def last_played_color (self):
		""" Return the color that did the last move """
		if self.int_turn % 2 == 0:
			return "Black"
		return "White"

	def ask_positions (self):
		""" Ask the user for a position from/to where pieces should be moved from/to and return a list of the two """

		position = ["", ""]
		while not self.board.is_valid_position(position[0]) and not self.board.is_valid_position(position[1]):
			position[0] = input(self.next_color() + ", what is the location of the piece you would like to move (e.g. a1)?\n")
			position[1] = input(self.next_color() + ", what is the new location of this piece (e.g. a4)?\n")

		return [(position[0][0], int(position[0][1])),
		        (position[1][0], int(position[1][1]))]

	def next_turn (self):
		""" Perform the next turn by asking which piece to move and moving that piece """
		
		positions = self.ask_positions()
		first_letter_color = self.next_color()[0].lower()

		while not self.board.move_piece(first_letter_color, positions[0], positions[1]):
			positions.append(False)
			self.history.append(positions)
			positions = self.ask_positions()

		positions.append(True)
		self.history.append(positions)
		self.int_turn += 1


	def start_game (self):
		""" As long as the game has not ended keep asking the players what to do """
		while not self.board.game_over(self.last_played_color()[0].lower()):
			print(self.board)
			self.next_turn()

		print(self.board)
		print("Game has ended. " + self.last_played_color() + " lost!")

		self.save_history()
