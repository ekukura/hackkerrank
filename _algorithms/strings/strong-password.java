import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the minimumNumber function below.
    /*satisfied categories is a 4 length boolean array
         0 = numbers
         1 = capitals
         2 = lowers
         3 = special chars
         
     satisfiedCategories[i] = true iff that category has been satisfied; false otherwise
     */
    static void satisfies(String c) //only should pass in here if not all categories already satisfied, 
    //e.g. at least one of elements in satisfiedCategores = 0
    {
        //the character c can only fall into one category, so if found it, then stop
        boolean foundSatisfyingCategory = false;
        int curCat = 0;
        
        while (!foundSatisfyingCategory && curCat < 4)
        {        
            if (!satisfiedCategories[curCat])
            {
                //check current category. If c is in this, change to 1 and stop
                if (c.matches(regexMatches[curCat]))
                {
                    foundSatisfyingCategory = true;
                    satisfiedCategories[curCat] = true;
                    numCategoriesSatisfied++;
                }
            }
            curCat++;
        }
    }
    // Complete the minimumNumber function below.
    static int minimumNumber(int n, String password) {
            //if n<=3, always can satisfy by adding missing length
            int res = 0;
        int missingLength = 6 - n;
        if (n <= 3)
        {
            res = missingLength;
        }
        else
        {
            // Return the minimum number of characters to make the password strong
               //abcef309ro2qVeawef39#d
                String[] passwordArr = password.split("");    
                int curIndex = 0;
                String curChar;
                
                while (numCategoriesSatisfied < 4 && curIndex < n)
                {
                    curChar = passwordArr[curIndex];     
                    satisfies(curChar); //updates the categories that are satisfied
                    curIndex++;
                }
                //System.out.printf("After index {}:\n", curIndex);
                //System.out.println(Arrays.toString(satisfiedCategories));
                
                //will always need to extend password with number
                //of unsatisfied categories, e.g. 4-numCategoriesSatified
                int missingCategories = 4-numCategoriesSatisfied;
                //if missingLength > missing Categories, need to fill in missingLength,
                //else missingCategories
                if (missingLength > missingCategories)
                    res = missingLength;
                else
                    res = missingCategories;
        }
        return res;
    }
   
    static String numbersMatch = "\\d{1}";
    static String lowerCaseMatch = "[a-z]{1}";
    static String upperCaseMatch = "[A-Z]{1}";
    static String specialCharMatch = "[-!@#$%^&*()+]{1}";
    
    static boolean[] satisfiedCategories = new boolean[4];
    static String[] regexMatches = {numbersMatch, lowerCaseMatch,
            upperCaseMatch,specialCharMatch};
    static int numCategoriesSatisfied = 0;

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String password = scanner.nextLine();

        int answer = minimumNumber(n, password);

        bufferedWriter.write(String.valueOf(answer));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

