#include <algorithm>
#include <bitset>
 
class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        std::sort(reservedSeats.begin(), reservedSeats.end(), [](vector<int>& a, vector<int>& b) {
           return a[0] < b[0] || (a[0] == b[0] && a[1] < b[1]);
        });

        int max = 2 * n, r = 1;

        bitset<3> avail;
        avail.set();

        for (auto& v: reservedSeats) {
            if (r != v[0]) {
                if (avail.none()) max -= 2;
                else if (!avail[0] || !avail[2]) max -= 1;

                avail.set();
                r = v[0];
            }

            if (v[1] == 1 || v[1] == 10) continue;

            int d = v[1] / 4;

            avail[d] = false;
            if (d != 0 && d != 2) {
                avail[(v[1] % 4 < 2)? 0 : 2] = false;
            }
        }

        if (avail.none()) max -= 2;
        else if (avail.count() != 3 && !avail[0] || !avail[2]) max -= 1;

        return max;
    }
};