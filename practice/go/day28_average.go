package main

import "fmt"

func main() {
    nums := []float64{5, 10, 15}
    sum := 0.0
    for _, n := range nums {
        sum += n
    }
    fmt.Println(sum / float64(len(nums)))
}

