# Paths (adjust if needed)
OUTPUT_DIR = ./output
FLOWS_DIR = ./flows
ADDONS_DIR = ./addons
FLAGS = -w $(FLOWS_DIR)/last.mitm
MANUAL = -s $(ADDONS_DIR)/manual_dump_js.py
AUTO = -s $(ADDONS_DIR)/auto_dump_js.py

# Clean up unwanted files
clean:
		rm -rf $(OUTPUT_DIR)
		rm -rf $(ADDONS_DIR)/__pycache__
		rm -f $(FLOWS_DIR)/*

# Start mitmproxy with stable manual_dump_js.py addon
stable:
		mitmproxy $(MANUAL) $(FLAGS)

# Start mitmproxy with experimental auto_dump_js.py addon
experimental:
		mitmproxy $(AUTO) $(FLAGS)

.PHONY: clean stable experimental