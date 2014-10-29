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
			("a", 2): Pieces.Pawn("w")
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
