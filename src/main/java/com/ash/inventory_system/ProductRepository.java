package com.ash.inventory_system;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    // THIS IS THE MAGIC METHOD
    // It finds products where the name contains your search text (case-insensitive)
    List<Product> findByNameContainingIgnoreCase(String name);
}