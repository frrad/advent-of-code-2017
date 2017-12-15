package main

import (
	"fmt"

	"gopkg.in/cheggaaa/pb.v1"
)

func generator(seed, multiple int64, filter int64, results chan<- int64) {
	value := seed

	for {
		if value%filter == 0 {
			results <- value
		}

		value *= multiple
		value %= 2147483647
	}
}

func compare(a, b int64) bool {
	ones := int64(1)<<16 - 1
	return a&ones == b&ones
}

func main() {
	length := 5000000
	count := 0

	a := make(chan int64, 100)
	b := make(chan int64, 100)

	go generator(883, 16807, 4, a)
	go generator(879, 48271, 8, b)

	bar := pb.StartNew(length)
	for i := 0; i < length; i++ {
		if compare(<-a, <-b) {
			count++
		}
		bar.Increment()
	}
	bar.FinishPrint(fmt.Sprintf("Found %d", count))
}
