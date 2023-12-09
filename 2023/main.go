package main

import (
	"bufio"
	"day01"
	"day02"
	"day03"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	args := os.Args[1:]

	day, _ := strconv.Atoi(args[0])

	switch day {
	case 1:
		day01.Part1()
		day01.Part2()
	case 2:
		day02.Run()
	case 3:
		input := readInputFile(day)
		sol1, sol2 := readSolutionFile(day)
		res1 := day03.Part1(input)
		res2 := day03.Part2(input)
		fmt.Println(res1, res1 == sol1)
		fmt.Println(res2, res2 == sol2)
	}
}

func readInputFile(day int) string {
	folder := fmt.Sprintf("day%02d", day)
	file, err := os.Open(folder + "/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	ret := ""
	for scanner.Scan() {
		ret += scanner.Text() + "\n"
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return ret
}

func readSolutionFile(day int) (int, int) {
	folder := fmt.Sprintf("day%02d", day)
	file, err := os.Open(folder + "/solution.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	scanner.Scan()
	sol1, _ := strconv.Atoi(scanner.Text())

	scanner.Scan()
	sol2, _ := strconv.Atoi(scanner.Text())

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return sol1, sol2
}
