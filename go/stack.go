package main

import "fmt"

type stack struct {
	array []string
}

func (s *stack) push(text string) {
	s.array = append(s.array, text)
}

func (s *stack) pop() string {
	if len(s.array) > 0 {
		n := len(s.array) - 1
		text := s.array[n]
		s.array = s.array[:n]
		return fmt.Sprintln(text)
	}
	return ""
}

func main() {
	s := stack{array: []string{}}
	s.push("1")
	s.push("2")
	fmt.Println(s.pop())
	s.push("3")
	s.push("5")
	fmt.Println(s.pop())
	fmt.Println(s.array)
}
