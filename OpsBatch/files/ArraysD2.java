package com.fatman.hello;

import java.util.Arrays;

/**
 * Created by test on 2017/2/7.
 */
public class ArraysD2 {
    public static void fill(int[][] array) {
        /**
         * 执行赋值操作
         */
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                array[i][j] = (int) (Math.random()*100);
            }
        }
    }
    public static void sort(int[][] array) {
        /**
         * 先把二维数组使用System.arraycopy进行数组复制到一个一维数组
         * 然后使用sort进行排序
         * 最后再复制回到二维数组。
         */
        int[] a = new int[array.length * array[0].length];
        int b = 0;
        int c = 0;
        for (int i = 0; i < array.length; i++) {
            System.arraycopy(array[i],0,a,b,array[i].length);
            b += array[i].length;
        }
        Arrays.sort(a);
        System.out.println(Arrays.toString(a));
        for (int i = 0; i < array.length; i++) {
            System.arraycopy(a,c,array[i],0,array[i].length);
            c += array[i].length;
            System.out.println(Arrays.toString(array[i]));
        }
    }
    public static void main(String[] args) {
        int[][] a = new int[5][8];
        fill(a);
        sort(a);
    }
}
