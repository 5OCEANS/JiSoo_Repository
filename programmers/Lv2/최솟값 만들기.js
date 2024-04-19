function solution(A, B) {
  // A의 가장 높은 수와 B의 가장 낮은 수를 곱해야 가장 낮은 곱셈 가능
  // A는 오름차순, B는 내림차순 정렬
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);

  return A.reduce((a, b, i) => (a += b * B[i]), 0);
  // a는 누적된 값
  // A의 요소 b와 B에서 동일 인덱스 i의 요소를 곱해준다
  // 0은 초기값으로 사용되고 초기 누적값이 된다
}
