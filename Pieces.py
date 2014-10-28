class Piece:
	def __init__ (color):
		self.color = color

	def allowed_direction (self):
		""" In what direction can the pieces of this color move """
		if self.color = "white":
			return 1
		return -1

class King (Piece):
	def is_legal_move (self, pos1, pos2, board):
		""" check if this piece can move in the specified direction """
		if abs(pos2[1] - pos1[1]) <= 1 and abs(pos2[0] - pos1[0]) <= 1:
			return True
		return False

class Pawn:
	def is_legal_move (self, pos1, pos2, board):
		""" check if this piece can move in the specified direction """
		if (pos2[1] - pos1[1] == self.allowed_direction() and pos2[0] == pos1[0]) or (board.get(pos2, False) and pos2[1] - pos1[1] == self.allowed_direction() and abs(pos2[0] - pos1[0])):
			return True
		return False

class Rook:

class Bishop:

class Knight:
