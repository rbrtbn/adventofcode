package day01

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func Part1() {
	file, err := os.Open("day01/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	calibration := 0
	scanner := bufio.NewScanner(file)
	reDigit := regexp.MustCompile(`\d`)
	for scanner.Scan() {
		txt := scanner.Text()
		digits := reDigit.FindAllString(txt, -1)

		if len(digits) >= 1 {
			firstDigit, _ := strconv.Atoi(digits[0])
			lastDigit, _ := strconv.Atoi(digits[len(digits)-1])

			calibration += 10*firstDigit + lastDigit
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(calibration)
}
