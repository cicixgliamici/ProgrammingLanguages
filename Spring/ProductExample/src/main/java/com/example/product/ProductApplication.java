package com.example.product;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Main Application Class for the Product Management System
 * 
 * This class serves as the entry point for the Spring Boot application.
 * The @SpringBootApplication annotation is a convenience annotation that adds all of the following:
 * - @Configuration: Tags the class as a source of bean definitions
 * - @EnableAutoConfiguration: Tells Spring Boot to start adding beans based on classpath settings
 * - @ComponentScan: Tells Spring to look for other components, configurations, and services in the current package
 * 
 * The main method uses SpringApplication.run() to bootstrap the application, starting Spring,
 * which starts the auto-configured Tomcat web server.
 */
@SpringBootApplication
public class ProductApplication {

    /**
     * Main method that bootstraps the Spring Boot application
     * 
     * @param args Command line arguments passed to the application
     */
    public static void main(String[] args) {
        SpringApplication.run(ProductApplication.class, args);
    }
} 