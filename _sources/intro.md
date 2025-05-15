# *Data Structures*

> Master the building blocks of computer science — from arrays to linked lists, recursion to queues.

---

## Contents Overview

A structured path through core programming concepts — from fundamentals to deeper abstractions.

| Module            | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| **1. Essentials** | Core Python syntax — variables, conditionals, loops, functions, and types.  |
| **2. Classes**    | Introduction to object-oriented programming. Build custom data structures.  |
| **3. Arrays**     | Manipulate and store sequences efficiently with lists and arrays.           |
| **4. Recursion**  | Use self-referential functions for elegant, compact solutions.              |
| **5. Linked Lists** | Go beyond arrays. Handle dynamic, non-contiguous memory elegantly.        |
| **6. Stacks**     | Master LIFO logic — from undo systems to expression evaluation.             |
| **7. Queues**     | Implement FIFO structures used in scheduling and real-time systems.         |

---

### Module Flow

```{mermaid}
flowchart LR
    %% Style des nœuds
    classDef core fill:#f9d0ff,stroke:#66337a,stroke-width:2px,color:#333,font-weight:bold;
    classDef dataStruct fill:#d0e5ff,stroke:#335599,stroke-width:2px,color:#333,font-weight:bold;
    classDef algo fill:#d0ffda,stroke:#337a44,stroke-width:2px,color:#333,font-weight:bold;

    %% Nœuds principaux
    A[Essentials]:::core
    B[Classes]:::core
    C[Arrays]:::dataStruct
    E[Linked Lists]:::dataStruct
    F[Stacks]:::dataStruct
    G[Queues]:::dataStruct
    D[Recursion]:::algo

    %% Connexions internes (inchangées)
    A --> B
    C --> E --> F
    E --> G

    %% Noeuds vides pour forcer alignement horizontal des subgraphs
    subgraph Core["Core Concepts"]
        direction TB
        A
        B
    end

    subgraph Data["Data Structures"]
        direction TB
        C
        E
        F
        G
    end

    subgraph Algo["Algorithms"]
        direction TB
        D
    end

    %% Faux liens invisibles pour aligner horizontalement les subgraphs
    Core --- Data
    Data --- Algo

    %% Style des sous-graphes
    style Core fill:#fff4f9,stroke:#ff99cc,stroke-width:1px,color:#663366,font-weight:bold
    style Data fill:#f0f8ff,stroke:#99ccff,stroke-width:1px,color:#335599,font-weight:bold
    style Algo fill:#f0fff0,stroke:#99ffcc,stroke-width:1px,color:#337a44,font-weight:bold

```

---

## Table of Contents

```{tableofcontents}
```

---

**Author**: *Dylan Barros*