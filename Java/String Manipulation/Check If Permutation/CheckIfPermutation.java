import java.util.*;

class CheckIfPermutation 
{
    public static boolean checkIfPermutation(String s1, String s2) 
    {
        if (s1 == null || s2 == null) 
        {
            return false;
        }
        if (s1.length() != s2.length()) 
        {
            return false;
        }
        Map<Character, Integer> stringMap1 = new HashMap<Character, Integer>();
        Map<Character, Integer> stringMap2 = new HashMap<Character, Integer>();

        for (int i = 0; i < s1.length(); i++) 
        {
            if (!(stringMap1.containsKey(s1.charAt(i)))) 
            {
                stringMap1.put(s1.charAt(i), 1);
            } 
            else 
            {
                stringMap1.put(s1.charAt(i), stringMap1.get(s1.charAt(i)) + 1);
            }

            if (!(stringMap2.containsKey(s2.charAt(i)))) 
            {
                stringMap2.put(s2.charAt(i), 1);
            } 
            else 
            {
                stringMap2.put(s2.charAt(i), stringMap2.get(s2.charAt(i)) + 1);
            }
        }

        for (char c : stringMap1.keySet()) 
        {
            if (stringMap1.get(c) != stringMap2.get(c)) 
            {
                return false;
            }
        }

        return true;

    }
}
