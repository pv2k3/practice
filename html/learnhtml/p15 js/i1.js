
let a = ["Cool", "Smart", "Elegant"];
let b = ["Office", "Workplace", "Platform"];
let c = ["Product", "Item", "Produce"];

let rand = Math.random();
let first, second, third;
if(rand < 0.33){
    first = a[0];
}
else if(rand < 0.66){
    first = a[1];
}
else{
    first = a[2];
}

if(rand < 0.33){
    second = b[0];
}
else if(rand < 0.66){
    second = b[1];
}
else{
    second = b[2];
}

if(rand < 0.33){
    third = c[0];
}
else if(rand < 0.66){
    third = c[1];
}
else{
    third = c[2];
}

console.log(`${first} ${second} ${third}`);