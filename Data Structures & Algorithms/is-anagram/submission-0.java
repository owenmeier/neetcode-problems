class Solution {
    public boolean isAnagram(String s, String t) {
        int[] counts = new int[26];

        for (int i = 0; i < s.length(); i++) {
            int index = s.charAt(i) - 'a';
            counts[index]++;
        }

        for (int i = 0; i < t.length(); i++) {
            int index = t.charAt(i) - 'a';
            counts[index]--;
        }

        
        for (int i = 0; i < 26; i++) {
            if (counts[i] == 0) continue;
            return false;
        }
        return true;
    }
}
