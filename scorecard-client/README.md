# credit-scorecard-java-client

Fineract Credit Scorecard
- API version: 0.1.0-SNAPSHOT

An API module for credit risk assessment


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven/Gradle

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.apache.fineract</groupId>
  <artifactId>credit-scorecard-java-client</artifactId>
  <version>0.1.0-SNAPSHOT</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "org.apache.fineract:credit-scorecard-java-client:0.1.0-SNAPSHOT"
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/credit-scorecard-java-client-0.1.0-SNAPSHOT.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.apache.fineract.credit.scorecard.ApiClient;
import org.apache.fineract.credit.scorecard.ApiException;
import org.apache.fineract.credit.scorecard.Configuration;
import org.apache.fineract.credit.scorecard.models.*;
import org.apache.fineract.credit.scorecard.services.AlgorithmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://127.0.0.1:8000");

    AlgorithmsApi apiInstance = new AlgorithmsApi(defaultClient);
    Algorithm algorithm = new Algorithm(); // Algorithm | 
    try {
      Algorithm result = apiInstance.algorithmsCreate(algorithm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlgorithmsApi#algorithmsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:8000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlgorithmsApi* | [**algorithmsCreate**](docs/AlgorithmsApi.md#algorithmsCreate) | **POST** /api/v1/algorithms | 
*AlgorithmsApi* | [**algorithmsDestroy**](docs/AlgorithmsApi.md#algorithmsDestroy) | **DELETE** /api/v1/algorithms/{id} | 
*AlgorithmsApi* | [**algorithmsList**](docs/AlgorithmsApi.md#algorithmsList) | **GET** /api/v1/algorithms | 
*AlgorithmsApi* | [**algorithmsPartialUpdate**](docs/AlgorithmsApi.md#algorithmsPartialUpdate) | **PATCH** /api/v1/algorithms/{id} | 
*AlgorithmsApi* | [**algorithmsPredict**](docs/AlgorithmsApi.md#algorithmsPredict) | **POST** /api/v1/algorithms/predict | 
*AlgorithmsApi* | [**algorithmsRetrieve**](docs/AlgorithmsApi.md#algorithmsRetrieve) | **GET** /api/v1/algorithms/{id} | 
*AlgorithmsApi* | [**algorithmsUpdate**](docs/AlgorithmsApi.md#algorithmsUpdate) | **PUT** /api/v1/algorithms/{id} | 
*DatasetsApi* | [**datasetsList**](docs/DatasetsApi.md#datasetsList) | **GET** /api/v1/datasets | 
*DatasetsApi* | [**datasetsRetrieve**](docs/DatasetsApi.md#datasetsRetrieve) | **GET** /api/v1/datasets/{id} | 
*RequestsApi* | [**requestsCreate**](docs/RequestsApi.md#requestsCreate) | **POST** /api/v1/requests | 
*RequestsApi* | [**requestsDestroy**](docs/RequestsApi.md#requestsDestroy) | **DELETE** /api/v1/requests/{id} | 
*RequestsApi* | [**requestsList**](docs/RequestsApi.md#requestsList) | **GET** /api/v1/requests | 
*RequestsApi* | [**requestsPartialUpdate**](docs/RequestsApi.md#requestsPartialUpdate) | **PATCH** /api/v1/requests/{id} | 
*RequestsApi* | [**requestsRetrieve**](docs/RequestsApi.md#requestsRetrieve) | **GET** /api/v1/requests/{id} | 
*RequestsApi* | [**requestsUpdate**](docs/RequestsApi.md#requestsUpdate) | **PUT** /api/v1/requests/{id} | 


## Documentation for Models

 - [Algorithm](docs/Algorithm.md)
 - [Dataset](docs/Dataset.md)
 - [PredictionRequest](docs/PredictionRequest.md)
 - [PredictionResponse](docs/PredictionResponse.md)


## Documentation for Authorization

All endpoints do not require authorization.
Authentication schemes defined for the API:

## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author


