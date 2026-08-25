<div align="center">

# Coding Interview Questions

*A category-organized archive of data structure, algorithm, and system-design practice — solved in Python.*

`Python 3` · `Self-Study` · `Work in Progress`

</div>

---

## About

This repository holds solutions to coding interview problems, grouped by topic rather than by source or difficulty. The goal is a structure that mirrors how these problems actually get studied — one folder per concept, one file per problem — so revisiting a weak area later is a matter of opening a folder, not searching through history.

## Structure

```
coding-interview-questions/
├── data_structures/
│   ├── arrays_and_strings/
│   ├── linked_lists/
│   ├── stacks_and_queues/
│   ├── hash_tables/
│   ├── trees/
│   │   ├── binary_trees/
│   │   ├── binary_search_trees/
│   │   ├── tries/
│   │   └── heaps/
│   ├── graphs/
│   │   ├── adjacency_list/
│   │   └── adjacency_matrix/
│   └── advanced/
│       ├── union_find/
│       ├── segment_trees/
│       └── fenwick_trees/
│
├── algorithms/
│   ├── sorting_and_searching/
│   ├── recursion_and_backtracking/
│   ├── dynamic_programming/
│   │   ├── 1d_dp/
│   │   ├── 2d_dp/
│   │   └── knapsack_variants/
│   ├── greedy/
│   ├── divide_and_conquer/
│   ├── graph_algorithms/
│   │   ├── bfs_dfs/
│   │   ├── shortest_path/
│   │   ├── topological_sort/
│   │   └── minimum_spanning_tree/
│   └── bit_manipulation/
│
├── patterns/
│   ├── two_pointers/
│   ├── sliding_window/
│   ├── fast_slow_pointers/
│   ├── merge_intervals/
│   ├── binary_search_variants/
│   ├── matrix_traversal/
│   └── prefix_sum/
│
├── system_design_adjacent/
│   ├── object_oriented_design/
│   ├── concurrency_and_multithreading/
│   └── low_level_design/
│
├── distributed_systems/
│   ├── consistency_and_availability/
│   ├── caching_strategies/
│   ├── load_balancing/
│   ├── sharding_and_partitioning/
│   ├── message_queues/
│   └── rate_limiting/
│
├── frontend_specific/
│   ├── dom_manipulation/
│   ├── event_loop_and_async/
│   ├── state_management/
│   ├── rendering_and_reflow/
│   └── component_design/
│
├── machine_learning/
│   ├── feature_engineering/
│   ├── model_evaluation_metrics/
│   ├── data_preprocessing/
│   ├── ml_system_design/
│   └── classic_ml_coding/
│
├── testing/
│   ├── unit_test_design/
│   ├── edge_case_identification/
│   ├── test_driven_development/
│   └── mocking_and_stubbing/
│
├── math_and_logic/
│   ├── number_theory/
│   ├── combinatorics/
│   └── probability/
│
└── other/
    ├── string_manipulation/
    ├── simulation/
    └── sql_queries/
```

## Categories

| Domain | Focus | Subtopics |
|---|---|---|
| `data_structures` | Core structures and their operations | 13 |
| `algorithms` | Classic algorithmic techniques | 13 |
| `patterns` | Recurring problem-solving patterns | 7 |
| `system_design_adjacent` | Design questions bordering on architecture | 3 |
| `distributed_systems` | Concepts common in systems interviews | 6 |
| `frontend_specific` | Browser, DOM, and UI-runtime questions | 5 |
| `machine_learning` | ML fundamentals asked in coding rounds | 5 |
| `testing` | Test design and reasoning | 4 |
| `math_and_logic` | Number theory, combinatorics, probability | 3 |
| `other` | Everything else worth practicing | 3 |

## Conventions

Every problem lives in its own file, placed in the folder matching its primary topic. Each starts from the same minimal stub:

```python
"""
Category: <topic>

Solution stub for a <topic> problem.
"""


def solution(*args, **kwargs):
    raise NotImplementedError


if __name__ == "__main__":
    pass
```

A few ground rules:

- **One problem, one file.** Named for the problem itself once it's filled in (e.g. `two_sum.py`), not left as a generic `solution.py`.
- **Primary topic wins.** A problem that touches two categories goes wherever the *intended* technique lives — a DP problem solved with recursion still belongs under `dynamic_programming`.
- **Runnable by default.** The `if __name__ == "__main__":` block is for quick manual checks, not a substitute for tests.

## Usage

```bash
git clone <repo-url>
cd coding-interview-questions
python data_structures/trees/binary_trees/<problem>.py
```

No external dependencies are required unless a specific problem calls for one, in which case it's noted at the top of that file.

---

<div align="center">

*Structure over volume. Depth over speed.*

</div>
