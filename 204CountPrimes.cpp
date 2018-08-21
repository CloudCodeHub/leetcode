// 204 Count the number of prime numbers less than a non-negative number, n.
// Example:

// Input: 10
// Output: 4
// Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution {
public:
    int countPrimes(int n){
        if(n<=2){
            return 0; 
        }
        else {
            int m=1;
            for(int i=3;i<n;i++){
                bool flag=false;
                for(int j=2;j*j<=i;j++){
                    if(i%j==0){
                        flag=true;
                        break;
                    }
                }
                if(flag==false){
                    m++;
                }
            }
            return m;
        }
    }
};

//replace j<=sqrt(i) with j*j<=i