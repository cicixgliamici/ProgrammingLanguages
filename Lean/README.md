# Studiare Lean 4

Questa cartella è un percorso progressivo di programmazione funzionale e
dimostrazione formale. I file sono autonomi: possono essere letti ed eseguiti
singolarmente, nell'ordine indicato dal prefisso numerico.

## Che cos'è Lean

Lean 4 è sia un linguaggio di programmazione funzionale sia un *proof assistant*.
Una definizione come `def double (n : Nat) : Nat := n * 2` è un programma;
un teorema come `theorem t (n : Nat) : n = n := by rfl` è una definizione il
cui valore è una prova. Il kernel di Lean controlla che il termine costruito
abbia davvero il tipo dichiarato.

Questa idea è chiamata corrispondenza di Curry–Howard:

- una proposizione è un tipo;
- una prova è un valore di quel tipo;
- `p → q` è una funzione che trasforma una prova di `p` in una prova di `q`;
- `p ∧ q` contiene entrambe le prove;
- `p ∨ q` contiene una delle due prove, identificata da un costruttore;
- `¬p` è un'abbreviazione per `p → False`.

Lean usa tipi induttivi. `Nat`, `List`, `Option` e gli alberi definiti negli
esercizi sono descritti mediante costruttori. Il `match` elimina un valore
considerando tutti i suoi costruttori; la ricorsione strutturale richiama una
funzione solo su parti più piccole del dato. Questa restrizione permette a Lean
di verificare la terminazione.

## File, comandi e feedback dell'editor

In un file `.lean` si incontrano principalmente:

```lean
def square (n : Nat) : Nat := n * n

#check square       -- mostra il tipo, senza eseguire il programma
#eval square 5      -- valuta l'espressione e stampa 25

example (n : Nat) : n = n := by
  rfl               -- controlla una prova senza assegnarle un nome pubblico
```

`#check` e `#eval` sono comandi di sviluppo: aiutano a esplorare il codice, ma
non fanno parte del risultato di una funzione. Nell'estensione VS Code
**Lean 4**, posizionando il cursore dopo una tattica si vedono gli obiettivi
ancora aperti e le ipotesi disponibili.

Per controllare un singolo file dalla cartella principale del repository:

```powershell
lean .\Lean\005_Induction.lean
```

Se Lean termina senza errori, tutte le definizioni e tutte le prove del file
sono state accettate. Le righe `#eval` producono inoltre il loro output.

## Elaborazione, compilazione e kernel

Quando Lean legge un sorgente attraversa, in modo semplificato, queste fasi:

1. Il parser trasforma il testo in sintassi.
2. L'elaboratore risolve nomi, argomenti impliciti, typeclass e notazione; le
   tattiche generano termini di prova.
3. Il kernel controlla i termini risultanti. È la piccola parte fidata del
   sistema: non si fida delle tattiche, ma solo del termine finale.
4. Per eseguire programmi, Lean può valutare nell'ambiente oppure generare
   codice C e compilare un eseguibile nativo tramite `lean --run` o Lake.

Una prova normalmente non ha bisogno di essere eseguita: deve essere
*type-checked*. La compilazione nativa è invece utile per applicazioni Lean con
un `main`:

```lean
def main : IO Unit :=
  IO.println "Hello from Lean"
```

## Elan: gestire le versioni di Lean

**Elan** è il gestore delle toolchain di Lean, analogo a `rustup` per Rust.
Installa versioni di Lean e mette a disposizione comandi proxy come `lean` e
`lake`. I comandi fondamentali sono:

```powershell
elan --version
elan show
elan toolchain list
elan default stable
elan update
```

Un progetto può contenere un file `lean-toolchain`, per esempio:

```text
leanprover/lean4:v4.24.0
```

Elan legge quel file e seleziona automaticamente la versione richiesta quando
si lavora nella cartella del progetto. Fissare una versione rende la build
riproducibile: aggiornamenti del compilatore o della libreria standard non
cambiano inaspettatamente le prove.

## Lake: progetti, dipendenze e build

**Lake** è il build system e package manager incluso nella toolchain Lean. Per
creare un progetto didattico minimale in una nuova cartella:

```powershell
lake new MyLeanProject
cd MyLeanProject
lake build
lake env lean MyLeanProject.lean
```

I file principali di un progetto moderno sono:

- `lean-toolchain`: versione di Lean scelta da Elan;
- `lakefile.toml` oppure `lakefile.lean`: package, librerie, eseguibili e
  dipendenze;
- `lake-manifest.json`: versioni risolte delle dipendenze;
- `.lake/`: cache di build e pacchetti scaricati;
- `Main.lean` o i moduli della libreria: codice sorgente.

Comandi utili:

```powershell
lake build              # controlla e compila tutti i target
lake update             # aggiorna le dipendenze e il manifest
lake env lean File.lean # usa l'ambiente e le dipendenze del progetto
lake exe nome           # esegue un target eseguibile
```

Questa cartella non richiede ancora Lake perché ogni lezione è indipendente e
usa soltanto ciò che Lean importa implicitamente. In un progetto con moduli, un
file `Geometry/Point.lean` viene importato come `import Geometry.Point`; Lake
configura i percorsi nei quali Lean cerca questi moduli.

## Tattiche e termini

Il blocco `by` apre la modalità tattica. Le tattiche modificano uno stato formato
da ipotesi locali e obiettivi:

```lean
example (p q : Prop) : p → q → p ∧ q := by
  intro hp hq        -- aggiunge le due ipotesi
  constructor        -- divide l'obiettivo p ∧ q
  · exact hp         -- risolve il primo sotto-obiettivo
  · exact hq         -- risolve il secondo
```

La stessa prova può essere scritta come termine:

```lean
example (p q : Prop) : p → q → p ∧ q :=
  fun hp hq => ⟨hp, hq⟩
```

Per studiare conviene comprendere entrambe le forme. Le tattiche mostrano bene
il processo; i termini rendono evidente che una prova è un programma.

## Ordine di studio

1. `000`–`004`: definizioni, proposizioni, riscrittura, pattern matching e
   strutture.
2. `005`–`006`: ricorsione, induzione e liste.
3. `007`–`009`: logica proposizionale, tipi induttivi e tattiche.
4. `010`–`012`: `Option`, somme, prodotti e combinatori su liste.
5. `013`–`015`: dimostrazioni strutturali su liste e alberi.
6. `016`: typeclass, istanze e codice generico basato su capacità.
7. `017`: tipi dipendenti, vettori indicizzati e accessi sicuri con `Fin`.
8. `018`: mini-linguaggio aritmetico, ottimizzazione e prova di correttezza.

Un buon metodo consiste nel coprire una soluzione, provare a ricostruirla e
osservare lo stato degli obiettivi dopo ogni riga. Quando una prova usa `simp`,
provare anche `simp?`: Lean può suggerire un insieme più preciso di lemmi.

## Problemi comuni

- **Unknown identifier**: il nome non è nello scope, è scritto diversamente o
  manca un `import`.
- **Type mismatch**: il valore prodotto ha un tipo diverso da quello atteso;
  leggere entrambi i tipi nel messaggio prima di aggiungere tattiche.
- **Unsolved goals**: il blocco `by` è terminato lasciando sotto-obiettivi aperti.
- **Failed to synthesize**: Lean non trova un'istanza richiesta, per esempio
  uguaglianza decidibile o `BEq` per un tipo generico.
- **Fail to show termination**: la chiamata ricorsiva non è evidentemente su un
  dato strutturalmente più piccolo; occorre cambiare la definizione o fornire
  una misura di terminazione.
- **Versione incompatibile**: controllare `elan show` e il contenuto di
  `lean-toolchain` del progetto.

Il principio più utile è leggere prima il goal come un tipo: chiedersi quale
costruttore o quale funzione possa produrre un valore di quel tipo. Le tattiche
diventano così strumenti guidati dalla struttura, non comandi da memorizzare.
