// Last updated: 6/12/2025, 8:28:23 PM
#include <bits/stdc++.h>
class Solution {
public:
    int romanToInt(string s) {
    unordered_map<char, int> dict;
    dict['I'] = 1;
    dict['V'] = 5;
    dict['X'] = 10;
    dict['L'] = 50;
    dict['C'] = 100;
    dict['D'] = 500;
    dict['M'] = 1000;
    int n=s.length();
    int result=0;

    for (int i=0;i<n;i++)
    {
        if (i+1<n && dict[s[i]] < dict[s[i+1]])
        {
            result-=dict[s[i]];
            continue;
        }
        result+=dict[s[i]];
    }
    return result;



    }
};