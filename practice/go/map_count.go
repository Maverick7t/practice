package main

import "fmt"

func main() {
    counts := map[string]int{"apple": 2, "banana": 3, "cherry": 1}
    total := 0
    for _, value := range counts {
        total += value
    }
    fmt.Println("total items:", total)
}

