package day02

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func Run() {
	sol1, sol2 := getSolution()

	res1 := part1()
	res2 := part2()

	fmt.Printf("Part 1: %d (should be %d)\n", res1, sol1)
	fmt.Printf("Part 2: %d (should be %d)\n", res2, sol2)
}

func getSolution() (int, int) {
	file, err := os.Open("solution.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	scanner.Scan()
	sol1, _ := strconv.Atoi(scanner.Text())

	scanner.Scan()
	sol2, _ := strconv.Atoi(scanner.Text())

	return sol1, sol2
}

func part1() int {
	sets := readGames()
	maxRed, maxGreen, maxBlue := 12, 13, 14
	impossibleIds := make(map[int]bool)

	for id, sets := range sets {
		for _, set := range sets {
			red, blue, green := set["red"], set["blue"], set["green"]
			if red > maxRed || blue > maxBlue || green > maxGreen {
				impossibleIds[id] = true
				break
			}
		}
	}

	sum := 0
	for id := range sets {
		if !impossibleIds[id] {
			sum += id
		}
	}

	return sum
}

func part2() int {
	games := readGames()
	powers := make(map[int]int)

	for game, sets := range games {
		minRed, minGreen, minBlue := 0, 0, 0
		for _, set := range sets {
			red, blue, green := set["red"], set["blue"], set["green"]
			if red > minRed {
				minRed = red
			}
			if blue > minBlue {
				minBlue = blue
			}
			if green > minGreen {
				minGreen = green
			}
		}
		powers[game] = minRed * minBlue * minGreen
	}

	sumPowers := 0
	for _, power := range powers {
		sumPowers += power
	}

	return sumPowers
}

func readGames() map[int]map[int]map[string]int {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	reId := regexp.MustCompile(`^Game (\d*):(.*)$`)
	reSets := regexp.MustCompile(`([^;]*);?`)

	sets := make(map[int]map[int]map[string]int)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lineMatches := reId.FindAllStringSubmatch(scanner.Text(), -1)
		idStr, setsStr := lineMatches[0][1], lineMatches[0][2]

		id, _ := strconv.Atoi(idStr)
		sets[id] = make(map[int]map[string]int)

		setsMatches := reSets.FindAllStringSubmatch(setsStr, -1)
		for setNo, setStr := range setsMatches {
			sets[id][setNo] = map[string]int{
				"red":   countCubes("red", setStr[1]),
				"blue":  countCubes("blue", setStr[1]),
				"green": countCubes("green", setStr[1]),
			}
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return sets
}

func countCubes(color, results string) int {
	re := regexp.MustCompile(`(\d*) ` + color)
	matches := re.FindAllStringSubmatch(results, -1)
	if matches != nil {
		count, _ := strconv.Atoi(matches[0][1])
		return count
	} else {
		return 0
	}
}
