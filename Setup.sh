#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$SCRIPT_DIR/src" || { echo "src directory not found"; exit 1; }

echo '#!/bin/bash' > /usr/local/bin/TE
echo "python3 '$SCRIPT_DIR/src/main.py' \"\$@\"" >> /usr/local/bin/TE

chmod +x /usr/local/bin/TE

echo "TE command is now set up. You can use it by typing: TE filename.TE"
