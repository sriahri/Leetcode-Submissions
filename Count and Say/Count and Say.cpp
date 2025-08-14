class Solution {
public:
    string countAndSay(int n) {
        string s="1";
        while(--n)
        {
            string res="";
            int i=0;
            while(i<s.size())
            {
                int c=1;
                while(i+1<s.size() && s[i]==s[i+1])
                {
                    ++i;
                    ++c;
                }
                res+=to_string(c)+s[i];
                ++i;
            }
            s=res;
        }
        return s;
    }
};