package com.corsospring;

public class Product {
    private Long id;
    private String codiceModello;
    private String breveDescrizione;
    private Double prezzo;
    private Integer quantita;

    public Product() { }

    public Product(Long id, String codiceModello, String breveDescrizione, Double prezzo, Integer quantita) {
        this.id = id;
        this.codiceModello = codiceModello;
        this.breveDescrizione = breveDescrizione;
        this.prezzo = prezzo;
        this.quantita = quantita;
    }

    // getters
    public Long getId() { return id; }
    public String getCodiceModello() { return codiceModello; }
    public String getBreveDescrizione() { return breveDescrizione; }
    public Double getPrezzo() { return prezzo; }
    public Integer getQuantita() { return quantita; }

    // setters
    public void setId(Long id) { this.id = id; }
    public void setCodiceModello(String codiceModello) { this.codiceModello = codiceModello; }
    public void setBreveDescrizione(String breveDescrizione) { this.breveDescrizione = breveDescrizione; }
    public void setPrezzo(Double prezzo) { this.prezzo = prezzo; }
    public void setQuantita(Integer quantita) { this.quantita = quantita; }

    @Override
    public String toString() {
        return "Product{" +
               "id=" + id +
               ", codiceModello='" + codiceModello + '\'' +
               ", breveDescrizione='" + breveDescrizione + '\'' +
               ", prezzo=" + prezzo +
               ", quantita=" + quantita +
               '}';
    }
}
