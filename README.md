# ACO_ShortestPath

In this project __Ant Colony Optimization__ is used to find optimally shortest path between two points in graph with non directional edges.

### [Documentation](https://github.com/Michael-Czekanski/ACO_ShortestPath_Documentation)

## Requirements
- python 3.8 or later

---

## How to install
Clone or download this repository.

---

## How to launch
- Open terminal in project's root directory
- In terminal:\
    `python Run.py input_filename vertex_start vertex_end pheromone_influence desirability_influence evaporation_coefficent iters_num runs_num print_all_paths[y/n]`

---

## Input files

- All input files should put be in __Data/InputGraphFiles__ directory
- When launching program you just provide input file's name, program will be
looking for that file in __Data/InputGraphFiles__

#### Input files format
Input files should look like this:
```
vertexesNum = x
edgesNum = y
1. v1Ind v2Ind weight
2. v1Ind v2Ind weight
...
y. v1Ind v2Ind weight
```

---

## Output files
- Output files will be put in __Data/OutputResultFiles__ or
__Data/OutputResultFiles/ResultsWithAllPathsPrinted__, depending on
__print_all_paths__ argument.
- Output files will be named: `inputFilename_parameters`, where `parameters`
are:
  - vertex_start
  - vertex_end
  - pheromone_influence
  - desirability_influence
  - evaporation_coefficent
  - iters_num
