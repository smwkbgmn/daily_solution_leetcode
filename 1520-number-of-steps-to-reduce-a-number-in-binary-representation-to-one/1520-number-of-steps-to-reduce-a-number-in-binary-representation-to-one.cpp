
#include <string>

class Solution {
	public:
		static int numSteps( std::string );
};

int Solution::numSteps( std::string str ) {
	int rst = 0;
	bool up = false;
	std::string::reverse_iterator it = str.rbegin();

	while(it != str.rend()) {
		if (!up) {
			if (it + 1 == str.rend()) break;

			if (*it == '1') {
				up = true;
				++rst;
			}
			++rst;
			++it;
		}

		else {
			if (*it == '0') {
				*it = '1';
				up = false;
			}
			else {
				++rst;
				++it;
			}
		}
	}
	return rst;
}