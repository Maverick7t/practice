// contribution 12
package main

import "fmt"

func main() {
    nums := []int{1, 2, 3, 4}
    sum := 0
    for _, n := range nums {
        sum += n
    }
    fmt.Println(sum)
}


