import Pieces

class Board:
	def __init__ (self):
		self.board = {
			("a", 5): Pieces.King("b"),
			("b", 5): Pieces.Knight("b"),
			("c", 5): Pieces.Bishop("b"),
			("d", 5): Pieces.Rook("b"),
			("a", 4): Pieces.Pawn("b"),
			("a", 1): Pieces.King("w"),
			("b", 1): Pieces.Knight("w"),
			("c", 1): Pieces.Bishop("w"),
			("d", 1): Pieces.Rook("w"),
			("d", 2): Pieces.Pawn("w")
		}

	def __str__ (self):
		boardstring = "   ------------------\n"
		boardstring += "  |                  |\n"

		for y in range(5, 0, -1):
			boardstring += str(y) + " |  "
			for x in "abcd":
				boardstring += str(self.board.get((x, y), "  ")) + "  "
			boardstring += "|\n"
			boardstring += "  |                  |\n"

		boardstring += "   ------------------\n"
		boardstring += "     a   b   c   d"
		return boardstring

	def is_valid_position (self, position):
		""" Is the given position a valid position of the form 'a1' where a is a character and 1 is an integer between 0 and 6 """
		try:
			return len(position) == 2 and position[0] in "abcd" and int(position[1]) > 0 and int(position[1]) < 6
		except:
			return False

	def move_piece (self, color, frompos, topos):
		""" Move the piece from the given color (w/b) from frompos to topos and return if it succeeded"""
		piece_from = self.board.get(frompos, False)
		piece_to = self.board.get(topos, False)

		if piece_from.color != color:
			print("Please select a position containing a " + self.get_full_color(color) + " piece.")
			return False

		if not piece_from or not piece_from.is_legal_move(frompos, topos, self.board) or (piece_to and piece_to.color == color):
			print("Invalid move. Try again.")
			return False

		self.board[topos] = self.board.pop(frompos)
		return True

	def get_full_color (self, color):
		""" Get the full human readable lower case color from the first letter """
		if color == "w":
			return "white"
		return "black"

	def get_opposite_color (self, color):
		""" Get the first letter of the opposite colors first letter """
		if color == "w":
			return "b"
		return "w"

	def get_king_position (self, color):
		""" Get the king of the given color """
		for (position, piece) in self.board.items():
			if isinstance(piece, Pieces.King) and piece.color == color:
				return (position, piece)
		return False

	def game_over (self, color):
		""" Run trough every piece of the opposite color and see if they have a legal move to the king """

		king = self.get_king_position(color)
		enemy = self.get_opposite_color(color)

		for (position, piece) in self.board.items():
			if piece.color == enemy and piece.is_legal_move(position, king[0], self.board):
				return True