package com.fatman.hello;

/**
 * Created by test on 2017/2/8.
 */
public class ConstructMethod {
    String heroName;
    float heroHP;
    float heroArmor;
    int heroMoveSpeed;
    boolean legenderaed;

    public ConstructMethod(String heroName,float heroHP,float heroArmor,int heroMoveSpeed) {
        System.out.println("heroName = [" + heroName + "], heroHP = [" + heroHP + "]," +
                " heroArmor = [" + heroArmor + "], heroMoveSpeed = [" + heroMoveSpeed + "]");
    }

    public ConstructMethod(String name,float hp,float armor,int moveSpeed,boolean legenderay) {
        heroName = name;
        heroHP = hp;
        heroArmor = armor;
        heroMoveSpeed = moveSpeed;
        legenderaed = legenderay;
    }

    public static void main(String[] args) {
        ConstructMethod constructMethod = new ConstructMethod("魔腾",
                2791.729f,220.34f,421);

        ConstructMethod constructMethod1 = new ConstructMethod("蒙多",4300.23f,
                350.23f,510,true);
    }
}