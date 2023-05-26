
// function to convert number to roman numbers

function solution(number){
  const romans = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
  };
  
  const l = number.toString().length - 1;
  let r = "";

  var divider = 10**l;

  for(var i=0; i<l; i++){
    var n = Math.trunc((number/divider));
    if (n == 0) {continue;}

    divider = divider/10;
  }

  console.log(r);
   
}

solution(301);
