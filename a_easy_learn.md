# easy to get

//风格和py一样 构造和c一样 随时更正

// 当前包名,c类语言只有main一个入口
package main

//引入其他包作为辅助
import "fmt"
import (
    "os"
    "fmt"
)
import std "fmt" //还可以只拿出包里的方法直接用 std.Println("hello word")

//关键字25个 简单
break      default       func     interface   select
case       defer         go       map         struct
chan       else          goto     package     switch
const      fallthrough   if       range       type
continue   for           import   return      var

//预定义的名字 「是否会常用到？？」
内建常量: true false iota nil

内建类型: int int8 int16 int32 int64
          uint uint8 uint16 uint32 uint64 uintptr
          float32 float64 complex128 complex64
          bool byte rune string error

内建函数: make len cap new append copy close delete
          complex real imag
          panic recover

//常量定义 编译替换
const xxxx xxxx
const (
    e  = 2.71828182845904523536028747135266249775724709369995957496696763
    pi = 3.14159265358979323846264338327950288419716939937510582097494459
)

//变量
var 变量名字 类型 = 表达式
i := 100

//赋值
i, j := 0, 1

//交换
i, j = j, i

//变量作用范围
在包一级声明语句声明的名字可在整个包对应的每个源文件中访问，局部声明的名字就只能在函数内部很小的范围被访问

//类型声明
Go语言主要有四种类型的声明语句：var、const、type和func，分别对应变量、常量、类型和函数实体对象的声明
type newType int //类型
type newStruct struct{} //结构体
type newInterface interface{} //接口
