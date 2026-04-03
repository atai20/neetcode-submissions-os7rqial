class Solution {
public:
    bool isValid(string s) {
        bool a;
        bool b;
        bool c;
        vector<char> stack1;
        for(int i = 0; i<s.size(); i++){
            if(i == 0){
                if((s[i] == '(' || s[i] == '{' || s[i] == '[')){
                    stack1.push_back(s[i]);
                }else{
                    return false;
                }
            }else{
                if((s[i] == '(' || s[i] == '{' || s[i] == '[')){
                    stack1.push_back(s[i]);
                }else{
                    if(stack1[stack1.size()-1] == '(' && s[i] == ')'){
                        stack1.pop_back();
                    }else if(stack1[stack1.size()-1] == '{' && s[i] == '}'){
                        stack1.pop_back();
                    }else if(stack1[stack1.size()-1] == '[' && s[i] == ']'){
                        stack1.pop_back();
                    }else{
                        return false;
                    }
                }
            }
            
        }
        for(int i = 0; i<stack1.size(); i++){
            cout<<stack1[i]<<" : ";
        }
        if(stack1.empty()){
            return true;
        }else{
            return false;
        }
    }
};
