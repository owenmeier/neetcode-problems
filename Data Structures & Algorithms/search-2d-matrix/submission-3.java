class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int lower = 0;
        int upper = matrix.length - 1;

        while (lower <= upper) {
            int index = lower + (upper - lower) / 2;
            if (target < matrix[index][0]) {
                upper = index - 1;
                continue;
            } else if (target > matrix[index][matrix[index].length - 1]) {
                lower = index + 1;
                continue;
            } else {
                int low = 0;
                int high = matrix[index].length - 1;

                while (low <= high) {
                    int half = low + (high - low) / 2;
                    if (target < matrix[index][half]) {
                        high = half - 1;
                        continue;
                    } else if (target > matrix[index][half]) {
                        low = half + 1;
                        continue;
                    } else {
                        return true;
                    }
                }
                return false;
            }
        }

        return false;
    }
}
