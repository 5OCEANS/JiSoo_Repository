function solution(numbers) {
  const answer = numbers
    .map((n) => String(n))
    .sort((a, b) => b + a - (a + b))
    // ['6', '10', '2']라면 106-610은 음수라서 순서 바뀌지 X
    //['6', '2', '10']로 정렬되면 join으로 "6210" 만들어 출력
    .join("");
  return answer[0] === "0" ? "0" : answer;
}
