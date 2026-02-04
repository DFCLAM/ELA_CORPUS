# ELA_CORPUS

This repository contains the corpus of documents published in ELA - https://ela.unisi.it/

## Naming conventions (ita)

```
ELA_1_1_nomeautore_titolo.xml
```

[+eventuali altri dati di disambiguazione]

Esempi:

```
ELA_2_2_andreasdeperusia_epistola.xml
ELA_2_2_augustinusapaschali_epistola_16841215.xml
ELA_2_2_benedictuspolonus_relatio.xml
ELA_2_2_iohannesdemontecorvino_epistola2.xml
ELA_2_2_iohannesdemontecorvino_epistola3.xml
```

I due numeri iniziali determinano la qualità della trascrizione del testo (da 1 a 3) e la qualità di codifica in tei (da 1 a 3).

Se il testo proviene da un altro archivio e non ci sono sostanziali modifiche, usare l'acronimo di riferimento.

Esempi:

```
ALIM_2_2_iohannesdemontecorvino_espistola4.xml
CORPUS_1_2_rubruic_itinerario.xml
```

(*Emmanuela Carbé*)

## License

There is no single license valid for the entire corpus: each XML/TEI document declares its own license in the `<availability>` of the `<teiHeader>`.
