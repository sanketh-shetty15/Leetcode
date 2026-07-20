// Last updated: 20/07/2026, 18:40:10
class Solution {
    public int lengthOfLastWord(String s)
     {
        String str=s.trim();
        int count=0;
        for(int i=str.length()-1;i>=0;i--)
        {
            if(str.charAt(i)!=' ')
            {
                count=count+1;
            }
            else
            {
                break;
            }
        }
        return count;
        
    }

public static void main(String args[])
{
    Solution solution=new Solution();
    String str="Hello World";
    System.out.println(solution.lengthOfLastWord(str));
}
}