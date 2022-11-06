let rovid_szoveg = 'Egy egyszeru szoveg ' + "meg egy egyszeru szoveg"
let hosszu_szoveg = `Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                     Sed hendrerit, quam non aliquam hendrerit, ipsum urna porttitor sem, a aliquam ex ipsum eu dui.
                     Praesent tristique vitae tortor nec luctus.`

// szovegek hossza
console.log("Valami".length); // length property segítségével

// indexelés
let suti = "dobostorta";
console.log(suti[0]);
console.log(suti[5]);
console.log(suti[suti.length-1]);
// intervallumos, negativ indexeles nem mudokdik
console.log(suti[-1]);
console.log(suti[60]);

// immutable adattipus
let demo = "fóka";
demo[0] = "r";  // nem tortenik semmi
console.log(demo)

let szoveg = "    A citromos fagyi a legjobb fagyi        ";

szoveg = szoveg.trim();     // helyközök eltávolítása a szöveg elejéről és végéről

console.log(szoveg.toLowerCase());      // kisbetűsítés
console.log(szoveg.toUpperCase());      // nagybetűsítés
console.log(szoveg.endsWith("fagyi"));  // a "fagyi" stringre végződik-e a szöveg
console.log(szoveg.substr(0, 8));       // az első 8 karakter
console.log(szoveg.replace("fagyi", "süti"));   // részstring lecserélése (csak az első előfordulást!)

if (szoveg.indexOf("fagyi") >= 0) {     // részstring előfordulásának vizsgálata
    console.log("Szerepel a szövegben fagyi!");
} else {
    console.log("A szövegben nem szerepel fagyi!");
}

const szavak = szoveg.split(" ");       // feldarabolás szóközök mentén
console.log(szavak);

// help: osszefuzogetes helyett template stringek
let nev = "Józsi", eletkor = 20, foglalkozas = "programozó";
console.log(`${nev} egy ${eletkor} éves ${foglalkozas}.`);
