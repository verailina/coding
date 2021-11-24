class Solution {
public:
    
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> result;
        unordered_map <int, int> valueToIndex;
        
        for (int i = 0; i < nums.size(); i++){
            int second = target - nums[i];
            auto searchIt = valueToIndex.find(second);
            if (searchIt != valueToIndex.end()){
                if (searchIt-> second != i){
                    result = vector<int>{i, searchIt->second};
                    break;
                }
            }
            else {
                valueToIndex[nums[i]] = i;
            }
        }
        return result;
    }
    
};