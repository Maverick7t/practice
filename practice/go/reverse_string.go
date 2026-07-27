package main

import (
    "fmt"
    "strings"
)

func main() {
    word := "golang"
    var reversed strings.Builder
    for i := len(word) - 1; i >= 0; i-- {
        reversed.WriteByte(word[i])
    }
    fmt.Println(reversed.String())
}

