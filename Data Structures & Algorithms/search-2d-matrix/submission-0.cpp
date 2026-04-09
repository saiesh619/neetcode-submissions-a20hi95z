class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(int i = 0 ; i < matrix.size() ; i++){
            int start = 0 ;
            int end = matrix[0].size();
            int mid = (start+end)/2 ;
            while(start <= end){
                cout<<matrix[i][mid]<<endl;
                if(matrix[i][mid] == target){
                    return true ;
                }
                else if(matrix[i][mid] < target) {
                    start = mid + 1 ;
                }
                else if(matrix[i][mid] > target){
                    end = mid - 1 ;                     
                }
                mid = (start + end)/ 2 ;   
            }
        }
        return false ;
    }
};
