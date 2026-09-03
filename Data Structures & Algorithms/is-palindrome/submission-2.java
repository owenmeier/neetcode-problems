class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder reverse = new StringBuilder();

        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        for (int i = s.length() - 1; i >= 0; i--) {
            reverse.append(s.charAt(i));
        }

        // reverse.toString().toLowerCase();
        // System.out.println(s);
        // System.out.println(reverse);
        return reverse.toString().toLowerCase().equals(s);
    }
}
