package com.example.product.service;

import com.example.product.entity.Product;
import com.example.product.repository.ProductRepository;
import com.example.product.service.impl.ProductServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
class ProductServiceImplTest {

    @Mock
    private ProductRepository productRepository;

    private ProductServiceImpl productService;

    @BeforeEach
    void setUp() {
        productService = new ProductServiceImpl(productRepository);
    }

    @Test
    void createProductDefaultsActiveToTrue() {
        Product product = productWithId(1L);
        product.setActive(null);
        when(productRepository.save(product)).thenReturn(product);

        Product createdProduct = productService.createProduct(product);

        assertTrue(createdProduct.getActive());
        verify(productRepository).save(product);
    }

    @Test
    void getProductByIdReturnsStoredProduct() {
        Product product = productWithId(7L);
        when(productRepository.findById(7L)).thenReturn(Optional.of(product));

        assertEquals(product, productService.getProductById(7L));
    }

    @Test
    void getProductByIdRejectsUnknownId() {
        when(productRepository.findById(99L)).thenReturn(Optional.empty());

        RuntimeException error = assertThrows(
                RuntimeException.class,
                () -> productService.getProductById(99L)
        );

        assertTrue(error.getMessage().contains("99"));
    }

    @Test
    void updateProductChangesOnlyProvidedFields() {
        Product storedProduct = productWithId(3L);
        Product changes = new Product();
        changes.setName("Updated keyboard");
        when(productRepository.findById(3L)).thenReturn(Optional.of(storedProduct));
        when(productRepository.save(storedProduct)).thenReturn(storedProduct);

        Product updatedProduct = productService.updateProduct(3L, changes);

        assertEquals("Updated keyboard", updatedProduct.getName());
        assertEquals(99.0, updatedProduct.getPrice());
        assertEquals("Hardware", updatedProduct.getCategory());
    }

    @Test
    void deleteProductDoesNotCallDeleteForUnknownId() {
        when(productRepository.existsById(5L)).thenReturn(false);

        assertThrows(RuntimeException.class, () -> productService.deleteProduct(5L));
        verify(productRepository, never()).deleteById(5L);
    }

    private Product productWithId(Long id) {
        return new Product(id, "Keyboard", "Mechanical keyboard", 99.0, 10, "Hardware", true);
    }
}
