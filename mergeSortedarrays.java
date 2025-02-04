class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int num3[] = new int[m + n];
        int i = 0, j = 0, k = 0;
        while (i < m && j < n) {
            if (nums1[i] < nums2[j]) {
                num3[k++] = nums1[i++];
            } else if (nums1[i] > nums2[j]) {
                num3[k++] = nums2[j++];
            } else {
                num3[k++] = nums1[i++];
                num3[k++] = nums2[j++];
            }
        }
        // assign num3 to nums1
        while (i < m) {
            num3[k++] = nums1[i++];
        }
        while (j < n) {
            num3[k++] = nums2[j++];
        }
        for (int l = 0; l < num3.length; l++) {
            nums1[l] = num3[l];
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums1 = { 1, 2, 3, 0, 0, 0 };
        int[] nums2 = { 2, 5, 6 };
        s.merge(nums1, 3, nums2, 3);
        for (int i = 0; i < nums1.length; i++) {
            System.out.println(nums1[i]);
        }
    }
}