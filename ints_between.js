#https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/javascript
#takes two integeres and returns an array of all integers between the input parameters, including them.
function between(a, b) {
 let arr =[];
  
 for (let i = a; i <= (b); i++) {
   arr.push(i)
 }
  return arr
}
