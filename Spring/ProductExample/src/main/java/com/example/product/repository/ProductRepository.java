package com.example.product.repository;

import com.example.product.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * Product Repository
 * 
 * This interface extends JpaRepository to provide basic CRUD operations
 * and custom query methods for the Product entity.
 */
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    
    /**
     * Find products by category
     * @param category the product category
     * @return list of products in the specified category
     */
    List<Product> findByCategory(String category);
    
    /**
     * Find active products
     * @return list of active products
     */
    List<Product> findByActiveTrue();
    
    /**
     * Find products with stock quantity less than specified value
     * @param quantity the threshold quantity
     * @return list of products with low stock
     */
    List<Product> findByStockQuantityLessThan(Integer quantity);
    
    /**
     * Find products by name containing the given string (case-insensitive)
     * @param name the name to search for
     * @return list of products matching the name
     */
    List<Product> findByNameContainingIgnoreCase(String name);
} 