from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

Both_Nights = And(AKnight, BKnight)
Both_Knaves = And(AKnave, BKnave)

Knight_N_Knave = And(AKnight, BKnave)
Knave_N_Knight = And(AKnave, BKnight)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),        # Each character is either a Knight or a Knave
    Not(And(AKnight, AKnave)),  # But not both

    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),           # Each character
    Not(And(AKnight, AKnave)),     # is either a Knight
    Or(BKnight, BKnave),           # or a Knave,
    Not(And(BKnight, BKnave)),     # but not both

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, Or(Both_Nights, Both_Knaves)),
    Implication(AKnave, Not(Or(Both_Nights, Both_Knaves))),

    Implication(BKnight, Or(Knight_N_Knave, Knave_N_Knight)),
    Implication(BKnave, Not(Or(Knight_N_Knave, Knave_N_Knight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    Or(Implication(AKnight, AKnight), Implication(AKnight, AKnave)),
    Or(Implication(AKnave, Not(AKnight)), Implication(AKnave, Not(AKnave))),

    # Keep in mind that if a is a Knight, they can't say "I am a Knave"
    Implication(BKnight, And(Implication(AKnight, AKnave),Implication(AKnave, Not(AKnave)))),
    Implication(BKnave, Not(And(Implication(AKnight, AKnave),Implication(AKnave, Not(AKnave))))),

    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)) 
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
