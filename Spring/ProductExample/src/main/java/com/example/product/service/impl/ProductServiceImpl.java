package com.example.product.service.impl;

import com.example.product.entity.Product;
import com.example.product.repository.ProductRepository;
import com.example.product.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Product Service Implementation
 * 
 * This class implements the ProductService interface and provides
 * the business logic for product management operations.
 */
@Service
public class ProductServiceImpl implements ProductService {

    private final ProductRepository productRepository;

    @Autowired
    public ProductServiceImpl(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    @Override
    public Product createProduct(Product product) {
        // Set default values for new products
        if (product.getActive() == null) {
            product.setActive(true);
        }
        return productRepository.save(product);
    }

    @Override
    public Product getProductById(Long id) {
        return productRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Product not found with id: " + id));
    }

    @Override
    public List<Product> getAllProducts() {
        return productRepository.findAll();
    }

    @Override
    public Product updateProduct(Long id, Product product) {
        Product existingProduct = getProductById(id);
        
        // Update only non-null fields
        if (product.getName() != null) {
            existingProduct.setName(product.getName());
        }
        if (product.getDescription() != null) {
            existingProduct.setDescription(product.getDescription());
        }
        if (product.getPrice() != null) {
            existingProduct.setPrice(product.getPrice());
        }
        if (product.getStockQuantity() != null) {
            existingProduct.setStockQuantity(product.getStockQuantity());
        }
        if (product.getCategory() != null) {
            existingProduct.setCategory(product.getCategory());
        }
        if (product.getActive() != null) {
            existingProduct.setActive(product.getActive());
        }
        
        return productRepository.save(existingProduct);
    }

    @Override
    public void deleteProduct(Long id) {
        if (!productRepository.existsById(id)) {
            throw new RuntimeException("Product not found with id: " + id);
        }
        productRepository.deleteById(id);
    }

    @Override
    public List<Product> getProductsByCategory(String category) {
        return productRepository.findByCategory(category);
    }

    @Override
    public List<Product> getProductsWithLowStock(Integer threshold) {
        return productRepository.findByStockQuantityLessThan(threshold);
    }

    @Override
    public List<Product> searchProductsByName(String name) {
        return productRepository.findByNameContainingIgnoreCase(name);
    }
} 