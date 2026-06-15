"""Run all 7 core tests"""

import subprocess
import sys

tests = [
    "test1_zero_mean.py",
    "test2_low_rank.py",
    "test3_linear_prediction.py",
    "test4_group_regression.py",
    "test5_temperature.py",
    "test6_local_gluing.py",
    "test7_holonomy.py",
]

print("=" * 70)
print("Running All Tests (1-7)")
print("=" * 70)

passed = 0
failed = 0

for test in tests:
    print(f"\n>>> Running {test}...")
    result = subprocess.run([sys.executable, test], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode == 0 and "PASS" in result.stdout:
        passed += 1
    else:
        failed += 1

print("\n" + "=" * 70)
print(f"Summary: {passed} passed, {failed} failed")
print("=" * 70)
