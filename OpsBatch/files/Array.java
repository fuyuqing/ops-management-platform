package com.fatman.hello;

/**
 * Created by test on 2017/2/7.
 */
public class Array {
    public static void main(String[] args) {
        int[] a;
        a = new int[5];

        a[0] = (int) (Math.random() * 100);
        a[1] = (int) (Math.random() * 100);
        a[2] = (int) (Math.random() * 100);
        a[3] = (int) (Math.random() * 100);
        a[4] = (int) (Math.random() * 100);
//      a[5] = 6;

        int z = a[0];    //初始化一个flag，值为数组的第一个值

        System.out.println("args = [" + a[0] + "]");
        System.out.println("args = [" + a.length + "]");

        for (int i = 0; i < a.length; i++) {
            System.out.println("数组中的随机数分别为：" + a[i]);
            if (a[i] < z) {
                z = a[i];  //每次循环都去和flag对比，大于则忽略，小于则替换值
            }
        }
        System.out.println("本数组中最小的值是：" + z );
    }
}
