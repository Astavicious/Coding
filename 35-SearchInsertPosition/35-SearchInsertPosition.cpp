// Last updated: 6/12/2025, 8:28:18 PM
class Solution {
public:
     int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();

        // Search for the target in the entire array.
        for (int i = 0; i < n; i++) {
            if (nums[i] == target) {
                return i;  // Target found, return its index.
            }
        }

        // If target is not found, find the insertion index.
        for (int i = 0; i < n; i++) {
            if (nums[i] > target) {
                return i;  // Insertion point is here.
            }
        }

        // If the target is larger than all elements, insert at the end.
        return n;
    }
};