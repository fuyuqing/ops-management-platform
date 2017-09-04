package com.fatman.hello;

import java.util.Scanner;

/**
 * Created by test on 2017/2/6.
 */
public class NumCalc {
    public void getNumber() {
        Scanner first = new Scanner(System.in);
        Scanner second = new Scanner(System.in);
        int numOne = first.nextInt();
        int numTwo = second.nextInt();
        int result = numOne + numTwo;
        System.out.println("result: " + (numOne + numTwo));
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        float a = s.nextFloat();
        System.out.println("args = [" + a + "]");
        NumCalc numCalc = new NumCalc();
        numCalc.getNumber();
        int i = 1;
        int z = 2;
        int y = i + z;
        System.out.println("args = [" + y + "]");

        int x = 1;
        boolean b = !(x++ == 3) ^ (x++ ==2) && (x++==3);
        /*
         * 此结果x = 3,原因分析：
         *  1、由于boolean类型的变量b所代表的后面是一个表达式，因此先计算该表达式。
         *  2、!(x++ == 3) ^ (x++ ==2) #^表示的是异或，需要两边一样才是true，不一样为false
         *     先计算x++ 是2 ，2 != 3 为false ，前面的！取反为true， 后面 x++是3，3!=2 为false
         *     所以!(x++ == 3) ^ (x++ ==2)是false，&&是逻辑短与，短与判断前面为false就不往下计算了
         *     因此后面(x++==3)不会在去计算，最后为false ， x = 3
         */
        System.out.println(b);
        System.out.println(x);

        int f = 1;
        f += f++;
        System.out.println("args = [" + f + "]");
    }
}
