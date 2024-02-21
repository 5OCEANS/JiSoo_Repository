function solution(array, n) {
  var c = 0;
  for(var i=0;i<array.length;i++){
    if(array[i] == n)
      c += 1;
  }

  return c;
}