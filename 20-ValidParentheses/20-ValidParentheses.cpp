// Last updated: 6/12/2025, 8:28:20 PM
class Solution {
public:
    bool isValid(string s) {
         stack<char> stack{};
         if(s.size()<2){return false;}
         
        for ( int i=0; i<s.size();i++) {
            if ((s[i]=='(') || (s[i]=='{')||(s[i]=='['))
            {
            stack.push(s[i]);
            }
        else 
        {
            if(stack.empty()){return false;}
        if((s[i]==')') && (stack.top()!='('))
        {
            return false;
        }
        if((s[i]=='}') && (stack.top()!='{'))
        {
            return false;
        }
        if((s[i]==']') && (stack.top()!='[')){
            return false;
        }
      stack.pop();
    }
        }
     return stack.empty();
    }
};