// Last updated: 20/07/2026, 18:39:41
class Solution {
    public int evalRPN(String[] tokens) 
    {
         Stack<Integer> stack = new Stack<>(); 
         for(String c : tokens)
         {
            if(c.equals("+"))
            {
                stack.push(stack.pop()+stack.pop());
            }
            else if(c.equals("-"))
            {
                int s2=stack.pop();
                int s1=stack.pop();
                stack.push(s1-s2);
            }
            else if(c.equals("*"))
            {
                stack.push(stack.pop()*stack.pop());
            }
            else if(c.equals("/"))
            {
                int s2=stack.pop();
                int s1=stack.pop();
                stack.push(s1/s2);
            }
            else
            {
                stack.push(Integer.parseInt(c));
            }
            
         }
         return stack.peek();
         
         

         
        
    }
}