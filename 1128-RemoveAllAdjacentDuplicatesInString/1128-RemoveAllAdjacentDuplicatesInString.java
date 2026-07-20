// Last updated: 20/07/2026, 18:38:09

class Solution {
    public String removeDuplicates(String s) {
        
        StringBuilder result = new StringBuilder();

        
        for (char c : s.toCharArray()) {
           
            if (result.length() > 0 && result.charAt(result.length() - 1) == c) {
                result.deleteCharAt(result.length() - 1);
            } else {
               
                result.append(c);
            }
        }

        
        return result.toString();
    }
}
