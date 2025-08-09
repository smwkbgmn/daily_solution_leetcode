class Solution {
public:
    int heightChecker(vector<int>& heights);
};


int Solution::heightChecker(std::vector<int>& heights) {
	int rst = 0;

	std::vector<int> exp = heights;
	std::sort(exp.begin(), exp.end());
	
	for (size_t idx = 0; idx < heights.size(); ++idx)
		if (exp[idx] != heights[idx]) ++rst;

	return rst;
}
