class Piece:
	def __init__ (color):
		self.color = color

class King (Piece):
	def is_legal_move (self, pos1, pos2, board):
		""" check if this piece can move in the specified direction """
		if abs(pos2[1] - pos1[1]) <= 1 and abs(pos2[0] - pos1[0]) <= 1:
			return True
		return False

class Pawn:
	def allowed_direction (self):
		""" In what direction can the pawn of this color move """
		if self.color = "w":
			return 1
		return -1

	def is_legal_move (self, pos1, pos2, board):
		""" Check if this piece can move in the specified direction, ignore if there are other pieces unless it should not be able to take it or has to take it for it to be a valid move """
		if pos2[1] - pos1[1] == self.allowed_direction() and pos2[0] == pos1[0] and not board.get(pos2, False):
			return True
		elif board.get(pos2, False) and pos2[1] - pos1[1] == self.allowed_direction() and abs(pos2[0] - pos1[0]) == 1:
			return True
		return False

class Rook:
	def is_legal_move (self, pos1, pos2, board):
		""" Check if this piece can move in the specified direction, ignore if there are other pieces unless it should not be able to take it or has to take it for it to be a valid move """
		if pos2 == pos1:
			return False

		if not (pos2[1] == pos1[1] or pos2[0] == pos1[0]):
			return False

		if self.piece_in_the_way(pos1, pos2, board):
			return False
		return True

	def piece_in_the_way (self, pos1, pos2, board):
		""" See if there is a piece in the way but only check horizontally and vertically """
		sign = abs(pos2[1] - pos1[1]) / pos2[1] - pos1[1]
		for y in range(pos2[1], pos1[1], sign):
			if board.get((pos2[0], y), False):
				return True

		sign = abs(pos2[0] - pos1[0]) / pos2[0] - pos1[0]
		for x in range(pos2[0], pos1[0], sign):
			if board.get((x, pos2[1]), False):
				return True

		return False


class Bishop:
	def is_legal_move (self, pos1, pos2, board):
		""" Check if this piece can move in the specified direction, ignore if there are other pieces unless it should not be able to take it or has to take it for it to be a valid move """
		if not abs(pos2[1] - pos1[1]) == abs(pos2[0] - pos1[0]):
			return False

		if self.piece_in_the_way(pos1, pos2, board):
			return False

		return True

	def piece_in_the_way (self, pos1, pos2, board):
		""" Is there a piece on the direct way """
		sign = abs(pos2[1] - pos1[1]) / pos2[1] - pos1[1]
		
		for pos in range(pos2[1], pos1[1], sign):
			if board.get((pos, pos), False):
				return True

		return False

class Knight:
	def is_legal_move (self, pos1, pos2, board):
		""" Check if this piece can move in the specified direction, ignore if there are other pieces unless it should not be able to take it or has to take it for it to be a valid move """
		if abs(pos1[0] - pos2[0]) == 1 and abs(pos1[1] - pos1[1]) == 2:
			return True
		if abs(pos1[1] - pos2[1]) == 1 and abs(pos1[0] - pos1[0]) == 2:
			return True
		return False
