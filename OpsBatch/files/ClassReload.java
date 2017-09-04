package com.fatman.hello;

/**
 * Created by test on 2017/2/7.
 * 1、方法重载的Demo，如本类的方法 attack
 * 2、简化attack类，使用操作数组的方法
 */
public class ClassReload extends Hero{
    public void attack(){
        System.out.println(name + " 进行了一次攻击 ，但是不确定打中谁了"); //name的属性在Hero类中定义
    }

    public void attack(Hero h1) {
        System.out.println(name + " 进行了一次攻击打中了" + h1.name);
    }

    public void attack(Hero h1,Hero h2) {
        System.out.println(name + " 同时对" + h1.name + " " + h2.name + "进行了攻击");
    }

    public void attackJianHua(Hero ... heroes) {
        for (int i = 0; i < heroes.length; i++) {
            System.out.println(name + "攻击了" + " " + heroes[i].name);
        }
    }

    public static void main (String[] args) {
        ClassReload classReload = new ClassReload(); //实例化当前类
        classReload.name = "赏金猎人";                 //为从父类继承的name属性赋值

        ClassReload classReload1 = new ClassReload();
        classReload1.name = "盖伦";

        ClassReload classReload2 = new ClassReload();
        classReload2.name = "提莫";

        classReload.attack();
        classReload.attack(classReload1);
        classReload.attack(classReload1,classReload2);
        classReload.attackJianHua(classReload1,classReload2);
    }
}
