package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func main() {
	part1()
}

func part1() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	reId := regexp.MustCompile(`^Game (\d*):(.*)$`)
	reSets := regexp.MustCompile(`([^;]*);?`)
	reRed := regexp.MustCompile(`(\d*) red`)
	reBlue := regexp.MustCompile(`(\d*) blue`)
	reGreen := regexp.MustCompile(`(\d*) green`)

	sets := make(map[int]map[int]map[string]int)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lineMatches := reId.FindAllStringSubmatch(scanner.Text(), -1)
		idStr, setsStr := lineMatches[0][1], lineMatches[0][2]

		id, _ := strconv.Atoi(idStr)
		sets[id] = make(map[int]map[string]int)

		setsMatches := reSets.FindAllStringSubmatch(setsStr, -1)
		for setNo, setStr := range setsMatches {

			redMatches := reRed.FindAllStringSubmatch(setStr[1], -1)
			blueMatches := reBlue.FindAllStringSubmatch(setStr[1], -1)
			greenMatches := reGreen.FindAllStringSubmatch(setStr[1], -1)

			red, blue, green := 0, 0, 0
			if redMatches != nil {
				red, _ = strconv.Atoi(redMatches[0][1])
			}
			if blueMatches != nil {
				blue, _ = strconv.Atoi(blueMatches[0][1])
			}
			if greenMatches != nil {
				green, _ = strconv.Atoi(greenMatches[0][1])
			}
			sets[id][setNo] = map[string]int{
				"red":   red,
				"blue":  blue,
				"green": green,
			}
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

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

	fmt.Println(sum)
}
