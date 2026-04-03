class Solution {
private:
    vector<char> s1;
    vector<char> s2;
    vector<char> s3;
public:
    bool isPalindrome(string s) {
        for(int i = 0; i<s.size(); i++){

            if((s[i] >= 'a' && s[i] <= 'z') || isdigit(s[i]) ){
                s3.push_back(s[i]);
            }else if(((s[i] >= 'A' && s[i] <= 'Z'))){
                s3.push_back(s[i]+32);
            }
        };
   
        for(int i = 0; i<s3.size()/2; i++){
            cout<<s3[i]<<" : "<<s3[s3.size()-i-1]<<endl;
            if(s3[i] != s3[s3.size()-1-i]){
                return false;
            }
        }
        return true;

    };
};
