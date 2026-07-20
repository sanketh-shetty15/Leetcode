// Last updated: 20/07/2026, 18:38:49
class Solution {
    public void reverseString(char[] s) {
        int n = s.length;
        for(int i=0; i<n/2; i++)
        {
            char tmp = s[i];
            s[i] = s[n-1-i];
            s[n-1-i] = tmp;
        }
        return;
    
        
    }
}