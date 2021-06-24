package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	err := ioutil.WriteFile("test.txt", []byte("HELLO WORLD for write\n"), 0666)
	if err != nil {
		log.Fatal(err)
	}
	file, err := os.Open("test.txt")
	defer file.Close() // Close the file when main() function running complete.
	if err != nil {
		log.Fatal(err)
	}
	data, err := ioutil.ReadAll(file)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Data as hex: %x\n", data)
	fmt.Printf("Data as string: %s\n", data)
	fmt.Println("Number of bytes read:", len(data))
}
