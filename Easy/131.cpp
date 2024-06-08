#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> current;
        backtrack(s, 0, current, result);
        return result;
    }

private:
    void backtrack(const string& s, int start, vector<string>& current, vector<vector<string>>& result){
        if (start == s.length()) {
            result.push_back(current);
            return;
        }

        for (int end = start; end < s.length(); ++end) {
            if (isPalindrome(s, start, end)) {
                 current.push_back(s.substr(start, end - start + 1));
                backtrack(s, end + 1, current, result);
                           current.pop_back();
            }
        }
    }

    bool isPalindrome(const string& s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            ++left;
            --right;
        }
        return true;
    }
};


int main() {
    Solution sol;
    string s = "abacccdbe";
    vector<vector<string>> result = sol.partition(s);
    
    for (const auto& vec : result) {
        cout << "[";
        for (const auto& str : vec) {
            cout << "\"" << str << "\"";
            if (&str != &vec.back()) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
    
    return 0;
}