class Piece:
	def __init__ (self, color):
		self.color = color

	def get_real (self, pos):
		""" Change coords in the form (char, int) to (int, int) [required by specification]"""
		return (ord(pos[0]) - 96, pos[1])

class King (Piece):
	def __str__ (self):
		return "K" + self.color

	def is_legal_move (self, pos1, pos2, board):
		""" check if this piece can move in the specified direction """
		pos1 = self.get_real(pos1)
		pos2 = self.get_real(pos2)
		
		return abs(pos2[1] - pos1[1]) <= 1 and abs(pos2[0] - pos1[0]) <= 1

class Pawn (Piece):
	def __str__ (self):
		return "P" + self.color

	def allowed_direction (self):
		""" In what direction can the pawn of this color move """
		if self.color == "w":
			return 1
		return -1

	def is_legal_move (self, pos1, pos2, board):
		""" Check if this piece can move in the specified direction, ignore if there are other pieces unless it should not be able to take it or has to take it for it to be a valid move """
		pos1 = self.get_real(pos1)
		pos2 = self.get_real(pos2)

		if pos2[1] - pos1[1] == self.allowed_direction() and pos2[0] == pos1[0] and not board.get(pos2, False):
			return True
		elif board.get(pos2, False) and pos2[1] - pos1[1] == self.allowed_direction() and abs(pos2[0] - pos1[0]) == 1:
			return True
		return False

class Rook (Piece):
	def __str__ (self):
		return "R" + self.color

	def is_legal_move (self, pos1, pos2, board):
		""" Check if this piece can move in the specified direction, ignore if there are other pieces unless it should not be able to take it or has to take it for it to be a valid move """
		pos1 = self.get_real(pos1)
		pos2 = self.get_real(pos2)

		if pos2 == pos1:
			return False

		if not (pos2[1] == pos1[1] or pos2[0] == pos1[0]):
			return False

		if self.piece_in_the_way(pos1, pos2, board):
			return False

		return True

	def piece_in_the_way (self, pos1, pos2, board):
		""" See if there is a piece in the way but only check horizontally and vertically """
		
		if pos2[1] - pos1[1] != 0:
			sign = int(abs(pos2[1] - pos1[1]) / (pos2[1] - pos1[1]))
			for y in range(pos2[1], pos1[1], -sign):
				if board.get((pos2[0], y), False):
					if y != pos2[1]:
						return True

		if pos2[0] - pos1[0] != 0:
			sign = int(abs(pos2[0] - pos1[0]) / (pos2[0] - pos1[0]))
			for x in range(pos2[0], pos1[0], -sign):
				if board.get((x, pos2[1]), False):
					if x != pos2[0]:
						return True

		return False


class Bishop (Piece):
	def __str__ (self):
		return "B" + self.color

	def is_legal_move (self, pos1, pos2, board):
		""" Check if this piece can move in the specified direction, ignore if there are other pieces unless it should not be able to take it or has to take it for it to be a valid move """
		pos1 = self.get_real(pos1)
		pos2 = self.get_real(pos2)

		if not abs(pos2[1] - pos1[1]) == abs(pos2[0] - pos1[0]):
			return False

		if self.piece_in_the_way(pos1, pos2, board):
			return False

		return True

	def piece_in_the_way (self, pos1, pos2, board):
		""" Is there a piece on the direct way """
		sign = int(abs(pos2[1] - pos1[1]) / (pos2[1] - pos1[1]))

		for pos in range(pos2[1], pos1[1], -sign):
			if board.get((pos, pos), False):
				return True

		return False

class Knight (Piece):
	def __str__ (self):
		return "N" + self.color

	def is_legal_move (self, pos1, pos2, board):
		""" Check if this piece can move in the specified direction, ignore if there are other pieces unless it should not be able to take it or has to take it for it to be a valid move """
		pos1 = self.get_real(pos1)
		pos2 = self.get_real(pos2)

		if abs(pos1[0] - pos2[0]) == 1 and abs(pos1[1] - pos2[1]) == 2:
			return True
		if abs(pos1[1] - pos2[1]) == 1 and abs(pos1[0] - pos2[0]) == 2:
			return True

		return False
