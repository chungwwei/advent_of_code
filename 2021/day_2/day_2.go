package main

import (
	"fmt"
	"os"
	"strconv"
	"bufio"
	"strings"
);

func main() {
	path := "./day_2.txt"
	arr := readLines(path)

	fmt.Println("--- Part One ---")
	fmt.Println(f(arr))

	fmt.Println("--- Part Two ---")
	fmt.Println(f2(arr))
}


func f(arr []string) int {
	depth, horizontal := 0, 0
	for _, instruction := range arr {
		ins := strings.Split(instruction, " ")
		command := ins[0]
		unit := toInt(ins[1])

		switch command {
		case "forward":
			horizontal += unit
			break
		case "down":
			depth += unit
		case "up":
			depth -= unit
		default:
			// empty
		}

	}
	return depth * horizontal
}


func f2(arr []string) int {
	depth, horizontal, aim := 0, 0, 0
	for _, instruction := range arr {
		ins := strings.Split(instruction, " ")
		command := ins[0]
		unit := toInt(ins[1])

		switch command {
		case "forward":
			horizontal += unit
			depth += aim * unit
		case "down":
			aim += unit
		case "up":
			aim -= unit
		default:
			// empty
		}

	}
	return depth * horizontal
}


func readLines(filename string) []string {
	file, err := os.Open(filename)
	check(err)
	defer file.Close()

	Scanner := bufio.NewScanner(file)

	var lines []string
	for Scanner.Scan() {
		lines = append(lines, Scanner.Text())
	}
	return lines
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