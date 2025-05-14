package com.example.product.service;

import com.example.product.entity.Product;
import java.util.List;

/**
 * Product Service Interface
 * 
 * This interface defines the business operations available for products.
 * It provides methods for managing products including CRUD operations
 * and business-specific operations.
 */
public interface ProductService {
    
    /**
     * Create a new product
     * @param product the product to create
     * @return the created product
     */
    Product createProduct(Product product);
    
    /**
     * Get a product by its ID
     * @param id the product ID
     * @return the product if found
     * @throws RuntimeException if product not found
     */
    Product getProductById(Long id);
    
    /**
     * Get all products
     * @return list of all products
     */
    List<Product> getAllProducts();
    
    /**
     * Update an existing product
     * @param id the product ID
     * @param product the updated product data
     * @return the updated product
     * @throws RuntimeException if product not found
     */
    Product updateProduct(Long id, Product product);
    
    /**
     * Delete a product
     * @param id the product ID
     * @throws RuntimeException if product not found
     */
    void deleteProduct(Long id);
    
    /**
     * Get products by category
     * @param category the product category
     * @return list of products in the category
     */
    List<Product> getProductsByCategory(String category);
    
    /**
     * Get products with low stock
     * @param threshold the stock threshold
     * @return list of products with stock below threshold
     */
    List<Product> getProductsWithLowStock(Integer threshold);
    
    /**
     * Search products by name
     * @param name the name to search for
     * @return list of matching products
     */
    List<Product> searchProductsByName(String name);
} 