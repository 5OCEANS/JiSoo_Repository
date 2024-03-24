function solution(n, lost, reserve) {
  var answer = 0;
  const uni = [];

  // 모든 학생들 체육복 수 1개로
  for (let i = 0; i < n; i++) {
    uni[i] = 1;
  }
  // 도난당한 학생의 체육복 0으로
  for (let i = 0; i < lost.length; i++) {
    uni[lost[i] - 1] = 0;
  }
  // 여벌 체육복 있는 학생 체육복 +1
  for (let i = 0; i < reserve.length; i++) {
    uni[reserve[i] - 1] += 1;
  }
  // 체육복 0개인 학생이 앞친구에게 빌려오는 경우
  for (let i = 0; i < n; i++) {
    if (uni[i - 1] === 2 && uni[i] === 0) {
      uni[i - 1] = 1;
      uni[i] = 1;
    }
    //뒷친구에게 빌려오는 경우
    else if (uni[i] === 0 && uni[i + 1] === 2) {
      uni[i] = 1;
      uni[i + 1] = 1;
    }
  }
  for (let i = 0; i < n; i++) {
    if (uni[i] > 0) {
      answer += 1;
    }
  }

  return answer;
}
