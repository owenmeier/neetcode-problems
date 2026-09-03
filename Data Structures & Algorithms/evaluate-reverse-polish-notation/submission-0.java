class Solution {
    public int evalRPN(String[] tokens) {
        if (tokens == null || tokens.length == 0) return 0;
        // we want to keep track of the operands we find in a stack
        // anytime we find an operand we know it will deal with i - 2 and i - 1
        // we can keep 4 lists of the operands?
        // issue arrises with keeping track of in place indices

        // uses a stack to push numbers, works because of 
        // reverse polish always deals with the two numbers right before it

        Stack<Integer> nums = new Stack<>();

        for (String t : tokens) {
            if (t.equals("+") || t.equals("-") || t.equals("*") || t.equals("/")) {
                
                int two = nums.pop();
                int one = nums.pop();

                switch(t) {
                    case "+":
                        nums.push(one + two);
                        continue;
                    case "-":
                        nums.push(one - two);
                        continue;
                    case "*":
                        nums.push(one * two);
                        continue;
                    case "/":
                        nums.push(one / two);
                        continue;
                }
            } else {
                nums.push(Integer.parseInt(t));
            }
        }

        return nums.pop();

    }
}
