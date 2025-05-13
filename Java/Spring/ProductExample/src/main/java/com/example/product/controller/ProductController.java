package com.example.product.controller;

import com.example.product.entity.Product;
import com.example.product.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Product Controller
 * 
 * This REST controller provides endpoints for managing products.
 * It handles HTTP requests and delegates business logic to the service layer.
 */
@RestController
@RequestMapping("/api/products")
public class ProductController {

    private final ProductService productService;

    @Autowired
    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    /**
     * Create a new product
     * @param product the product to create
     * @return the created product
     */
    @PostMapping
    public ResponseEntity<Product> createProduct(@RequestBody Product product) {
        return new ResponseEntity<>(productService.createProduct(product), HttpStatus.CREATED);
    }

    /**
     * Get a product by ID
     * @param id the product ID
     * @return the product if found
     */
    @GetMapping("/{id}")
    public ResponseEntity<Product> getProductById(@PathVariable Long id) {
        return ResponseEntity.ok(productService.getProductById(id));
    }

    /**
     * Get all products
     * @return list of all products
     */
    @GetMapping
    public ResponseEntity<List<Product>> getAllProducts() {
        return ResponseEntity.ok(productService.getAllProducts());
    }

    /**
     * Update a product
     * @param id the product ID
     * @param product the updated product data
     * @return the updated product
     */
    @PutMapping("/{id}")
    public ResponseEntity<Product> updateProduct(@PathVariable Long id, @RequestBody Product product) {
        return ResponseEntity.ok(productService.updateProduct(id, product));
    }

    /**
     * Delete a product
     * @param id the product ID
     */
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteProduct(@PathVariable Long id) {
        productService.deleteProduct(id);
        return ResponseEntity.noContent().build();
    }

    /**
     * Get products by category
     * @param category the product category
     * @return list of products in the category
     */
    @GetMapping("/category/{category}")
    public ResponseEntity<List<Product>> getProductsByCategory(@PathVariable String category) {
        return ResponseEntity.ok(productService.getProductsByCategory(category));
    }

    /**
     * Get products with low stock
     * @param threshold the stock threshold
     * @return list of products with stock below threshold
     */
    @GetMapping("/low-stock")
    public ResponseEntity<List<Product>> getProductsWithLowStock(@RequestParam Integer threshold) {
        return ResponseEntity.ok(productService.getProductsWithLowStock(threshold));
    }

    /**
     * Search products by name
     * @param name the name to search for
     * @return list of matching products
     */
    @GetMapping("/search")
    public ResponseEntity<List<Product>> searchProductsByName(@RequestParam String name) {
        return ResponseEntity.ok(productService.searchProductsByName(name));
    }
} 