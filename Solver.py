import itertools
import operator

CARD_MAP = {
    'A': 1.0,
    'J': 11.0,
    'Q': 12.0,
    'K': 13.0,
}

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

TARGET = 24
EPS = 1e-6

def parse_card(card):
    if card in CARD_MAP:
        return CARD_MAP.get(card)
    elif card.isdigit() and 1 <= float(card) <= 10:
        return float(card)
    else:
        raise ValueError(f"Invalid card: {card}")

def safe_apply(op,a,b):
    try:
        if op == '/' and abs(b) < EPS:
            return None
        return OPS[op](a,b)
    except:
        return None
    
def solve_24(cards):
    nums = [parse_card(c) for c in cards]
    solutions = set()
    for perm in itertools.permutations(nums):
        for ops in itertools.product(OPS.keys(), repeat=3):
            a, b, c, d = perm
            op1, op2, op3 = ops

            # ((a op1 b) op2 c) op3 d
            r1 = safe_apply(op1, a, b)
            if r1 is not None:
                r2 = safe_apply(op2, r1, c)
                if r2 is not None:
                    r3 = safe_apply(op3, r2, d)
                    if r3 is not None and abs(r3 - TARGET) < EPS:
                        expr = f"(({a} {op1} {b}) {op2} {c}) {op3} {d}"
                        solutions.add(expr)
            
            # (a op1 (b op2 c)) op3 d
            r1 = safe_apply(op2, b, c)
            if r1 is not None:
                r2 = safe_apply(op1, a, r1)
                if r2 is not None:
                    r3 = safe_apply(op3, r2, d)
                    if r3 is not None and abs(r3 - TARGET) < EPS:
                        expr = f"({a} {op1} ({b} {op2} {c})) {op3} {d}"
                        solutions.add(expr)

            # a op1 ((b op2 c) op3 d)
            r1 = safe_apply(op2, b, c)
            if r1 is not None:
                r2 = safe_apply(op3, r1, d)
                if r2 is not None:
                    r3 = safe_apply(op1, a, r2)
                    if r3 is not None and abs(r3 - TARGET) < EPS:
                        expr = f"{a} {op1} (({b} {op2} {c}) {op3} {d})"
                        solutions.add(expr)
            
            # a op1 (b op2 (c op3 d))
            r1 = safe_apply(op3, c, d)
            if r1 is not None:
                r2 = safe_apply(op2, b, r1)
                if r2 is not None:
                    r3 = safe_apply(op1, a, r2)
                    if r3 is not None and abs(r3 - TARGET) < EPS:
                        expr = f"{a} {op1} ({b} {op2} ({c} {op3} {d}))"
                        solutions.add(expr)

            # (a op1 b) op2 (c op3 d)
            r1 = safe_apply(op1, a, b)
            r2 = safe_apply(op3, c, d)
            if r1 is not None and r2 is not None:
                r3 = safe_apply(op2, r1, r2)
                if r3 is not None and abs(r3 - TARGET) < EPS:
                    expr = f"({a} {op1} {b}) {op2} ({c} {op3} {d})"
                    solutions.add(expr)
    return solutions

if __name__ == "__main__":
    cards = input("Enter 4 cards (e.g. A 2 3 J): ").split()
    solutions = solve_24(cards)
    if solutions:
        print("Solutions:")
        for sol in solutions:
            print(sol)
    else:
        print("No solution found.")



