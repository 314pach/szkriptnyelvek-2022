// letrehozas
let t1 = new Array();    // ures tomb
let t2 = [];             // ures tomb

let t3 = new Array(1,2);
let t4 = [3,4,5,6];

// tombok hossza
console.log(t4.length);

// indexeles
let sutik = ["sajttorta", "csokis keksz", "francia krémes", "banános muffin"];

console.log(sutik[0]);                        // a legelső elem
console.log(sutik[sutik.length - 1]);         // az utolsó elem
console.log(sutik[-1]);                       // ez JavaScriptben nem működik!

// mutable
sutik[1] = "isler";
console.log(sutik);

// bejárás
// index szerint
for (let i=0; i<sutik.length; i++){
    console.log(`A ${sutik[i]} finom`);
}

// listaszerű
for (let suti of sutik){
    console.log(`A ${suti} nagyon finom`);
}

// tombkezelo fuggvenyek
let bevasarlolista = ["tej", "tojás", "sajt", "üdítő"];

bevasarlolista.pop();                           // törlés a végéről
bevasarlolista.push("kenyér", "felvágott");     // beszúrás a végére
bevasarlolista.shift();                         // törlés az elejéről
bevasarlolista.unshift("kalkulus példatár");    // beszúrás az elejére

bevasarlolista.sort();                          // rendezés
let szovegkent = bevasarlolista.join("; ");     // egyesítés szöveggé
console.log("Ezeket kell megvennünk: " + szovegkent);

let fontos = bevasarlolista.slice(1, 3);        // "résztömb" lekérése
console.log("Minél hamarabb vegyük meg:");
console.log(fontos);

//bonusz replaceAll:
let szoveg = "A baraclekvár a legjobb lekvár";
szoveg = szoveg.split("lekvár").join("leves");
console.log(szoveg)