import re
import pprint

# Sample logs containing timestamps, severity levels, and subsystem modules in brackets
system_logs = [
    "[2026-10-27 10:15:01] [ERROR] [Module_TFT_01] Connection timeout on CAN-bus",
    "[2026-10-27 10:15:02] [INFO]  [Module_Door_02] Door closed successfully",
    "[2026-10-27 10:15:05] [ERROR] [Module_TFT_01] Packet checksum mismatch",
    "[2026-10-27 10:15:07] [WARN]  [Module_WC_01] Water level low",
    "[2026-10-27 10:15:10] [ERROR] [Module_Door_02] Obstruction detected",
    "[2026-10-27 10:15:12] [ERROR] [Module_WC_01] Valve sensor failure"
]

def extract_faulty_modules(logs):
    """
    Uses Regular Expressions (re) to extract module names from error logs
    and counts occurrences of failures per module.
    """
    # Regex pattern breakdown:
    # 1. Look for error level: \[(?:ERROR)\]
    # 2. Capture target module name inside brackets: \[([^\]]+)\]
    pattern = r"\[ERROR\]\s*\[([^\]]+)\]"
    
    error_modules = []

    for log in logs:
        match = re.search(pattern, log)
        if match:
            # Extract the group captured inside parentheses
            module_name = match.group(1)
            error_modules.append(module_name)

    # Aggregate error counts using a dictionary comprehension / loop
    error_counts = {}
    for module in error_modules:
        error_counts[module] = error_counts.get(module, 0) + 1

    return error_counts

if __name__ == "__main__":
    print("--- Running Regex Log Analysis ---\n")
    stats = extract_faulty_modules(system_logs)
    
    pprint.pprint(stats)
    print("\n[SUCCESS]: Regex parsing completed successfully.")
