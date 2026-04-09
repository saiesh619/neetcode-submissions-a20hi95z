class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freqOfElements ;
        map<int, vector<int>> bucket;
        vector<int> res ;
        int size = nums.size() ;
        for(int i = 0 ; i < nums.size() ; i++){
            freqOfElements[nums[i]]++;
        }

        for( auto pair : freqOfElements){
            bucket[pair.second].push_back(pair.first);
        }

        while(k >0 && size >=0){
            if(bucket.find(size) != bucket.end()){                               
               vector<int> temp = bucket[size];   
                           
               for(int i = 0 ; i < temp.size() ; i++){
                    res.push_back(temp[i]); 
                    cout<<temp[i]<<" ";
               } 
               cout<<endl; 
               k = k - temp.size();               
            }
            size--;
        }
        return res ;

    }
};
