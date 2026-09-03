class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();

        for (String word : strs) {
            encoded.append(word.length() + "#" +word);
        }

        System.out.println(encoded.toString());
        return encoded.toString();
    }

    public List<String> decode(String str) {
        int i = 0;
        List<String> result = new ArrayList<>();

        while (i < str.length()) {
            int delim = str.indexOf('#', i);
            // String num = ;
            // System.out.println(num);
            int length = Integer.parseInt(str.substring(i, delim));

            String word = str.substring(delim + 1, delim + 1 + length);
            result.add(word);

            i = delim + 1 + length;
        }
        

        return result;
    }
}
