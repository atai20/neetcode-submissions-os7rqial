class MinStack {
private:
    vector<int> stack1;
    vector<int> smallest;
    vector<int> smallest_index;
public:
    MinStack() {
        this->smallest.push_back(2147483647);
    }
    
    void push(int val) {
        this->stack1.push_back(val);
        if(this->smallest[smallest.size()-1]>val){
            this->smallest.push_back(val);
            this->smallest_index.push_back(stack1.size()-1);
            cout<<val<<endl;
        }
    }
    
    void pop() {
        if(this->stack1.size()-1 == this->smallest_index[smallest_index.size()-1]){
            this->smallest.pop_back();
            this->smallest_index.pop_back();
        }
        this->stack1.pop_back();

    }
    

    int top() {
        return this->stack1[this->stack1.size()-1];
    }
    
    int getMin() {
        return this->smallest[this->smallest.size()-1];
    }
};
