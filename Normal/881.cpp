#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        int boat = 0;
        sort(people.begin(),people.end());
        auto low = people.begin();
        auto high = people.end() - 1;

        while(high>=low){
            if (*low <= (limit - *high)){
                ++low;
            }
            ++boat;
            --high;
        }
        return boat;
    }
};


int main() {
    Solution sol;
    std::vector<int> arr = {3,5,3,4};
    cout<<sol.numRescueBoats(arr,5)<<endl;
    return 0;
}