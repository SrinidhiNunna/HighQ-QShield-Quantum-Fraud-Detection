# HighQ: Quantum Kernel Learning for Mobile Money Fraud Detection

[![IBM Quantum](https://img.shields.io/badge/IBM-Quantum-blue)]()
[![Qiskit](https://img.shields.io/badge/Qiskit-QML-purple)]()
[![Python](https://img.shields.io/badge/Python-3.12-green)]()

## IBM Quantum Fall Fest 2026

**Team:** HighQ

**Track:** Financial Inclusion & Resilient Markets

---

## Problem Statement

Mobile money services are a key enabler of financial inclusion, particularly in regions where many users lack access to traditional banking infrastructure.

Fraudulent transactions reduce trust in these systems, increase financial losses, and negatively impact the adoption of digital financial services.

This project investigates whether Quantum Machine Learning (QML), specifically Quantum Support Vector Machines (QSVMs) with quantum kernels, can identify fraudulent mobile-money transactions and how their performance compares with established classical machine learning methods.

---

## Research Question

Can quantum kernel methods learn meaningful fraud patterns in mobile-money transactions while operating under current NISQ (Noisy Intermediate-Scale Quantum) hardware constraints?

---

## Dataset

### PaySim Mobile Money Dataset

Source:
https://www.kaggle.com/datasets/ealaxi/paysim1

### Dataset Statistics

| Metric | Value |
|----------|----------|
| Total Transactions | 6,362,620 |
| Fraudulent Transactions | 8,213 |
| Fraud Rate | 0.129% |

The dataset simulates realistic mobile-money transactions and is widely used for fraud detection research.

---

## Exploratory Data Analysis

### Key Findings

Fraudulent activity was concentrated almost entirely in:

- TRANSFER transactions
- CASH_OUT transactions

Fraud Rates:

| Transaction Type | Fraud Rate |
|----------|----------|
| TRANSFER | 0.7688% |
| CASH_OUT | 0.1840% |
| CASH_IN | 0% |
| PAYMENT | 0% |
| DEBIT | 0% |

### Existing Rule-Based Detection

The dataset contains a built-in fraud flag mechanism (`isFlaggedFraud`).

Results:

| Metric | Value |
|----------|----------|
| Known Fraud Cases | 8,213 |
| Fraud Cases Flagged | 16 |
| Detection Rate | 0.19% |

This observation motivated the investigation of machine learning and quantum-enhanced fraud detection approaches.

---

## Feature Engineering

The following engineered features were created to capture suspicious transaction behavior:

### Balance Consistency Features

- `balance_error_orig`
- `balance_error_dest`

### Transaction Features

- `amount`
- `amount_ratio`
- `oldbalanceOrg`
- `newbalanceOrig`
- `oldbalanceDest`
- `newbalanceDest`

### Encoded Features

- Transaction Type

---

## Classical Machine Learning Pipeline

Classical benchmark models:

- Logistic Regression
- Random Forest
- XGBoost
- Classical SVM (RBF Kernel)

### Classical Results

| Model | F1 Score |
|----------|----------|
| Random Forest | 0.9997 |
| XGBoost | 0.9994 |
| Classical SVM | 0.9058 |
| Logistic Regression | 0.9048 |

Random Forest achieved the strongest overall fraud detection performance on the engineered feature set.

---

## Quantum Machine Learning Pipeline

### Workflow

```text
PaySim Dataset
      │
      ▼
Feature Engineering
      │
      ▼
Standard Scaling
      │
      ▼
PCA (4 Components)
      │
      ▼
ZZFeatureMap
      │
      ▼
FidelityQuantumKernel
      │
      ▼
Quantum Support Vector Machine
```

### Quantum Configuration

| Component | Value |
|----------|----------|
| Quantum Algorithm | QSVM |
| Feature Map | ZZFeatureMap |
| Kernel | FidelityQuantumKernel |
| Principal Components | 4 |
| Logical Qubits | 4 |

### PCA Results

| Metric | Value |
|----------|----------|
| Original Features | 9 |
| Reduced Features | 4 |
| Variance Retained | 89.68% |

---

## QSVM Results

| Metric | Value |
|----------|----------|
| Accuracy | 0.7900 |
| Precision | 0.8625 |
| Recall | 0.6900 |
| F1 Score | 0.7667 |
| Support Vectors | 418 |

### Comparison Against Classical Models

| Model | F1 Score |
|----------|----------|
| Random Forest | 0.9997 |
| XGBoost | 0.9994 |
| Classical SVM | 0.9058 |
| Logistic Regression | 0.9048 |
| QSVM | 0.7667 |

While classical tree-based approaches achieved the highest performance, the QSVM successfully learned meaningful fraud patterns using a quantum kernel operating on a four-dimensional quantum feature space.

---

## IBM Quantum Hardware Validation

To validate hardware compatibility, the QShield quantum feature map was executed using IBM Quantum Runtime on real IBM Quantum hardware.

### Hardware Configuration

| Item | Value |
|----------|----------|
| Backend | IBM Fez |
| Feature Map | ZZFeatureMap |
| Logical Qubits | 4 |
| Circuit Depth | 128 |
| Shots | 4096 |
| Runtime Primitive | SamplerV2 |

The successful execution demonstrates that the quantum feature-encoding circuit used in the QSVM workflow can run on real IBM Quantum hardware.

---

## Project Structure

```text
HighQ/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Classical_Baselines.ipynb
│   ├── 03_QSVM.ipynb
│   ├── 04_QSVM_FAST_TEST.ipynb
│   └── 05_IBM_Quantum_Hardware_Validation.ipynb
│
├── src/
│
├── results/
│   ├── classical_results.csv
│   ├── qsvm_results.csv
│   └── final_comparison.csv
│
└── submission/
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Exploratory Data Analysis

```bash
01_EDA.ipynb
```

### Classical Machine Learning

```bash
02_Classical_Baselines.ipynb
```

### Quantum Machine Learning

```bash
03_QSVM.ipynb
```

### IBM Quantum Hardware Validation

```bash
05_IBM_Quantum_Hardware_Validation.ipynb
```

---

## Key Takeaways

- Fraud activity is concentrated within specific mobile-money transaction categories.
- Existing rule-based approaches identify only a very small fraction of fraudulent transactions.
- Classical machine learning remains highly effective for this dataset.
- Quantum kernel methods successfully learned fraud-related transaction patterns.
- Real IBM Quantum hardware execution validated deployment feasibility.
- QSVM achieved meaningful fraud-detection performance under current NISQ-era constraints.

---

## Future Work

- Larger-scale QSVM experiments
- Error mitigation techniques
- Noise-aware quantum kernels
- Hybrid quantum-classical fraud detection systems
- Execution on additional IBM Quantum backends

---

## Team

**HighQ**

IBM Quantum Fall Fest 2026

Project Title:

**QShield: Quantum Kernel Learning for Mobile Money Fraud Detection**# HighQ-QShield-Quantum-Fraud-Detection
