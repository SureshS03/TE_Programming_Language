
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/src" && pwd)"

if [ -w /usr/local/bin ]; then
    ln -sf "$SCRIPT_DIR/main.py" /usr/local/bin/TE
elif [ -w /usr/bin ]; then
    ln -sf "$SCRIPT_DIR/main.py" /usr/bin/TE
else
    echo "ERROR: You need root permissions to install TE. Please run the script with sudo."
    exit 1
fi

chmod +x /usr/local/bin/TE 2>/dev/null || chmod +x /usr/bin/TE

echo "TE has been installed successfully."
