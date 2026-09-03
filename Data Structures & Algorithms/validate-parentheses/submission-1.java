class Solution {
    public boolean isValid(String s) {
        // make a stack to make sure everytime you open one you are closing
        
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            
            if (s.charAt(i) == '(') {
                stack.push(')');
                continue;
            } else if (s.charAt(i) == '[') {
                stack.push(']');
                continue;
            } else if (s.charAt(i) == '{') {
                stack.push('}');
                continue;
            }

            if (stack.isEmpty() || s.charAt(i) != stack.peek()) {
                return false;
            }

            stack.pop();
            

        }

        return stack.isEmpty();

    }
}
