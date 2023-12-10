package day03

import (
	"regexp"
	"strconv"
	"strings"
)

func Part1(input string) int {
	lines := strings.Split(input, "\n")
	symbols := make([][]bool, len(lines)-1)
	for i, line := range lines[:len(lines)-1] {
		symbols[i] = make([]bool, len(line))
		for j, char := range line {
			symbols[i][j] = isSymbol(char)
		}
	}

	sum := 0
	for i, line := range lines {
		lastNumber := ""
		for j, char := range line {
			if isNumber(char) {
				lastNumber += string(char)
			} else {
				jMin, jMax := j-len(lastNumber), j
				if isNumberNextToSymbol(symbols, i, jMin, jMax) {
					number, _ := strconv.Atoi(lastNumber)
					sum += number
				}
				lastNumber = ""
			}
		}
		if lastNumber != "" {
			jMin, jMax := len(line)-len(lastNumber), len(line)
			if isNumberNextToSymbol(symbols, i, jMin, jMax) {
				number, _ := strconv.Atoi(lastNumber)
				sum += number
			}
		}
	}

	return sum
}

func Part2(input string) int {
	return 0
}

func isSymbol(symbol rune) bool {
	reNotSymbol := regexp.MustCompile(`\d|\.`)
	return !reNotSymbol.MatchString(string(symbol))
}

func isNumber(symbol rune) bool {
	reNumber := regexp.MustCompile(`\d`)
	return reNumber.MatchString(string(symbol))
}

func isNumberNextToSymbol(symbols [][]bool, i, jMin, jMax int) bool {
	for j := jMin; j < jMax; j++ {
		if isNextToSymbol(symbols, i, j) {
			return true
		}
	}

	return false
}

func isNextToSymbol(symbols [][]bool, i, j int) bool {
	for ii := i - 1; ii <= i+1; ii++ {
		for jj := j - 1; jj <= j+1; jj++ {
			if ii >= 0 && ii <= len(symbols)-1 && jj >= 0 && jj <= len(symbols[0])-1 && symbols[ii][jj] {
				return true
			}
		}
	}

	return false
}
