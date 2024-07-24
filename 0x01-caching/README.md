# Caching System Project

## Overview
This project demonstrates different caching algorithms, including FIFO, LIFO, LRU, MRU, and LFU, implemented in Python.

## Getting Started
- Ensure you have Python 3.7 installed.
- All scripts are executable and follow the `pycodestyle` style (version 2.5).

## Cache Replacement Policies

### 1. FIFO (First In, First Out)
The oldest cached item is removed first when the cache exceeds its limit.

### 2. LIFO (Last In, First Out)
The most recently cached item is removed first when the cache exceeds its limit.

### 3. LRU (Least Recently Used)
The least recently accessed item is removed first when the cache exceeds its limit.

### 4. MRU (Most Recently Used)
The most recently accessed item is removed first when the cache exceeds its limit.

### 5. LFU (Least Frequently Used)
The least frequently accessed item is removed first when the cache exceeds its limit.

## Usage
Each caching policy is implemented in a separate Python script. You can run the provided `main.py` scripts to see the caching mechanisms in action.

## Examples
Run the `main.py` scripts for each caching policy to see how they work:

```sh
./0-main.py  # BasicCache
./1-main.py  # FIFOCache
./2-main.py  # LIFOCache
./3-main.py  # LRUCache
./4-main.py  # MRUCache
./100-main.py  # LFUCache
