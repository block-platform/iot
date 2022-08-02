package com.iot;

public class TestClass {

    public static void main(String[] args) throws Exception {
        FabricClass fc1 = new FabricClass();
        System.out.println(fc1.pushIPFSHashToFabric(args[0], args[1]));
    }
}
