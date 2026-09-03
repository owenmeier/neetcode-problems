class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.isEmpty()) return 0;
        // char[] string = s.toCharArray();

        int left = 0;
        int right = 1;
        int max = 1;

        Set<Character> seen = new HashSet<>();

        seen.add(s.charAt(0));

        while (right < s.length()) {
            // System.out.println(right - left);
            // check if new right item is in set
            if (!seen.contains(s.charAt(right))) {
                seen.add(s.charAt(right));
                right++;
            } else {
                seen.remove(s.charAt(left));
                left++;
            }

            

            max = Math.max(max, right - left);
            // if it's not
                // add right item
                
            // if it is
                // remove left item, increment left
                // if left == right
                    // right++

            // max = max(max, right - left)

        }

        return max;


    }
}
