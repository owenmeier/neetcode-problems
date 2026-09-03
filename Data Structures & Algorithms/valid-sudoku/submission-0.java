class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            List<Character> seen = new ArrayList<>();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                if (seen.contains(board[i][j])) return false;
                seen.add(board[i][j]);
            }
        }

        for (int i = 0; i < 9; i++) {
            List<Character> seen = new ArrayList<>();
            for (int j = 0; j < 9; j++) {
                if (board[j][i] == '.') continue;
                if (seen.contains(board[j][i])) return false;
                seen.add(board[j][i]);
            }
        }

        for (int i = 0; i < 9; i++) {
            List<Character> seen = new ArrayList<>();
            for (int j = 0; j < 9; j++) {
                int row = 3 * (i / 3) + (j / 3);
                int col = 3 * (i % 3) + (j % 3);
                
                if (board[row][col] == '.') continue;
                if (seen.contains(board[row][col])) return false;
                seen.add(board[row][col]);
            }
        }

        return true;
    }
}
