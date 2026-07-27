package main

import "fmt"

func main() {
    nums := []int{2, 4, 6, 8}
    sum := 0
    for _, n := range nums {
        sum += n
    }
    fmt.Println("sum:", sum)
}

