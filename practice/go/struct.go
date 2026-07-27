package main

import "fmt"

type Book struct {
    Title string
    Pages int
}

func main() {
    book := Book{Title: "Go Basics", Pages: 200}
    fmt.Printf("%s has %d pages\n", book.Title, book.Pages)
}

