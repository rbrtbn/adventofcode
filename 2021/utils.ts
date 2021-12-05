import fetch from "node-fetch";

export const fetchInput = async (day : string|number) => {
    const response = await fetch(`https://adventofcode.com/2021/day/${day}/input`, {
        "headers": {
          "cookie": "session=53616c7465645f5fe353480ecb925afa7dafde0c116d1fffd4081bfe4f444784aabbf7f9a7d1ed9bf8d5e76361de0551"
        },
      });
      
    return await response.text();
}