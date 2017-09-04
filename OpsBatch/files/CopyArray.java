package com.fatman.hello;

/**
 * Created by test on 2017/2/7.
 */
public class CopyArray {
    public static void main(String[] args) {
        /**
         *   System.arraycopy(src, srcPos, dest, destPos, length)
         *   src: 源数组
         *   srcPos: 从源数组复制数据的启始位置
         *   dest: 目标数组
         *   destPos: 复制到目标数组的启始位置
         *   length: 复制的长度
         */
        int[] src = new int[5];
        int[] des = new int[6];

        CopyArray copyarr = new CopyArray();
        copyarr.cycleDefine(src);
/**        for (int i : src) {
 *           System.out.println(i);
 *       }
 *
        for (int i = 0; i < src.length; i++) {
            des[i] = src[i];
        }
*/
        System.arraycopy(src,0,des,0,5);

        for (int i : des) {
            System.out.println(i);
        }
    }

    public void cycleDefine(int[] array) {
        /**
         * 执行列表的赋值操作
         */
        for (int i = 0; i < array.length; i++) {
            array[i] = (int) (Math.random()*100);
        }
    }
}
