from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

hole = [Card(2, 1), Card(2, 2)]
board = []
score = HandEvaluator.evaluate_hand(hole, board)