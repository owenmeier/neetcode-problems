class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // keep track of how many times top k numbers appear
        // swap in a number if map value at nums[i] key is > lowest in k array
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] values = new List[nums.length + 1];
        for (int key : map.keySet()) {
            int freq = map.get(key);

            if (values[freq] == null) {
                values[freq] = new ArrayList<>();
            }

            values[freq].add(key);
        }

        int[] result = new int[k];
        int counter = 0;

        for (int i = values.length - 1; i >= 0 && counter < k; i--) {
            if (values[i] != null) {
                for (int num : values[i]) {
                    result[counter++] = num;
                    if (counter == k) break;
                }
            }
        } 

        return result;
    }
}
