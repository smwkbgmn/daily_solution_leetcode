
class Solution {
	public:
		bool judgeSquareSum(int);
};
bool Solution::judgeSquareSum(int c) {
	long long pow_a;
	for (long long a = 0; (pow_a = a * a) <= c; ++a) {
		double sqrt_rval = std::sqrt(c - pow_a);

		if (sqrt_rval == static_cast<int>(sqrt_rval)) return true;
	}
	return false;
}