function solution(ingredient) {
  var answer = 0;
  for (let i = 3; i < ingredient.length; i++) {
    const n = ingredient[i];
    if (
      n === 1 && // 현재 재료가 빵
      ingredient[i - 1] === 3 && // 이전 재료가 고기
      ingredient[i - 2] === 2 && // 그 이전 재료가 야채
      ingredient[i - 3] === 1 //그 이전이전 재료가 빵
    ) {
      ingredient.splice(i - 3, 4);
      answer += 1;
      i -= 4;
    }
  }
  return answer;
}
