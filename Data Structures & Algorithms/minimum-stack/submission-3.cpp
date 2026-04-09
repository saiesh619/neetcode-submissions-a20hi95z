class MinStack {
public:
    stack<long>minStack;
    long min ;
    MinStack() {   
    }
    
    
    void push(int val) {
     if(minStack.empty()){
        minStack.push(0) ;
        min = val ;
     }
     else{
        long top = val - min ;
        minStack.push(top);
        if(val < min){
            min = val ;
        }
     }
        
    }
    
    void pop() {
        if (minStack.empty()) return;            
        long pop = minStack.top();
        minStack.pop();
        if(pop < 0){
            min = min - pop ;
        }

        
    }
    
    int top() {
       if(minStack.top() > 0){
            return (minStack.top() + min);
       }
       else{
            return min;
       }
    }
    
    int getMin() {
        return (min);
    }
};
