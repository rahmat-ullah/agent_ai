"""Script to run the Streamlit application."""

import streamlit.web.cli as stcli
import sys
from pathlib import Path

def main():
    """Run the Streamlit application."""
    root_dir = Path(__file__).parent.parent
    sys.path.append(str(root_dir))
    
    app_path = root_dir / "src" / "ai_agents_hub" / "ui" / "streamlit_app.py"
    sys.argv = ["streamlit", "run", str(app_path)]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()
