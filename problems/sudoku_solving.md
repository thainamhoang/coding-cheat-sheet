# Sudoku Solving
[Sudoku](https://en.wikipedia.org/wiki/Sudoku) is a number-placement puzzle game. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids (box) that compose the grid contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution. 

The two ways of solving the Sudoku can be used are [*Backtracking*](https://www.geeksforgeeks.org/backtracking-algorithms/) and [*Dancing Links*](https://www.geeksforgeeks.org/exact-cover-problem-algorithm-x-set-2-implementation-dlx/). Backtracking is a brute force approach. It is an ordinary recursive way, takes a lot of time and memory, and can be prevented by anti-brute-force sudoku. Dancing Links is a recursive, nondeterministic, depth-first, backtracking algorithm that finds all solutions to the exact cover problem.

## Backtracking

#### Java
```java
public M1_Backtracking_Sudoku(int[][] board) {
    this.board = new int[SIZE][SIZE];
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            this.board[i][j] = board[i][j];
        }
    }
}

private static final int SIZE = 9;
private static final int EMPTY_CELL = 0;
private static int[][] board;

private static boolean isInRow(int row, int num) {
    for (int i = 0; i < SIZE; i++) {
        if (board[row][i] == num) return true;
    }
    return false;
}

private static boolean isInCol(int col, int num) {
    for (int j = 0; j < SIZE; j++) {
        if (board[j][col] == num) return true;
    }
    return false;
}

private static boolean isInBox(int row, int col, int num) {
    int boxRow = row - row % 3;
    int boxCol = col - col % 3;
    for (int i = boxRow; i < boxRow + 3; i++) {
        for (int j = boxCol; j < boxCol + 3; j++) {
            if (board[i][j] == num) return true;
        }
    }
    return false;
}

private static boolean isSatisfied (int row, int col, int num) {
    if (!isInRow(row, num) && !isInCol(col, num) && !isInBox(row, col, num)) return true;
    return false;
}

public static boolean solved() {
    for (int row = 0; row < SIZE; row++) {
        for (int col = 0; col < SIZE; col++) {
            if (board[row][col] == EMPTY_CELL) {
                for (int num = 1; num <= SIZE; num++) {
                    if (isSatisfied(row, col, num)) {
                        board[row][col] = num;
                        
                        if (solved()) {
                            return true;
                        }
                        else {
                            board[row][col] = EMPTY_CELL;
                        }
                    }
                }
                
                return false;
            }
        }
    }  
    return true;
}
```

#### Python
```python
SIZE = 9
EMPTY_CELL = 0

def is_in_row(board, row, num):
    for i in range (SIZE):
        if (board[row][i] == num):
            return True
    return False

def is_in_col(board, col, num):
    for j in range (SIZE):
        if (board[j][col] == num):
            return True
    return false

def is_in_box(board, row, col, num):
    bowRow = row - row % 3
    boxCol = col - col % 3
    for i in range (bowRow, boxRow + 3):
        for j in range (boxCol, boxCol + 3):
            if (board[i][j] == num):
                return True
    return False

def is_satisfied(board, row, col, num):
    return not is_in_row(board, row, num) and not is_in_col(board, col, num) and not is_in_box(board, row, col, num)

def sudoku_solved(board):
    for row in range (SIZE):
        for col in range (SIZE:
            if board[row][col] == EMPTY_CELL:
                for num in range (1, SIZE + 1):
                    if is_satisfied(board, row, col, num):
                        board[row][col] = num

                        if sudoku_solved():
                            return True
                        else:
                            board[row][col] = EMPTY_CELL;
                return False
    return True
```

## Dancing Links

#### Java
```java
```

#### Python
````python
````