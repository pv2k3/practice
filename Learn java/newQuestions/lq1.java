package newQuestions;
import java.util.Arrays;
public class lq1 {
    public static int minOperations(int[] nums, int k) {
        int result = 0;

        // Iterate over the bits of k from the most significant bit to the least significant bit
        for (int i = 31; i >= 0; i--) {
            int targetBit = (k >> i) & 1; // Get the i-th bit of k

            int countZeros = 0;
            int countOnes = 0;

            // Count the number of zeros and ones at the current bit position in the array
            for (int num : nums) {
                int bit = (num >> i) & 1;
                if (bit == 0) {
                    countZeros++;
                } else {
                    countOnes++;
                }
            }

            // If the target bit is 0, we need to flip the ones to make XOR equal to k
            if (targetBit == 0) {
                result += countOnes;
            } else {
                // If the target bit is 1, we need to flip the zeros to make XOR equal to k
                result += countZeros;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] nums = {2, 1, 3, 4};
        int k = 1;

        int result = minOperations(nums, k);

        System.out.println("Minimum number of operations: " + result);
    }
}
