# Spring Boot Product Example

This project demonstrates a conventional layered Spring Boot application for
managing products. It is an ecosystem example, not a complete production
service: its purpose is to make dependencies between HTTP, business, and
persistence layers easy to inspect.

## Prerequisites

- JDK 17.
- Maven 3.9 or a compatible version.
- Basic Java and HTTP knowledge.

The application uses Spring Boot 3.2.3, Spring Web, Spring Data JPA, Lombok, and
an in-memory H2 database.

## Architecture

```text
HTTP request
    -> ProductController
    -> ProductService
    -> ProductServiceImpl
    -> ProductRepository
    -> H2 database
```

The controller translates HTTP requests, the service owns business operations,
and the repository handles persistence. Keeping these responsibilities
separate makes each boundary easier to test and replace.

## Build and test

From the repository root:

```powershell
mvn --file Spring/ProductExample/pom.xml verify
```

Run the application with:

```powershell
mvn --file Spring/ProductExample/pom.xml spring-boot:run
```

The default base URL is `http://localhost:8080/api/products`. Because H2 runs in
memory, application data is temporary and is lost when the process stops.

## API overview

| Method and path | Purpose |
| --- | --- |
| `POST /api/products` | Create a product. |
| `GET /api/products` | List all products. |
| `GET /api/products/{id}` | Retrieve one product. |
| `PUT /api/products/{id}` | Update one product. |
| `DELETE /api/products/{id}` | Delete one product. |
| `GET /api/products/category/{category}` | Filter by category. |
| `GET /api/products/low-stock?threshold=5` | Find low-stock products. |
| `GET /api/products/search?name=term` | Search by name. |

Example request:

```bash
curl -X POST http://localhost:8080/api/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Notebook","description":"A5 notebook","price":4.50,"stockQuantity":20,"category":"stationery","active":true}'
```

## Study method

Trace one request from the controller to the repository and back. At every
boundary, identify which layer owns validation, business decisions, and error
translation. Then inspect `ProductServiceImplTest` to see how the persistence
dependency is isolated during service tests.

Suggested exercises:

1. Add request validation and tests for invalid prices and stock quantities.
2. Map a missing product to a documented `404 Not Found` response.
3. Add controller integration tests with MockMvc.
4. Replace one repository query with an explicit derived-query method and
   explain the generated behavior.

## Current limitations

- Request validation and centralized exception mapping are not implemented.
- The API has no pagination or stable error representation.
- H2 is intended only for local learning and tests.
- Database migrations and production configuration are outside the current
  example.

These gaps are recorded explicitly so the example is not mistaken for a
production-ready service.

## Further reading

- [Spring Boot reference](https://docs.spring.io/spring-boot/reference/)
- [Spring Data JPA reference](https://docs.spring.io/spring-data/jpa/reference/)
- [Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/)
