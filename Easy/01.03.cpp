#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string replaceSpaces(string S, int length) {
        std::string result;
        int len = 0;
        for (char c : S) {
            if (len<length){
                if (c == ' ') result.append("%20");
                else result.push_back(c);
                len++;
            }
            else break;
        }
        return result;
    }
};

int main(){
    Solution test;
    std::cout << test.replaceSpaces("Mr John Smith    ",13) << std::endl;
    return 0;
}