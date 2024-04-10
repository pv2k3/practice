package newQuestions;
import java.util.Arrays;
import java.util.Scanner;

import static java.lang.Math.abs;

public class pr1 {
    public static void main(String[] args) {
        int[] arr1 = {87,24,43,56,33,54};
        int[] arr2 = {32,56,98,70,24};
        int len = (arr1.length+arr2.length);
        int[] arr3 = new int[len];
        int i;
        for (i=0; i < arr1.length; i++) {
            arr3[i] = arr1[i];
        }
        for (int j = 0; j < arr2.length; j++) {
            arr3[i++]  = arr2[j];
        }
        int temp = 0;
        for (int j = 0; j < arr3.length; j++) {
            for (int k = j+1; k < arr3.length; k++) {
                if(arr3[j] < arr3[k]) {
                    temp = arr3[j];
                    arr3[j] = arr3[k];
                    arr3[k] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(arr3));
    }
}
