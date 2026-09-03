class Solution {
    public int longestConsecutive(int[] nums) {
        // int count = 0;
        // int next = Integer.MIN_VALAUE;
        int max = 0;
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            seen.add(num);
        }
        // System.out.println(seen);

        for (int num : seen) {
            // System.out.println(curr);
            if (!seen.contains(num - 1)) {

                int curr = num;
                int count = 1;

                while (seen.contains(curr + 1)) {
                    curr++;
                    count++;
                }

                max = Math.max(max, count);
            } 
            
        }
        

        return max;
    }
}
