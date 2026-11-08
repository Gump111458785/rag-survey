# Awesome RAG Survey: Retrieval-Augmented Generation for Large Language Models

Official literature repository accompanying our comprehensive survey paper:  
**"Retrieval-Augmented Generation for Large Language Models: A Comprehensive Survey on Architectures, Benchmarks, and Future Frontiers"**

## Overview
This repository organizes the literature, architectural taxonomies, and benchmarking frameworks analyzed in the survey.

```
rag-survey/
├── taxonomy/
│   └── rag_taxonomy.json       # Paradigms (Naive, Advanced, Modular) and module definitions
├── benchmarks/
│   └── benchmarks.json         # Audited evaluation suites (RGB, MultiHop-RAG, ARES, RAGAS)
├── scripts/
│   └── verify_taxonomy.py      # Taxonomy integrity verifier
└── paper/
    ├── paper.md                # Full survey paper text (English)
    ├── paper_zh.md             # Survey paper summary (Chinese)
    └── paper7.pdf              # Compiled two-column academic survey publication
```

## Quick Verification
To verify the taxonomy categorization and benchmark suite metadata:
```bash
python scripts/verify_taxonomy.py
```

## Survey Taxonomy
- **Naive RAG**: Linear *Retrieve &rarr; Read* pipelines.
- **Advanced RAG**: Branching pre-retrieval query rewriting, hybrid dense/sparse retrieval, cross-encoder re-ranking, and context compression.
- **Modular RAG**: Dynamic, adaptive graph execution with self-reflection, multi-source orchestration, and verifiable citations.
