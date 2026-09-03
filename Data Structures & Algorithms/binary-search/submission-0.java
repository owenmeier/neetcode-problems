class Solution {
    public int search(int[] nums, int target) {
        int lower = 0;
        int upper = nums.length - 1;
        

        while (lower <= upper) {
            int index = lower + (upper - lower) / 2;

            if (target > nums[index]) {
                lower = index + 1;
            } else if (target < nums[index]) {
                upper = index - 1;
            } else {
                return index;
            }
        }

        return -1;
    }
}
