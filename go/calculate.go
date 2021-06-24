package main

import "fmt"

func sumE(sum int) func(int) int {
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	pos := sumE(200)
	re := pos(200)
	fmt.Println(re)
}
