package com.ash.inventory_system;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class InventorySystemApplication {

    public static void main(String[] args) {
        SpringApplication.run(InventorySystemApplication.class, args);
    }

    // This method runs automatically when the app starts!
    @Bean
    public CommandLineRunner demo(ProductRepository repository) {
        return (args) -> {
            // 1. Clear the database so we don't get duplicates every time we run
            repository.deleteAll();

            // 2. Add some fake inventory
            repository.save(new Product("Dell XPS 15", "Electronics", 1200.00, 50));
            repository.save(new Product("Herman Miller Chair", "Furniture", 850.00, 10));
            repository.save(new Product("Mechanical Keyboard", "Electronics", 150.00, 25));
            repository.save(new Product("27-inch Monitor", "Electronics", 300.00, 15));
            repository.save(new Product("Standing Desk", "Furniture", 500.00, 5));
            repository.save(new Product("Golden Rolex", "Luxury", 15000.00, 2));
            // 3. Print a success message to the console
            System.out.println("--------------------------------------------");
            System.out.println("✅ SUCCESS: Fake data loaded into the Database!");
            System.out.println("--------------------------------------------");
        };
    }
}