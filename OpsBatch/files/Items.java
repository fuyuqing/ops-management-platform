package com.fatman.hello;

/**
 * Created by test on 2017/2/6.
 */
public class Items {
    String name; //物品名称
    int price;   //物品价格

    public static void main(String[] args) {
        Items hpbox = new Items();
        hpbox.name = "血瓶";
        hpbox.price = 50;

        Items shoes = new Items();
        shoes.name = "草鞋";
        shoes.price = 300;

        Items sword = new Items();
        sword.name = "长剑";
        sword.price = 350;
    }
}
