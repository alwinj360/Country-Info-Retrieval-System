# Country Information Retrieval System

A Python-based information retrieval system that stores and queries development indicator data for 20 countries. The system implements multiple data structures (Binary Search Tree, Hash Table, Linked List, Sorted List) and provides a command-line interface for efficient data retrieval and analysis.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/alwinj360/Country-Info-Retrieval-System.git
cd Country-Info-Retrieval-System

# Run the program
python main.py
```

Then follow the interactive prompts to query country data!

## Table of Contents

- [Features](#features)
- [Development Indicators](#development-indicators)
- [Data Structures](#data-structures)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Performance Analysis](#performance-analysis)
- [Authors](#authors)

## Features

- **Multiple Data Structure Implementations**: Choose from BST, Hash Table, Linked List, or Sorted List for data storage
- **Interactive CLI**: User-friendly command-line interface for querying country data
- **Comprehensive Queries**: Search by country, view specific indicators, find min/max values
- **Performance Benchmarking**: Compare search efficiency across different data structures
- **Case-Insensitive Search**: Query countries without worrying about capitalization

## Development Indicators

The system contains real-world data from the **World Bank's World Development Indicators** database (last updated: March 1, 2023) for 20 countries. Each country includes the following development indicators:

1. **Population Total** - Total population count (e.g., India: 1,396,387,127)
2. **Life Expectancy at Birth** - Average years (e.g., Singapore: 83.74 years)
3. **Access to Clean Fuels and Technologies** - Percentage of population with access to clean cooking fuels (e.g., USA: 100%)
4. **Basic Drinking Water Services** - Percentage of population using at least basic drinking water services (e.g., UAE: 99.97%)
5. **GDP per Capita** - Current US Dollars (e.g., USA: $63,530.63)

**Countries included**: India, Mexico, Afghanistan, United Arab Emirates, United States, Ukraine, Uruguay, Singapore, Pakistan, El Salvador, Philippines, Nigeria, Canada, France, Japan, Morocco, Australia, Jordan, Sri Lanka, Vietnam

## Data Structures

The system implements four different data structure approaches:

### Binary Search Tree (BST)
- **File**: `countryIRSystemBSTDict.py`
- **Performance**: O(log n) average case for search operations
- **Use Case**: Balanced performance for small to medium datasets

### Hash Table
- **File**: `countryIRSystemHTDict.py`
- **Performance**: O(1) average case for search operations
- **Implementation**: Custom hash function based on country name length
- **Use Case**: Fastest retrieval for large datasets

### Linked List
- **File**: `countryIRSystemLLDict.py`
- **Performance**: O(n) for search operations
- **Use Case**: Simple implementation, good for small datasets

### Sorted List
- **File**: `countryIRSystemSLDict.py`
- **Performance**: O(n) for insertion (maintains sorted order), O(n) for search
- **Use Case**: When sorted order is important

## Installation

### Prerequisites

- Python 3.x
- No external dependencies required (uses only Python standard library)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/alwinj360/Country-Info-Retrieval-System.git
cd Country-Info-Retrieval-System
```

2. Ensure your data file is in the correct location:
```
datafiles/country_data.csv
```

The repository includes:
- `country_data.csv` - Real-world data for 20 countries (World Bank, 2020)
- `rand_*.txt` files - Generated test data for performance benchmarking

## Usage

### Running the Interactive Interface

**Recommended**: Launch the command-line interface using the BST implementation:

```bash
python main.py
```

This runs the `main.py` file, which uses the Binary Search Tree Dictionary implementation for optimal performance.

Or run specific implementations for testing:

```bash
# List-based implementation
python mainList.py

# Linked List Dictionary implementation
python mainLLDict.py

# Sorted List Dictionary implementation
python mainSLDict.py

# Hash Table Dictionary implementation  
python mainHTDict.py
```

**Alternative**: Use the interface module directly:
```bash
python -c "from otherFiles.interface import Interface; Interface.country_irsystem_Cl_dict()"
```

### Interactive Menu Options

When you run the program, you'll see:

```
Welcome to our program!
This program requires your input in order to function.

Please enter a number to select:
 00: Exit Program
 1: Print Data for a given country
 2: See indicators
```

### Example Queries

**Query 1: Get all data for a country**
```
Select: 1
Enter country name: India
```
Output displays all development indicators for India.

**Query 2: View specific indicator for all countries**
```
Select: 2
Choose indicator: 1 (Population Total)
Choose method: 2 (List all countries)
```
Output displays population data for all 20 countries.

**Query 3: Find minimum/maximum values**
```
Select: 2
Choose indicator: 5 (GDP per Capita)
Choose method: 3 (Find min/max)
```
Output shows countries with lowest and highest GDP per capita.

## Project Structure

```
Country-Info-Retrieval-System/
│
├── dict/                          # Dictionary implementations
│   ├── abstract.py                # Abstract base classes
│   ├── bstdict.py                 # Binary Search Tree dictionary
│   ├── htdict.py                  # Hash Table dictionary
│   ├── lldict.py                  # Linked List dictionary
│   └── sldict.py                  # Sorted List dictionary
│
├── irsystems/                     # IR System implementations
│   ├── countryIRSystemBSTDict.py  # BST-based system
│   ├── countryIRSystemHTDict.py   # Hash Table-based system
│   ├── countryIRSystemLLDict.py   # Linked List-based system
│   ├── countryIRSystemSLDict.py   # Sorted List-based system
│   └── countryIRSystemList.py     # Simple list-based system
│
├── otherFiles/                    # Supporting files
│   ├── country.py                 # Country class definition
│   ├── interface.py               # Command-line interface
│   ├── analysis_methods.py        # Performance analysis tools
│   └── randomFiles.py             # Test data generation
│
├── datafiles/                     # Data storage
│   ├── country_data.csv           # Real country data (20 countries)
│   ├── rand_10.txt                # Test data: 10 entries
│   ├── rand_100.txt               # Test data: 100 entries
│   └── rand_500.txt               # Test data: 500 entries
│
├── main.py                        # Main entry point (uses BST)
├── analyze.py                     # Performance benchmarking script
├── test.py                        # Testing utilities
├── main*.py                       # Various implementation demos
└── README.md                      # This file
```

## Performance Analysis

The system includes built-in performance benchmarking capabilities to compare search efficiency across different data structures.

### Running Performance Tests

```bash
python analyze.py
```

This script (located in `analyze.py`) generates random country data files and runs thousands of queries to measure performance across all implementations.

### Actual Benchmark Results

**Test Configuration**: 1000 queries on different dataset sizes

#### 100 Entries Dataset
- **List**: 0.0040 seconds
- **BST Dict**: 0.0129 seconds  
- **LL Dict**: 0.0250 seconds
- **SL Dict**: 0.0169 seconds

#### 1000 Entries Dataset
- **List**: 0.0349 seconds
- **BST Dict**: 0.0099 seconds **(Fastest!)**
- **SL Dict**: 0.2004 seconds

### Key Findings

1. **Binary Search Tree (BST)** offers the best performance for medium to large datasets (1000+ entries)
2. **List-based implementation** is faster for very small datasets (< 100 entries) due to lower overhead
3. **Hash Table** provides O(1) average lookup but wasn't included in final benchmarks
4. **Sorted List** has slower performance due to insertion sort overhead

> **Note**: BST was chosen for the final implementation despite List being slightly faster on small datasets because:
> - Better scalability for larger datasets
> - More interesting algorithmic challenge
> - Maintains O(log n) performance as data grows

### Performance Visualization

The `analyze.py` script allows you to test with custom parameters:
```python
from otherFiles.analysis_methods import countryIRSystem_analysis

# Test with custom configuration
countryIRSystem_analysis(
    "dataFiles/rand_100.csv",  # Data file
    100000,                      # Number of queries
    100                         # Number of entries
)
```

### Generating Test Data

The system includes utilities to generate random country data for testing:

```python
from otherFiles.randomFiles import generate_data_csv

# Generate a CSV file with random country data
generate_data_csv("test_data.csv", 1000)  # Creates file with 1000 entries
```

Test data files follow this format:
```
2020,YR2020,India1,IND,1400000000,70,90,90,15000
2020,YR2020,India2,IND,1400000000,70,90,90,15000
...
```

## Architecture

The project follows object-oriented design principles:

- **Abstract Base Classes**: Define contracts for all implementations
- **Inheritance**: All data structures inherit from abstract classes
- **Encapsulation**: Country data encapsulated in `Country` class
- **Polymorphism**: Same interface across different data structure implementations

## Key Implementation Details

### Country Class

Each country object stores:
```python
- country_name (str)
- country_code (str)
- population_total (int)
- life_expectancy_at_birth (float)
- access_to_clean_fuel_and_tech (float)
- using_basic_drinking_water (float)
- GDP_per_capita (float)
```

### Hash Function

The hash table implementation uses a simple modulo hash based on country name length:
```python
index = len(country_name) % 20
```

## Data Source

The country data is sourced from the **World Bank's World Development Indicators** database:
- **Database**: World Development Indicators
- **Last Updated**: March 1, 2023
- **Year**: 2020 data
- **Countries**: 20 selected nations representing diverse regions and development levels

All data is authentic and reflects real-world development metrics as reported by the World Bank.

## Authors

**Project Team** (Spring 2023):
- **Alwin Joseph Kowattu** (Alwin Alwin Joseph) - Binary Search Tree implementation, data loading, CLI design, Hash Table implementation
- **Vel Perez-Barba** - Linked List implementation, search algorithms, min/max functions, testing
- **Elyas Ehsan** - Data retrieval methods, series functions, query operations, documentation

**Project Date**: May 15, 2023

## Academic Context

This project was developed as part of a Data Structures course to:
- Explore different data structure implementations
- Compare performance characteristics in information retrieval
- Practice object-oriented programming principles
- Build practical applications with real-world data

## License

This project is available for educational purposes.

## Contributing

This is an academic project. For questions or suggestions, please open an issue on GitHub.

## Contact

For inquiries, please reach out via GitHub issues or contact the repository owner.

---

**Note**: This system was developed as a learning project to explore data structures and their performance characteristics in information retrieval applications.
