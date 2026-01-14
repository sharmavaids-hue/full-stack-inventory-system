package com.ash.inventory_system;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // Unique ID for every item

    private String name;
    private String category;
    private Double price;
    private Integer stockLevel;

    // Empty Constructor (Needed for the Database)
    public Product() {}

    // Constructor for us to use easily
    public Product(String name, String category, Double price, Integer stockLevel) {
        this.name = name;
        this.category = category;
        this.price = price;
        this.stockLevel = stockLevel;
    }

    // Getters (So the app can read the data)
    public Long getId() { return id; }
    public String getName() { return name; }
    public String getCategory() { return category; }
    public Double getPrice() { return price; }
    public Integer getStockLevel() { return stockLevel; }

    // Setters (So the app can update the data)
    public void setName(String name) { this.name = name; }
    public void setCategory(String category) { this.category = category; }
    public void setPrice(Double price) { this.price = price; }
    public void setStockLevel(Integer stockLevel) { this.stockLevel = stockLevel; }
}
