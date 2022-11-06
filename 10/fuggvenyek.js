function demo(){
    console.log("Elso fuggvenyem JS-ben");
}

// fuggvenyhivas
demo();

function koszones(nev){
    console.log("Szia, " + nev);
}

koszones("Béla");
koszones();
koszones("Karcsi", "Laci") // a felesleges paraméterekt figyelmen kívül hagyjuk

function koszones2(nev){
    if (nev === undefined){
        console.log("Nem tudom ki vagy :(");
        return;
    }
    console.log("Szia, " + nev);
}
koszones2()

// default paraméter
function koszonoes3(nev="Idegen"){
    console.log("Szia, " + nev)
}
koszonoes3()

// callback fgv-ek
function osszead(a, b){
    return a+b;
}

function kivon(a, b){
    return a-b;
}

function muvelet(fgv, a, b){
    if (typeof fgv === "function"){
        return fgv(a,b);
    }
    console.log("Nem fuggvenyt adtal meg");
}

console.log(muvelet(kivon, 10, 5));
console.log(muvelet(osszead, 10, 5));
muvelet("valami", 10, 5);

// egyéb megadási módok
// anonim fgv
let hatvany = function (a, k) {return a**k;}
console.log(hatvany(2, 6));

// arrow functon
let ping = () => {console.log("PING!");}
let gyok = a => {return a**0.5;}
let szoroz = (a, b) => {return a*b;}

ping()
console.log(gyok(9))
console.log(szoroz(7,9))