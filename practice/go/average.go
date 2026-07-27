package main

import "fmt"

func main() {
    numbers := []float64{10, 20, 30, 40}
    sum := 0.0
    for _, n := range numbers {
        sum += n
    }
    fmt.Println("average:", sum/float64(len(numbers)))
}

