package main

import (
	"fmt"
	"os"
	"strconv"
	"bufio"
);

func main() {
	path := "./day_1.txt"
	arr := readNumbers(path)
	fmt.Println("--- Part One ---")
	fmt.Println(f(arr))

	fmt.Println("--- Part Two ---")
	fmt.Println(f2(arr))
}


func f(arr []int) int {
	res := 0
	for i := 1; i < len(arr); i ++ {
		if arr[i] - arr[i - 1] > 0 {
			res += 1
		}
	}
	return res
}


func f2(arr []int) int {
	res := 0
	prev := 0
	s := 0
	i := 0
	size := 3

	for j, val := range arr {
		s += val
		if j - i + 1 > size {
			s -= arr[i]
			i += 1
		}

		if j - i + 1 == size {
			if s > prev && j != size - 1 {
				res += 1
			}
			prev = s
		}

	}
	return res
}


func readNumbers(filename string) []int {
	file, err := os.Open(filename)
	check(err)
	defer file.Close()

	Scanner := bufio.NewScanner(file)

	var numbers []int
	for Scanner.Scan() {
		numbers = append(numbers, toInt(Scanner.Text()))
	}
	return numbers
}


func check(err error) {
	if err != nil {
		panic(err)
	}
}


func toInt(str string) int {
	res, err := strconv.Atoi(str)
	check(err)
	return res
}