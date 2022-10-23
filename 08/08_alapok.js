// egysoros komment
/*
    tobb
    soros
    komment
 */

console.log("Hello") // kiiratas

// Adattipusok: boolean, number, string, undefined
console.log(typeof 42);                     // tipusellenorzes: typeof
console.log(typeof 42 === "number");
console.log(typeof "hello");

// Valtozok
var valami;
console.log(valami);
{
    var egyik = 4;       // ne hasznaljuk!
    let masik = 4;
}

// console.log(egyik == masik)

const PI =3.14;
// PI = 42;             // hibas
console.log(PI);


// Tipuskonverzio
console.log("2" + 2 - "2");                 // implicit
console.log(Number("2") + 2 - "2")    // explicit

let a = Number("3.14");         // 3.14
let b = Number("101 kiskutya"); // NaN (Not a Number)
let c = parseInt(3.14);         // 3
let d = String(42);             // "42"

// number -> boolean konverzió esetén: 0 -> false, minden más -> true
let e = Boolean(0);             // false


// Operatorok
let f = 7 / 2;
console.log(f);
let g = 7 ** 2;
console.log(g);

// == vs ===
console.log(1 == true);     // !=
console.log(1 === true);    // !===