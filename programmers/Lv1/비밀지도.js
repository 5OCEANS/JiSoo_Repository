function solution(n, arr1, arr2) {
  arr1 = arr1.map((e) => e.toString(2).padStart(n, 0));
  arr2 = arr2.map((e) => e.toString(2).padStart(n, 0));

  let answer = [];
  for (let i = 0; i < n; i++) {
    answer.push([]);
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (arr1[i][j] === "1" || arr2[i][j] === "1") answer[i].push("#");
      else if (arr1[i][j] === "0" && arr2[i][j] === "0") answer[i].push(" ");
    }
  }
  return answer.map((e) => e.join(""));
}
