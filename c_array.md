# 数组 直接提供顺序初始化值序列 & 指定一个索引和对应值列表的方式初始化

//定义: var varName [n]type

//直接提供顺序初始化值序列
var a [3]int
var q [3]int = [3]int{1, 2, 3}
q := [...]int{1, 2, 3}
q := [3]int{1, 2, 3}
q = [4]int{1, 2, 3, 4} //数组的长度是数组类型的一个组成部分，因此[3]int和[4]int是两种不同的数组类型

//指定一个索引和对应值列表的方式初始化
type Currency int
const (
    USD Currency = iota // 美元
    EUR                 // 欧元
    GBP                 // 英镑
    RMB                 // 人民币
)
symbol := [...]string{USD: "$", EUR: "€", GBP: "￡", RMB: "￥"}
fmt.Println(RMB, symbol[RMB]) // "3 ￥"  RMB代表了3 指定索引, 初始化赋值

//初始化
r := [...]int{99: -1} //定义了一个含有100个元素的数组r，最后一个元素被初始化为-1，其它元素都是用0初始化

//比较 「只有当两个数组的所有元素都是相等的时候数组才是相等的」「直接可以使用 `==` 或 `!=` 进行比较，但不可以使用 `<` 或 `>`」
a := [2]int{1, 2}
b := [...]int{1, 2}
c := [2]int{1, 3}
fmt.Println(a == b, a == c, b == c) // "true false false"
d := [3]int{1, 2}
fmt.Println(a == d) // compile error: cannot compare [2]int == [3]int
