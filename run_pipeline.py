import subprocess
import sys

# Note the "notebooks/" folder path here!
files_to_run = [
    "notebooks/01_ingest.ipynb",
    "notebooks/02_rag_engine.ipynb",
    "notebooks/03_app.ipynb"
]

print("Starting the RAG Pipeline...\n" + "-"*30)

for file in files_to_run:
    print(f"⏳ Running {file}...")
    
    try:
        subprocess.run([
            sys.executable, "-m", "jupyter", "nbconvert", 
            "--to", "notebook", "--execute", "--inplace", file
        ], check=True)
        
        print(f"✅ Successfully finished {file}\n")
        
    except subprocess.CalledProcessError:
        print(f"❌ Error occurred while running {file}. Stopping pipeline.")
        break
    except KeyboardInterrupt:
        print("\nPipeline stopped by user.")
        break