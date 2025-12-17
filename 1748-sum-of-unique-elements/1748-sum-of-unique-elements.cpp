class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        map<int, int> counts;
        for (auto& n: nums) {
            ++counts[n];
        }

        int result = 0;
        for (auto& [n, count]: counts) {
            if (count == 1) {
                result += n;
            }
        }

        return result;
    }
};