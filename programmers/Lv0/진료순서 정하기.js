function solution(emergency) {
  // 큰순으로 배열
  let a = [...emergency].sort((a,b)=>b-a);

  let b = []
  for(let i=0;i<emergency.length;i++){
    b.push(a.indexOf(emergency[i]) + 1);
  }
  
  return b;
}
