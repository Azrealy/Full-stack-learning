package main

import (
	"fmt"
	"math"
)

type geometry interface {
	area() float64
	perm() float64
}

type rectangle struct {
	width, height float64
}

type circle struct {
	radius float64
}

func (r *rectangle) area() float64 {
	return r.width * r.height
}

func (r *rectangle) perm() float64 {
	return 2 * (r.width + r.height)
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c circle) perm() float64 {
	return math.Pi * c.radius * 2
}

func measure(g geometry) {
	fmt.Println(g.area())
	fmt.Println(g.perm())
}

func main() {
	r := &rectangle{width: 2.0, height: 6.0}
	measure(r)
	c := circle{3}
	measure(c)
}
