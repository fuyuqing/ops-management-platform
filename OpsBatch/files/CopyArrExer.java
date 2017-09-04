package com.fatman.hello;

/**
 * Created by test on 2017/2/7.
 */
public class CopyArrExer {
    public void arrFill(int[] array) {
        for (int i = 0; i < array.length; i++) {
            array[i] = (int) (Math.random()*100);
        }
    }

    public static void main(String[] args) {
        /**
         * 将两个随意长度的数组合并到一个数组中
         */
        int[] a = new int[5];
        int[] b = new int[6];
        int[] c = new int[a.length + b.length];

        CopyArrExer copyArrExer = new CopyArrExer();
        copyArrExer.arrFill(a);
        copyArrExer.arrFill(b);

        System.arraycopy(a,0,c,0,a.length);
        System.arraycopy(b,0,c,a.length,b.length);

        for (int i : c) {
            System.out.println(i);
        }

    }
}
