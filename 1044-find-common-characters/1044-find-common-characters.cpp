
#include <string>
#include <vector>
#include <map>

typedef std::string str_t;
typedef std::vector<str_t> vec_str_t;
typedef std::map<char, unsigned int> map_char_uint_t;

class Solution {
	public:
		vec_str_t commonChars(vec_str_t&);
};

vec_str_t
Solution::commonChars(vec_str_t& words) {
	map_char_uint_t comn;

	for (auto idx = 0; idx < words.front().length(); ++idx) {
		if (comn.find(words.front()[idx]) == comn.end()) comn.insert(std::make_pair(words.front()[idx], 1));
		else ++comn.at(words.front()[idx]);
	}

	for (auto it_words = words.begin(); it_words != words.end(); ++it_words) {
		auto it_comn = comn.begin();

		while (it_comn != comn.end()) {
			size_t appear = 0;

			for (auto idx = 0; (idx = it_words->find(it_comn->first, idx)) != str_t::npos; ++idx)
				++appear;
	
			if (appear) {
				if (appear < it_comn->second) it_comn->second = appear;
				++it_comn;
			}
			else it_comn = comn.erase(it_comn);
		}
	}

	vec_str_t rst;
	for (auto it = comn.begin(); it != comn.end(); ++it) {
		for (auto cnt = it->second; cnt > 0; --cnt) rst.push_back(str_t(1, it->first));
	}

	return rst;
}