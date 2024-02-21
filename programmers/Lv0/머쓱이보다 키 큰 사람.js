function solution(array, height) {
  var c = 0;
  for(var i=0;i<array.length;i++){
    if(array[i] > height){
      c += 1;
    }
  }

  return c;
}