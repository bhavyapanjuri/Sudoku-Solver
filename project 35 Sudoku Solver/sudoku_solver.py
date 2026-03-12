"""
Sudoku Solver and Generator
Solves any valid 9x9 Sudoku puzzle using backtracking with fast pruning
Also generates new Sudoku puzzles
"""

import random


def print_board(board):
    """Display the Sudoku board in a formatted grid"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()


def is_valid(board, row, col, num):
    """Check if placing num at board[row][col] is valid"""
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True


def solve(board):
    """Solve Sudoku using backtracking with pruning"""
    # Find empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try numbers 1-9
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        
                        # Recursively solve
                        if solve(board):
                            return True
                        
                        # Backtrack
                        board[i][j] = 0
                
                return False
    
    return True


def generate_puzzle(difficulty=40):
    """Generate a new Sudoku puzzle
    difficulty: number of cells to remove (30-50 recommended)
    """
    # Create empty board
    board = [[0] * 9 for _ in range(9)]
    
    # Fill diagonal 3x3 boxes (independent)
    for box in range(3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[box * 3 + i][box * 3 + j] = nums[i * 3 + j]
    
    # Solve to get complete board
    solve(board)
    
    # Remove cells to create puzzle
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    
    for i, j in cells[:difficulty]:
        board[i][j] = 0
    
    return board


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("SUDOKU SOLVER & GENERATOR")
    print("=" * 50)
    
    # Example puzzle (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("\n📋 ORIGINAL PUZZLE:")
    print_board(puzzle)
    
    print("\n🔄 Solving...")
    if solve(puzzle):
        print("\n✅ SOLVED PUZZLE:")
        print_board(puzzle)
    else:
        print("\n❌ No solution exists!")
    
    print("\n" + "=" * 50)
    print("🎲 GENERATING NEW PUZZLE...")
    print("=" * 50)
    
    new_puzzle = generate_puzzle(difficulty=45)
    print("\n📋 GENERATED PUZZLE:")
    print_board(new_puzzle)
    
    # Solve the generated puzzle
    print("\n🔄 Solving generated puzzle...")
    if solve(new_puzzle):
        print("\n✅ SOLVED:")
        print_board(new_puzzle)
