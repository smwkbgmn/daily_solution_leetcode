#include <vector>
#include <algorithm>

typedef std::vector<int> vec_int_t;

class Solution {
	public:
		bool isNStraightHand(vec_int_t&, int);
};

bool Solution::isNStraightHand(vec_int_t& hand, int group_size) {
	if (hand.size() % static_cast<size_t>(group_size) != 0) return false;

	std::sort(hand.begin(), hand.end());

	while (hand.size()) {
		int min = hand.front();
		hand.erase(hand.begin());

		for (int cnt = 1; cnt < group_size; ++cnt) {
			vec_int_t::iterator next = std::upper_bound(hand.begin(), hand.end(), min);
			
			if (next == hand.end() || min + 1 != *next) return false;

			min = *next;
			hand.erase(next);
		}
	}
	return true;
}
