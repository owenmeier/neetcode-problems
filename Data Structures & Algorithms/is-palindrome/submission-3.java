class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder reverse = new StringBuilder();

        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        char[] string = s.toCharArray();

        int left = 0;
        int right = string.length - 1;

        while (left < right) {
            if (string[left] == string[right]) {
                left++; right--;
                continue;
            }
            else return false;
        }
        return true;

        // for (int i = s.length() - 1; i >= 0; i--) {
        //     reverse.append(s.charAt(i));
        // }

        // // reverse.toString().toLowerCase();
        // // System.out.println(s);
        // // System.out.println(reverse);
        // return reverse.toString().toLowerCase().equals(s);
    }
}
