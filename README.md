# EEE3097S
Design an ARM based digital IP using the Raspberry-Pi to encrypt and compress IMU data
# ARM-Based Digital IP Design for Compressing and Encrypting IMU Data

## Project Overview

This project aims to design an ARM-based digital IP using the STM32F0 microcontroller to compress and encrypt Inertial Measurement Unit (IMU) data. This data contains information about ice and wave dynamics in the southern Antarctic Ocean. The system is designed to be compatible with the ICM-20649 IMU, although testing will be performed using the ICM-20948 IMU.

## Team Members

- **Tlokomelo Nkosi**: Contributions include sections 1.1, 1.2, 1.3, 2.1.1, 2.1.3, 3.1, 3.2
- **Ashley Ratau**: Contributions include sections 1.2, 1.4, 2.1.2, 2.1.4, 2.1.5, 3.3
- **Shared Contributions**: Sections 2.2, 2.3

## Development Timeline

- **01/08/2022 - 05/08/2022**: Requirement Analysis
- **08/08/2022 - 12/08/2022**: Subsystem Design
- **15/08/2022 - 19/08/2022**: Acceptance Test Procedure
- **19/08/2022 - 22/08/2022**: Report Writing

## Project Structure

### 1. Requirement Analysis
1.1 **Interpretation of Requirements**:
- Ensure compatibility with ICM-20649.
- Extract at least 25% of Fourier coefficients from the data.
- Minimize processor computation to save power.

1.2 **Compression and Encryption Algorithms**:
- **Compression**: Utilize ZLIB, which implements the deflate algorithm.
- **Encryption**: Use AES algorithm with the Cipher Block Chaining mode.

1.3 **Feasibility Analysis**:
- Establish a timeline to meet deadlines.
- Address potential issues with STM32F0 memory and alternative solutions like Raspberry Pi Zero.

1.4 **Possible Bottlenecks**:
- Trade-offs between compression levels and processing time.
- Challenges in implementing efficient data filtering and encryption within the given constraints.

### 2. Subsystem Design
2.1 **Subsystem Requirements and Specifications**:
- **Data Compression**: Implement using ZLIB.
- **Data Encryption**: Implement using AES algorithm.
- **Data Processing and Filtering**: Extract 25% of Fourier coefficients using FFT.
- **Data Transmission**: Utilize Iridium modem for data transmission.
- **STM32F0 Usage**: Centralize data manipulation and transmission.

2.2 **Inter-Subsystem Interactions**:
- STM32F0 as the central hub for data flow and processing.

### 3. Implementation and Testing
3.1 **Coding and Integration**:
- Write and integrate code for data compression, encryption, and transmission.

3.2 **Testing and Validation**:
- Test each subsystem independently and then integrate and test the complete system.

### 4. Conclusion
4.1 **Summary**:
- Review of objectives met, challenges faced, and future improvements.

## Code and Implementation

The code for this project is organized into several modules, each corresponding to a subsystem of the design:

### 1. Compression Module
**File**: `compression.c`
```c
#include <zlib.h>

void compressData(unsigned char *input, unsigned long inputSize, unsigned char *output, unsigned long *outputSize) {
    compress(output, outputSize, input, inputSize);
}
