// contribution 6
package main

import "fmt"

type Speaker interface {
    Speak() string
}

type Cat struct{}

func (c Cat) Speak() string { return "meow" }

func main() {
    var s Speaker = Cat{}
    fmt.Println(s.Speak())
}


