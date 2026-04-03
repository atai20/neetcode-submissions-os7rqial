class LinkedList {
private:
    vector<int> my_list;
public:
    LinkedList() {
        
    }

    int get(int index) {
        if(not(index<this->my_list.size() && index>=0)){
            return -1;
        }
        return this->my_list[index];
    }

    void insertHead(int val) {
        vector<int> other;
        other.push_back(val);
        for(int i = 0; i<this->my_list.size(); i++){
            other.push_back(this->my_list[i]);
        }
        this->my_list = other;
    }
    
    void insertTail(int val) {
        this->my_list.push_back(val);

    }

    bool remove(int index) {
        vector<int> other;

        if(not(index<this->my_list.size() && index>=0)){
            return false;
        }
        

        for(int i = 0; i<index; i++){
            other.push_back(this->my_list[i]);
        }
        for(int i = index+1; i<this->my_list.size(); i++){
            other.push_back(this->my_list[i]);
        }
        this->my_list = other;
        return true;
    }

    vector<int> getValues() {
        return this->my_list;
    }
};
