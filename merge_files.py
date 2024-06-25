import pandas as pd

def merge_csv(files: list[str], out_file: str) -> None:
    output_df = pd.DataFrame()
    output_df = pd.concat([pd.read_csv(f) for f in files ], ignore_index=True)

    output_df.to_csv(out_file)
