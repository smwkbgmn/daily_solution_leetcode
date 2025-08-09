#include <string>
#include <map>

typedef std::map<char, unsigned int> map_char_uint_t;

class Solution {
	public:
		int longestPalindrome(std::string);
};

int
Solution::longestPalindrome(std::string str) {
	map_char_uint_t table;

	for (auto idx = 0; idx < str.length(); ++idx) {
		if (table.find(str[idx]) != table.end()) ++table.at(str[idx]);
		else table.insert(std::make_pair(str[idx], 1));
	}

	int rst = 0;
	bool odd = false;
	for (auto it = table.begin(); it != table.end(); ++it) {
		if (it->second & 0b1) {
			rst += (it->second - 1);
			odd = true;
		}
		else rst += it->second;
	}

	return rst + odd;
}
