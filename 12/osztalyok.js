class Allat{
    constructor(faj, labak_szama = 4) {
        this.faj = faj;
        this._labak_szama = labak_szama;
        this.husevo = false;
        this.kedvenc_etelek = [];
    }

    get labak_szama() {
        return this._labak_szama;
    }

    set labak_szama(ertek) {
        if(ertek >= 0 && ertek <= 100){
            this._labak_szama = ertek;
        }
    }

    etelt_hozzaad(etel){
        if (!this.kedvenc_etelek.includes(etel)){
            this.kedvenc_etelek.push(etel);
        }
    }

    etrend(){
        for (let etel of this.kedvenc_etelek){
            if (etel instanceof Allat){
                this.husevo = true;
            }
        }
    }

    info() {
        console.log(`${this.faj}, ${this.labak_szama} laba van, ${this.husevo ? "husevo": "novenyevo"}`);
    }
}

class Oroszlan extends Allat{
    constructor(dzsungel_kiralya) {
        super("oroszlan");
        this.dzsungel_kiralya = dzsungel_kiralya;
    }

    info() {
        console.log(`${this.faj}, ${this.labak_szama} laba van, o${this.dzsungel_kiralya ? "" : " nem"} a dzsungel kiralya`);
    }

    uvolt(){
        console.log("RAAAAAAAWRRRRR!!")
    }
}

// peldanyositas

const gazella = new Allat("gazella");
const oroszlan = new Oroszlan(true);

gazella.etelt_hozzaad("fu");    // ez a metódus az ősosztályból jön
oroszlan.etelt_hozzaad(gazella);
oroszlan.etrend();

oroszlan.uvolt();
gazella.info();
oroszlan.info();

console.log(gazella instanceof Allat);
console.log(oroszlan instanceof Allat);
console.log(gazella instanceof Oroszlan);