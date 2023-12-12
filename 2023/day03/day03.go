package day03

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

type part struct {
	isSymbol bool
	isNumber bool
	number   int
	position int
}

func Part1(input string) int {
	engine := parseInput(input)

	sum := 0
	for _, parts := range engine {
		for _, part := range parts {
			if part.isNumber && part.position == 0 {
				sum += part.number
			}
		}
	}

	return sum
}

func Part2(input string) int {
	engine := parseInput(input)

	sum := 0
	for i, parts := range engine {
		for j, part := range parts {
			if part.isSymbol {
				sum += i + j
				// neighbours := getNeighbours(parts, i, j)
				// if len(neighbours) > 0 {
				// 	min := neighbours[0][0]
				// 	for _, neighbour := range neighbours {
				// 		if neighbour[0] < min {
				// 			min = neighbour[0]
				// 		}
				// 	}
				// 	parts[i][j][0] = min
				// }
			}
		}
	}

	fmt.Println(engine)

	return sum
}

func parseInput(input string) [][]part {
	lines := strings.Split(input, "\n")
	lines = lines[:len(lines)-1]

	engine := make([][]part, len(lines))
	for i, line := range lines {
		engine[i] = make([]part, len(line))
		for j, char := range line {
			if isSymbol(char) {
				engine[i][j] = part{true, false, 0, 0}
			}
		}
	}

	for i, line := range lines {
		numStr := ""
		for j, char := range line {
			if isNumber(char) {
				numStr += string(char)
			} else {
				engine = storePartNumber(engine, i, j, numStr)
				numStr = ""
			}
		}
		if numStr != "" {
			engine = storePartNumber(engine, i, len(line), numStr)
		}
	}

	return engine
}

func storePartNumber(engine [][]part, i, j int, numStr string) [][]part {
	jMin, jMax := j-len(numStr), j
	if isPartNumber(engine, i, jMin, jMax) {
		partNumber, _ := strconv.Atoi(numStr)

		for k := j - 1; k > j-len(numStr)-1; k-- {
			engine[i][k] = part{false, true, partNumber, k - j + len(numStr)}
		}
	}

	return engine
}

func isPartNumber(engine [][]part, i, jMin, jMax int) bool {
	for j := jMin; j < jMax; j++ {
		for ii := i - 1; ii <= i+1; ii++ {
			for jj := j - 1; jj <= j+1; jj++ {
				if ii >= 0 && ii <= len(engine)-1 && jj >= 0 && jj <= len(engine[0])-1 && engine[ii][jj].isSymbol {
					return true
				}
			}
		}
	}

	return false
}

func isNumber(symbol rune) bool {
	return regexp.MustCompile(`\d`).MatchString(string(symbol))
}

func isSymbol(symbol rune) bool {
	return symbol != '.' && !isNumber(symbol)
}
