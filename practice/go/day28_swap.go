package main

import "fmt"

func swap(a, b *int) {
    *a, *b = *b, *a
}

func main() {
    x, y := 3, 7
    swap(&x, &y)
    fmt.Println(x, y)
}

