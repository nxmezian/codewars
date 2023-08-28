public class LoopDetection {
    public static boolean hasCycle(int[] nums) {
        int slow = 0;
        int fast = 0;

        while (fast < nums.length && nums[fast] >= 0) {
            slow = nums[slow];       // Move slow pointer
            fast = nums[nums[fast]]; // Move fast pointer

            if (slow == fast) {
                return true; // Cycle detected
            }
        }

        return false; // No cycle detected
    }

    public static void main(String[] args) {
        int[] arr1 = {2, 1, 3, 1, 100}; // Contains a cycle: 2 -> 3 -> 4 -> 2

    }
}
