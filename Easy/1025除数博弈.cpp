#include<stdio.h>
class Solution {
public:
    bool divisorGame(int n) {
        bool win = false;
        do{
            printf("%d\n",n);
            for (int x=1;x<n;x++){
                if (n % x == 0){
                    n = n - x;
                    win = !win;
                    break;
                }
            }
            printf("%d\n",n);
        }while(n != 1);
        return win;
    }
};

int main(){
    Solution test;
    if(test.divisorGame(3))
        printf("true");
    else
        printf("false");
    return 0;
}