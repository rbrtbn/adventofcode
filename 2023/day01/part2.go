package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func Part2() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	calibration := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		txt := scanner.Text()
		firstDigit, lastDigit := findFirstAndLastDigits(txt)

		calibration += 10*firstDigit + lastDigit
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(calibration)
}

func findFirstAndLastDigits(txt string) (int, int) {
	reFirst := regexp.MustCompile(`\d|one|two|three|four|five|six|seven|eight|nine`)
	first := reFirst.FindString(txt)

	// wow, this is ugly
	reLast := regexp.MustCompile(`\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin`)
	last := reLast.FindString(reverseString(txt))

	return digitToInt(first), digitToInt(last)
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func digitToInt(digit string) int {
	numMap := map[string]int{
		"":      0,
		"one":   1,
		"eno":   1,
		"two":   2,
		"owt":   2,
		"three": 3,
		"eerht": 3,
		"four":  4,
		"ruof":  4,
		"five":  5,
		"evif":  5,
		"six":   6,
		"xis":   6,
		"seven": 7,
		"neves": 7,
		"eight": 8,
		"thgie": 8,
		"nine":  9,
		"enin":  9,
	}

	value, ok := numMap[digit]
	if ok {
		return value
	} else {
		value, err := strconv.Atoi(digit)
		if err != nil {
			log.Fatal(err)
		}

		return value
	}
}
