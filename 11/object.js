// letrehozas
let o1 = new Object();    // ures object
let o2 = {};              // ures object

let hallgato = {
    nev: "Kiss Béla",
    neptun: "HZD3O",
    szak: "pti",
    kki: 4.2,
    csuszik: false
};

// elemek elerese
console.log(hallgato.neptun);
console.log(hallgato["neptun"]);

// property elofordulasa
if("kki" in hallgato){
    console.log("Juhééé, van kki");
}

// ertek modositasa
hallgato["kki"] = 4.4;
console.log(hallgato);

// uj ertek par beszurasa
hallgato["osztondij"] = true;
console.log(hallgato);

// ertek par torlese
delete hallgato.kki;
console.log(hallgato);

// bejaras
// for-in
for (let kulcs in hallgato) {
    console.log(kulcs + " értéke: " + hallgato[kulcs]);
}
console.log("---")

// for-of (kulcsok)
for (let kulcs of Object.keys(hallgato)) {
    console.log(kulcs + " értéke: " + hallgato[kulcs]);
}
console.log("---")

// for-of (parok)
for (let [kulcs, ertek] of Object.entries(hallgato)) {
    console.log(kulcs + " értéke: " + ertek);
}
