package com.ash.inventory_system;

import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/products")
@CrossOrigin(origins = "*") // Allows the browser/Python to talk to us easily
public class ProductController {

    private final ProductRepository repository;

    public ProductController(ProductRepository repository) {
        this.repository = repository;
    }

    // 1. GET ALL: Allows anyone to download our full inventory
    // access by visiting: http://localhost:8080/api/products
    @GetMapping
    public List<Product> getAllProducts() {
        return repository.findAll();
    }

    // 2. QUICK ADD: A simple way to add items via the browser URL
    // Try: http://localhost:8080/api/products/add?name=iPhone&price=999
    @GetMapping("/add")
    public Product quickAdd(@RequestParam String name, @RequestParam Double price) {
        Product newProduct = new Product(name, "New Arrival", price, 100);
        return repository.save(newProduct);
    }
    @PostMapping("/add")
    public Product addFullProduct(@RequestBody Product product) {
        return repository.save(product);
    }

    // 4. SEARCH: specific logic to find items on the backend
    // Usage: http://localhost:8080/api/products/search?text=macbook
    @GetMapping("/search")
    public List<Product> searchProducts(@RequestParam String text) {
        return repository.findByNameContainingIgnoreCase(text);
    }

    // 5. DELETE: Allows us to remove an item by its ID
    // Usage: DELETE http://localhost:8080/api/products/1
    @DeleteMapping("/{id}")
    public void deleteProduct(@PathVariable Long id) {
        repository.deleteById(id);
    }
}