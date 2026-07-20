// Last updated: 20/07/2026, 18:40:45
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>(); 
        for (char c : s.toCharArray()) { 
            if (c == '(') 
                stack.push(')'); 
            else if (c == '{') 
                stack.push('}');
            else if (c == '[')
                stack.push(']'); 
            else if (stack.isEmpty() || stack.pop() != c) 
               
                
                return false;
        }
        
           return stack.isEmpty();
    }
}