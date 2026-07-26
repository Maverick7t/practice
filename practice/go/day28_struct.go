// contribution 11
package main

import "fmt"

type User struct {
    Name string
    Age  int
}

func main() {
    u := User{Name: "Ada", Age: 36}
    fmt.Println(u.Name, u.Age)
}


