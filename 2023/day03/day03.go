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
		isPartNumber := false
		for j, char := range line {
			if isNumber(char) {
				lastNumber += string(char)
				isPartNumber = isPartNumber || isNextToSymbol(symbols, i, j)
			} else {
				if isPartNumber {
					number, _ := strconv.Atoi(lastNumber)
					sum += number
				}
				lastNumber = ""
				isPartNumber = false
			}
		}
		if isPartNumber {
			number, _ := strconv.Atoi(lastNumber)
			sum += number
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

func isNextToSymbol(symbols [][]bool, i, j int) bool {
	// fmt.Println(i, j, len(symbols), len(symbols[0]))
	iHighBound := len(symbols) - 1
	jHighBound := len(symbols[0]) - 1

	return (i > 0 && symbols[i-1][j]) ||
		(i < iHighBound && symbols[i+1][j]) ||
		(j > 0 && symbols[i][j-1]) ||
		(j < jHighBound && symbols[i][j+1]) ||
		(i > 0 && j > 0 && symbols[i-1][j-1]) ||
		(i > 0 && j < jHighBound && symbols[i-1][j+1]) ||
		(i < iHighBound && j > 0 && symbols[i+1][j-1]) ||
		(i < iHighBound && j < jHighBound && symbols[i+1][j+1])
}
