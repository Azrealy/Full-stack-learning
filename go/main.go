package main

import (
	"fmt"
)

func do(i interface{}) {
	switch v := i.(type) {
	case int:
		fmt.Println(fmt.Sprintf("Int type %v", v))
	case string:
		fmt.Println(fmt.Sprintf("String type of %v", v))
	default:
		fmt.Println(fmt.Sprintf("Not know the type %v", v))
	}
}

func main() {
	fmt.Println("running main")
	do(22)
	do("hello")
}
