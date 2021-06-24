package main

import "fmt"

type Animal struct {
	name   string
	sexual string
	legs   int
}

func (a *Animal) Eat() string {
	return fmt.Sprintf("%s is eatting", a.name)
}

func (a *Animal) Sleep() string {
	return fmt.Sprintf("%s is sleeping", a.name)
}

type Dog struct {
	Animal
}

func (a *Dog) Eat() string {
	return fmt.Sprintf("Dog %s is eatting", a.name)
}

func main() {
	a := Animal{
		name:   "alice",
		sexual: "female",
		legs:   2,
	}
	d := Dog{
		Animal: a,
	}
	fmt.Println(d)
	fmt.Println(d.Eat())
}
