# Studiare Coq / Rocq

Questa cartella introduce Coq con lo stesso stile delle lezioni Lean: file
numerati, obiettivi espliciti, definizioni commentate, esempi eseguibili,
dimostrazioni complete e note finali.

Il progetto è oggi chiamato **Rocq Prover**, mentre il nome Coq, i comandi
storici e molti materiali didattici restano ancora molto diffusi. I sorgenti
continuano a usare normalmente l'estensione `.v`.

## Coq come linguaggio e proof assistant

Coq usa il calcolo delle costruzioni induttive. Come in Lean, programmi e prove
sono termini tipati:

- una proposizione ha tipo `Prop`;
- una prova è un termine della proposizione;
- `P -> Q` può essere letto come una funzione da prove di `P` a prove di `Q`;
- i tipi induttivi descrivono numeri, liste e strutture definite dall'utente;
- il kernel controlla il termine finale prodotto dalle tattiche.

Una differenza sintattica immediata rispetto a Lean è che ogni comando Coq
termina con un punto. Una dimostrazione tipica ha questa forma:

```coq
Theorem identity (P : Prop) : P -> P.
Proof.
  intro proof_of_p.
  exact proof_of_p.
Qed.
```

## Esecuzione e compilazione

Con una distribuzione Coq 8.x, un singolo file si controlla dalla radice del
repository con:

```powershell
coqc .\Coq\000_BasicDefinitions.v
```

`coqc` controlla il sorgente `.v` e produce un oggetto compilato `.vo`.
`coqtop` apre invece un ambiente testuale interattivo. Nelle distribuzioni Rocq
più recenti gli equivalenti sono esposti anche attraverso comandi `rocq`, come
`rocq compile` e `rocq repl`; verificare i nomi forniti dalla versione installata.

Per progetti composti da più moduli si usano un file `_CoqProject` e strumenti
come `coq_makefile` oppure Dune. Le opzioni `-Q` e `-R` associano directory
fisiche a namespace logici.

La documentazione ufficiale conferma che `coqc` compila file `.v` in `.vo`,
mentre `coqtop` è l'interfaccia interattiva:
[Coq commands](https://rocq-prover.org/doc/V8.20.1/refman/practical-tools/coq-commands.html).

## Editor

Su VS Code si può usare VSCoq. L'editor invia il documento al prover una frase
alla volta e mostra contesto, ipotesi e obiettivo corrente. È utile avanzare
lentamente nella prova anziché eseguire subito tutto il file.

## Ordine di studio

1. `000_BasicDefinitions.v`: definizioni, tipi, `Check` e `Compute`.
2. `001_Propositions.v`: implicazioni, congiunzioni e disgiunzioni.
3. `002_RewritingAndSimplification.v`: uguaglianze, `rewrite` e `simpl`.
4. `003_InductiveTypes.v`: costruttori, `match` e `destruct`.
5. `004_Lists.v`: ricorsione e induzione strutturale sulle liste.
6. `005_Induction.v`: funzioni ricorsive e prove sui naturali.

## Tattiche iniziali

- `intro`: introduce una premessa o una variabile;
- `exact`: fornisce direttamente il termine richiesto;
- `apply`: usa un teorema e genera obiettivi per le sue premesse;
- `split`: costruisce una congiunzione;
- `left` / `right`: sceglie un ramo di una disgiunzione;
- `destruct`: analizza i costruttori di un valore;
- `rewrite`: sostituisce mediante un'uguaglianza;
- `simpl`: esegue riduzioni definizionali;
- `induction`: genera caso base, passi induttivi e ipotesi di induzione;
- `reflexivity`: chiude uguaglianze vere per calcolo.

## Confronto rapido con Lean

`Qed` in Coq corrisponde alla chiusura di una dichiarazione dimostrata; Lean
termina invece il blocco tramite la struttura sintattica della dichiarazione.
`Fixpoint` è la forma esplicita usuale per una funzione ricorsiva in Coq, mentre
Lean usa normalmente `def` con equazioni ricorsive. In entrambi i sistemi il
kernel non si fida delle tattiche: controlla il termine di prova risultante.

In questo ambiente `coqc` non è attualmente installato. I file sono scritti con
funzionalità introduttive della libreria standard, ma la verifica automatica
locale richiederà l'installazione di Coq/Rocq.
