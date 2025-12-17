class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        vector<int> counts(100, 0);
        for (auto& n: nums) {
            ++counts[n - 1];
        }

        int result = 0;
        for (auto i = 0; i < 100; ++i) {
            if (counts[i] == 1) {
                result += (i + 1);
            }
        }

        return result;
    }
};