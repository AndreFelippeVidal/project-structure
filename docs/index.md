# Workflow

mermaid

```mermaid 
flowchart LR
    subgraph ETL[Pipeline]
        A(Multiple Excel files) --> B[Extract: extract_from_excel]
        B[Extract: extract_from_excel] --> |Generate Dataframes list| C[Transformation: concat_dataframes]
        C[Transformation: concat_dataframes] --> |Generate concatenated Dataframe| D[Load: Convert to Excel]
        D(Load: Convert to Excel) --> |Save Excel file| E[Output folder: Unique Excel file]

    end
```
## Extract Function
### ::: project_structure.pipeline.extract.extract_from_excel

## Transform Function
### ::: project_structure.pipeline.transform.concat_dataframes

# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
