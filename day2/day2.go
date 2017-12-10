package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"os"
	"strconv"
)

func maxDiff(line []string, ans chan<- int64) {
	min, max := int64(9999999999), int64(-1)
	for _, x := range line {
		n, _ := strconv.ParseInt(x, 10, 32)
		if n < min {
			min = n
		}
		if n > max {
			max = n
		}
	}
	ans <- max - min
}

func main() {
	f, _ := os.Open("day2.txt")
	reader := csv.NewReader(bufio.NewReader(f))
	reader.Comma = '\t'

	lineAnswer := make(chan int64)
	i := 0
	for {
		line, err := reader.Read()
		if err != nil {
			break
		}
		go maxDiff(line, lineAnswer)
		i++
	}

	total := int64(0)
	for x := 0; x < i; x++ {
		total += <-lineAnswer
	}
	fmt.Println(total)
}
