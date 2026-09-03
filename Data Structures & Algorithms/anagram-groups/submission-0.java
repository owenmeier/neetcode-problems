class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // need a map that takes the strings as values
        // and frequency count array as keys
        Map<List<Integer>, List<String>> map = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            int[] counts = new int[26];
            for (int j = 0; j < strs[i].length(); j++) {
                int index = strs[i].charAt(j) - 'a';
                counts[index]++;
            }

            List<Integer> key = new ArrayList<>();
            for (int val : counts) {
                key.add(val);
            }

            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }

            map.get(key).add(strs[i]);
        }

        return new ArrayList<>(map.values());
    }
}
