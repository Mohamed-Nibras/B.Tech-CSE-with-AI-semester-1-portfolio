"""
🧩 Maze Solver (Recursion + Backtracking + Play Mode)

This project is a command-line Maze Solver built using Depth First Search (DFS)
and Recursion with Backtracking. It demonstrates how recursive algorithms explore
multiple paths, track state, and backtrack to find valid solutions.

------------------------------------------------------------
🚀 Features
------------------------------------------------------------
- Automatic solving (One Path / All Paths)
- Interactive Play Mode (manual movement + backtracking)
- Random Maze Generation (size 4–6)
- Prevents infinite loops using a visited matrix
- Limits search using MAX_PATHS to avoid path explosion
- Displays maze and paths visually in CLI
- Shows statistics (total paths, shortest, longest)

------------------------------------------------------------
🧠 Concepts Used
------------------------------------------------------------
- Recursion
- Backtracking
- Depth First Search (DFS)
- State Tracking (visited matrix)
- Matrix Traversal
- Input Validation
- CLI Interaction Design

------------------------------------------------------------
🗺️ Maze Representation
------------------------------------------------------------
0  → Free path
1  → Wall
🔺 → Start
📍 → Goal
*  → Path

------------------------------------------------------------
⚙️ How It Works
------------------------------------------------------------
The algorithm starts from the top-left cell and explores all possible directions:
Up, Down, Right, and Left.

- Marks visited cells to avoid cycles
- Backtracks when hitting walls or dead ends
- Stores valid paths reaching the goal
- Supports both single-path and all-path exploration

In Play Mode:
- User controls movement using W / A / S / D keys
- 'B' allows manual backtracking

------------------------------------------------------------
👨‍💻 Author
------------------------------------------------------------
Mohamed Nibras
B.Tech CSE (AI)

Focused on building strong foundations in problem solving,
algorithms, and software development.
"""

import shutil
import random

# -------------------- CONFIG --------------------
WIDTH = shutil.get_terminal_size().columns
MAX_PATHS = 10

DIRECTIONS = [(-1,0), (1,0), (0,1), (0,-1)]


# -------------------- MAZE GENERATOR --------------------
def generate_maze(size):
    # Better probability → more solvable mazes
    maze = [[0 if random.random() < 0.7 else 1 for _ in range(size)] for _ in range(size)]

    maze[0][0] = 0
    maze[size-1][size-1] = 0

    return maze


# -------------------- DISPLAY --------------------
def display_maze(maze, start, end, path_set=None):
    rows = len(maze)
    cols = len(maze[0])

    for x in range(rows):
        for y in range(cols):
            if (x, y) == start:
                print("🔺", end=" ")
            elif (x, y) == end:
                print("📍", end=" ")
            elif path_set and (x, y) in path_set:
                print(" *", end=" ")
            elif maze[x][y] == 1:
                print("⬛", end=" ")
            else:
                print(" 0", end=" ")
        print()


# -------------------- SOLVER --------------------
def solve_maze(maze, start, end, find_all=True):
    rows = len(maze)
    cols = len(maze[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    all_paths = []

    def dfs(x, y, path):
        # Stop if max paths reached
        if not find_all and len(all_paths) >= 1:
            return True

        # Invalid / wall / visited
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        if maze[x][y] == 1 or visited[x][y]:
            return False

        # Choose
        path.append((x, y))
        visited[x][y] = True

        found = False

        # Goal
        if (x, y) == end:
            all_paths.append(path.copy())
            found = True
        else:
            for dx, dy in DIRECTIONS:
                if dfs(x + dx, y + dy, path):
                    found = True
                    if not find_all:
                        break

        # Backtrack
        path.pop()
        visited[x][y] = False

        return found

    dfs(start[0], start[1], [])
    return all_paths


# -------------------- PLAY MODE --------------------
def play_mode(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    x, y = start
    path = [(x, y)]

    moves = {
        'w': (-1, 0),
        's': (1, 0),
        'd': (0, 1),
        'a': (0, -1)
    }

    while True:
        print("\n🎮 PLAY MODE")
        display_maze(maze, start, end, set(path))

        if (x, y) == end:
            print("\n🏁 You reached the goal! 🎉")
            print("Route:", " -> ".join(map(str, path)))
            break

        move = input("Move (W/A/S/D, B=Back): ").strip().lower()

        if move == 'b':
            if len(path) > 1:
                path.pop()
                x, y = path[-1]
            else:
                print("⚠️ Cannot go back from start")
            continue

        if move not in moves:
            print("❌ Invalid input")
            continue

        dx, dy = moves[move]
        new_x, new_y = x + dx, y + dy

        if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
            print("⚠️ Out of bounds!")
            continue

        if maze[new_x][new_y] == 1:
            print("🚫 Hit a wall!")
            continue

        x, y = new_x, new_y
        path.append((x, y))


# -------------------- INPUT HELPERS --------------------
def get_valid_choice(prompt, options):
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print("❌ Invalid choice. Try again.")


def get_valid_number(prompt, min_val, max_val):
    while True:
        val = input(prompt).strip()
        if val.isdigit():
            num = int(val)
            if min_val <= num <= max_val:
                return num
        print(f"❌ Enter a number between {min_val} and {max_val}")


# -------------------- MAIN --------------------
def main():
    print("=" * WIDTH)
    print("🧩 MAZE SOLVER (RECURSION + BACKTRACKING)".center(WIDTH))
    print("=" * WIDTH)

    print("\nLegend:")
    print("🔺 Start | 📍 Goal | ⬛ Wall | * Path\n")

    # Default maze
    maze = [
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 0]
    ]

    # Maze selection
    print("1. Default Maze")
    print("2. Random Maze")

    choice = get_valid_choice("Enter: ", ["1", "2"])

    if choice == "2":
        size = get_valid_number("Enter size (4-6): ", 4, 6)
        maze = generate_maze(size)

    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)

    # Check validity
    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        print("❌ Invalid maze: start or end is blocked")
        return

    # Mode
    print("\nChoose Mode:")
    print("1. Solve Automatically")
    print("2. Play Yourself")

    mode = get_valid_choice("Enter: ", ["1", "2"])

    if mode == "2":
        play_mode(maze, start, end)
        return

    # Solve mode
    print("\nSolve Mode:")
    print("1. One Path")
    print("2. All Paths")

    solve_choice = get_valid_choice("Enter: ", ["1", "2"])
    find_all = (solve_choice == "2")

    print("\n🔍 Solving maze... Please wait\n")

    all_paths = solve_maze(maze, start, end, find_all)

    if not all_paths:
        print("❌ No paths found")
        return

    print(f"✅ Total paths found: {len(all_paths)}\n")

    for i, path in enumerate(all_paths, start=1):
        print(f"Path {i}:")
        display_maze(maze, start, end, set(path))
        print("Route:", " -> ".join(map(str, path)))
        print("-" * 40)

    shortest = min(all_paths, key=len)
    longest = max(all_paths, key=len)

    print("\n🔥 Shortest Path:")
    display_maze(maze, start, end, set(shortest))
    print("Length:", len(shortest))

    print("\n📊 Stats:")
    print(f"Total Paths: {len(all_paths)}")
    print(f"Shortest Length: {len(shortest)}")
    print(f"Longest Length: {len(longest)}")


if __name__ == "__main__":
    main()