# python_learn_demo
pyhon study demo


break、continue和pass都是Python中的控制流语句，但它们的作用完全不同：

- break：用于终止当前循环，程序退出循环后继续执行循环后的代码
- continue：用于跳过当前循环迭代中剩余的语句，直接进入下一次迭代
- pass：空操作语句，作为占位符使用，当语法上需要语句但不需要执行任何操作时使用

需要注意的是：

- break和continue只影响内层循环，如果需要跳出外层循环，需要使用其他方法，比如标志变量
- pass在嵌套循环中同样只影响当前语句块