// szelekciós vezerles
let homerseklet = 16;
if (homerseklet > 28) {
    console.log("Meleg van");
} else if (homerseklet > 18) {
    console.log("Jo ido van");
} else {
    console.log("Hideg van");
}

let a = 2 + 2;
switch (a){
    case 3:
        console.log("Tul kicsi");
        break;
    case 4:
        console.log("Tokeletes");
        break;
    case 5:
        console.log("Tul nagy");
        break;
    // ha egyik esetre sem illeszkedünk:
    default:
        console.log("Nem ismerem ezt az erteket");
        break;
}

//ternary operator
0 == false ? console.log("2 egynelosegjelet hasznaltunk") : console.log("3 egynelosegjelet hasznaltunk");

// ismetleses vezerles

console.log("while ciklus:")
let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}

console.log("do-while ciklus:")
let j = 1;
do {
    console.log(j);
    j++;
} while (j <= 10);

console.log("for ciklus:")
for (let k = 1; k <= 10; k++) {
    console.log(k);
}
