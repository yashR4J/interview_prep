public class BalancedPartition {
    public static boolean findBalancePartition(int[] a){
        // Calculate the sum
        int sum = 0;
        for (int i = 0; i < a.length; i++)
            sum += a[i];
        
        if (sum % 2 == 1) {
            return false;
        }

        sum /= 2;

        // leave extra row and column for empty subset and sum == 0
        boolean dp[][] = new boolean[a.length + 1][sum];

        // all elements can form an empty set
        for (int i = 0; i <= a.length; i++)
            dp[i][0] = true;
        
        // all sums other than 0 are not possible with an empty set
        for (int i = 1; i <= a.length; i++)
            dp[0][i] = false;
        
        for (int i = 1; i <= a.length; i++) {
            for (int j = 1; j <= sum; j++) {
                // excluding element i 
                dp[i][j] = dp[i-1][j];

                // including element i (if element i is added, the sum is going to decrease but we want it to be positive)
                if (j - a[i-1] >= 0) {
                    dp[i][j] |= dp[i-1][j - a[i - 1]];
                }
            }
        }

        return dp[a.length][sum];
        // int diff = Integer.MAX_VALUE;
        // for (int x = sum/2; x >= 0; x--) {
        //     if (dp[a.length][x] == true) {
        //         diff = (sum - x) - x;
        //         break;
        //     }
        // }

        // return diff;
    }

    public static void main(String[] args) {
        int[] a = new int[]{1, 4, 6, 10};
        assert BalancedPartition.findBalancePartition(a) == false;
        a = new int[]{9,4,2,3,4};
        assert BalancedPartition.findBalancePartition(a) == true;
        a = new int[]{100,200,300,400,200,300,400,500};
        assert BalancedPartition.findBalancePartition(a) == true;
        System.out.println("SUCCESS");
    }
}