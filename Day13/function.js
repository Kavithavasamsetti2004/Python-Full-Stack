 // Named function

function add(x,y)
{
    return x+y
}
s = add(5,8)
console.log(s)

// Function Expressions

const square = function(x){
    return x**2
}
k = square(4)
console.log(k)

// Arrow functions 

const cube = (m)=>{
    return m**3
}
c = cube(5)
console.log(c)

//linear 

const cub = (m)=> m**3
t = cub(2)
console.log(t)

// Call Back function

const greet = (n,callback)=>{
    console.log("hello",n)
    callback();
}
greet("Kavitha",()=>console.log("hai"))