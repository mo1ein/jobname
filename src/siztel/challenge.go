package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup

func main() {
	fmt.Println("hi")
	time.Sleep(1000)
	ch := make(chan int, 10)
	wg.Add(2)
	go go1(ch)
	go go2(ch)
	fmt.Println("bye")
	wg.Wait()
}

func go1(ch chan int) {
	fmt.Println("start go1")
	rand.Seed(time.Now().UnixNano())
	randNum := rand.Intn(100)
	ch <- randNum
	fmt.Println("this is goroutine 1")
	wg.Done()
}

func go2(ch chan int) {
	fmt.Println("start go2")
	data := <-ch
	fmt.Println(data)
	if data > 80 {
		fmt.Println("u r the winner")
	} else {
		fmt.Println("u r the loser")
	}
	fmt.Println("this is goroutine 2")
	wg.Done()
}
