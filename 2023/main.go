package main

import (
	"aoc2023/day04"
	"bufio"
	"day01"
	"day02"
	"day03"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strconv"

	"github.com/joho/godotenv"
)

func main() {
	action, day := parseArgs(os.Args[1:])

	if action == "download" {
		fetchInput(day)
	} else if action == "solve" {
		solve(day)
	}
}

func parseArgs(args []string) (string, int) {
	var action string
	var day int

	if len(args) == 1 {
		action = "solve"
		day, _ = strconv.Atoi(args[0])
	} else {
		action = args[0]
		day, _ = strconv.Atoi(args[1])
	}

	return action, day
}

func solve(day int) {
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
	case 4:
		res1 := day04.Part1()
		fmt.Println(res1)
	}
}

func readInputFile(day int) string {
	file, err := os.Open(dayPath(day) + "/input.txt")
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
	file, err := os.Open(dayPath(day) + "/solution.txt")
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

func fetchInput(day int) {
	godotenv.Load()
	url := fmt.Sprintf("https://adventofcode.com/2023/day/%d/input", day)
	sessionCookie := os.Getenv("SESSION_COOKIE")

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		log.Fatal(err)
	}

	req.Header.Set("Cookie", "session="+sessionCookie)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		log.Fatal("Unexpected status code in response:", resp.StatusCode)
	}

	file, err := os.Create(dayPath(day) + "/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	_, err = io.Copy(file, resp.Body)
	if err != nil {
		log.Fatal(err)
	}
}

func dayPath(day int) string {
	return fmt.Sprintf("day%02d", day)
}
