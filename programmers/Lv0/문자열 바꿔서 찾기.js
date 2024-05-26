function solution(myString, pat) {
  for (let i = 0; i < myString.length; i++) {
    let answer = "";
    for (let j = 0; j < myString.length; j++) {
      if (myString[j] === "A") {
        answer += "B";
      } else if (myString[j] === "B") {
        answer += "A";
      }
    }
    if (answer.includes(pat)) {
      return 1;
    }
  }
  return 0;
}
