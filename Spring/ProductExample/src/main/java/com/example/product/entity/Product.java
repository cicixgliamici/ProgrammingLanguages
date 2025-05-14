package com.example.product.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * Product Entity
 * 
 * This class represents a product in the system.
 * It includes basic product information such as name,
 * description, price, and stock quantity.
 * 
 * Lombok Annotations:
 * @Data - A convenient shortcut annotation that bundles the features of:
 *         - @Getter: Generates getters for all fields
 *         - @Setter: Generates setters for all fields
 *         - @ToString: Generates toString() method
 *         - @EqualsAndHashCode: Generates equals() and hashCode() methods
 *         - @RequiredArgsConstructor: Generates constructor for required fields
 * 
 * @NoArgsConstructor - Generates a constructor with no parameters
 * @AllArgsConstructor - Generates a constructor with parameters for all fields
 */
@Entity
@Table(name = "products")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Product {
    
    /**
     * Primary key of the product
     * @GeneratedValue with IDENTITY strategy means the database will automatically
     * generate and increment this value for each new product
     */
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    /**
     * Product name
     */
    private String name;
    
    /**
     * Detailed description of the product
     */
    private String description;
    
    /**
     * Product price
     */
    private Double price;
    
    /**
     * Current quantity in stock
     */
    private Integer stockQuantity;
    
    /**
     * Product category for classification
     */
    private String category;
    
    /**
     * Flag indicating if the product is active in the system
     */
    private Boolean active;
} 