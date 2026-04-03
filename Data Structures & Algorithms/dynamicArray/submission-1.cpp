class DynamicArray {
private:
    int * my_array;
    int capacity;
    int pivot = 0;
public:

    DynamicArray(int capacity) {
        this->my_array = new int[capacity];
        this->capacity = capacity;
    }

    int get(int i) {
        return this->my_array[i];
    }

    void set(int i, int n) {
        this->my_array[i] = n;
    }

    void pushback(int n) {

        if(this->pivot>=this->capacity){
            resize();
        }
        this->my_array[this->pivot] = n;
        this->pivot++;

    }

    int popback() {
        this->pivot--;
        return this->my_array[this->pivot];
    }

    void resize() {
        this->capacity = this->capacity*2;
        int * new_array = new int[this->capacity];
        for(int i = 0; i<this->capacity; i++){
            new_array[i] = this->my_array[i];
        }
        this->my_array = new_array;
    }

    int getSize() {
        return this->pivot;
    }

    int getCapacity() {
        return this->capacity;
    }
};
