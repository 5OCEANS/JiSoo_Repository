function solution(array) {
  let map = new Map();

  // map 객체 초기화
  for (let i = 0; i <= Math.max(...array); i++) {
    map.set(i, 0);
  }

  for (let i = 0; i < array.length; i++) {
    map.set(array[i], map.get(array[i]) + 1);
  }
  // map 객체의 value 모아 배열로 만들기
  let a = Array.from(map.values());

  let max = Math.max(...a);

  if (a.indexOf(max) !== a.lastIndexOf(max)) {
    return -1;
  } else {
    return a.indexOf(max);
  }
}
