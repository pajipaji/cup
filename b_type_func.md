# 基本数据类型 & 复合数据类型

使用 math.MaxFloat32等方法检查是否溢出

//运算符  左上 > 右下
// *      /      %      <<       >>    &  &^
// +      -      |      ^
// ==     !=     <      <=       >      >=
// &&
// ||

// 「%取模运算符的符号和被取模数的符号总是一致的」
//左优先结合规则，括号提升优先级
&      位运算 AND
|      位运算 OR
^      位运算 XOR
&^     位清空 (AND NOT)
<<     左移
>>     右移

//基本数据类型
//整型 0
有符号整数: int8、int16、int32、int64   值域: $-2^{n-1}$到$2^{n-1}-1$
无符号整数: uint8、uint16、uint32、uint64   值域: 0到$2^n-1$

//浮点型 0.0「浮点数的范围极限值可以在math包找到」
有符号浮点数: float32、float64  值域: math.MaxFloat32 是 3.4e38; math.MaxFloat64是1.8e308; 最小值近似为1.4e-45和4.9e-324
「一个float32类型的浮点数可以提供大约6个十进制数的精度，而float64则可以提供约15个十进制数的精度」

//复数 「内置的complex函数用于构建复数，内建的real和imag函数分别返回复数的实部和虚部」
复数类型: complex64、complex128
var x complex128 = complex(1, 2)
x := 1 + 2i

//布尔型 false
取值: true、false  不可使用0/1代替true/false

//字符串 ""
string

//常量
const xxx xxx

//复合数据类型 拓展写
//数组
//slice
//map
//结构体
//json
//文本和HTML模版
