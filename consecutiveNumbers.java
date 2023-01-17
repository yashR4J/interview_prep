class Solution {
    public int consecutiveNumbersSum(int n) {
        int count=0;
        for(int i=1;i*(i+1)/2<=n;i++){
            if(i%2!=0){
                //odd
                if(n%i==0)
                    count++;
            }
            else{
                //even
                double res= 1.0*n/i;
                int IntPart = (int) res;
                if(res-IntPart==0.5)
                    count++;
            }
        }
        return count;
    }
}