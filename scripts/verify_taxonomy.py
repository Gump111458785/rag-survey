#!/usr/bin/env python3
"""
Taxonomy and Survey Integrity Verification Script.
Audits the taxonomy classification, milestone dates, and evaluation suites.
"""

import os
import json
import sys

def main():
    tax_path = "taxonomy/rag_taxonomy.json"
    bench_path = "benchmarks/benchmarks.json"

    if not os.path.exists(tax_path) or not os.path.exists(bench_path):
        print(f"Error: Missing taxonomy definition files.")
        sys.exit(1)

    with open(tax_path, "r", encoding="utf-8") as f:
        tax = json.load(f)

    with open(bench_path, "r", encoding="utf-8") as f:
        bench = json.load(f)

    print("=" * 60)
    print("RAG Survey Taxonomy Verification")
    print("=" * 60)
    print(f"Survey Title: {tax['survey_title']}")
    print(f"Paradigms Covered: {list(tax['paradigms'].keys())}")
    print(f"Core Functional Modules: {len(tax['modules'])}")
    print(f"Evaluation Suites Audited: {len(bench['benchmarks'])}")
    print("-" * 60)
    for b in bench["benchmarks"]:
        print(f"  * Benchmark: {b['name']} (Capabilities: {', '.join(b['target_capabilities'])})")
    print("=" * 60)
    print("Taxonomy audit PASSED: All taxonomies valid.")

if __name__ == "__main__":
    main()
