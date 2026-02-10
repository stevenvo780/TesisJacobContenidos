
import os
import re
import sys
import glob

def audit_case(case_dir):
    case_name = os.path.basename(case_dir)
    src_dir = os.path.join(case_dir, "src")
    
    validate_path = os.path.join(src_dir, "validate.py")
    ode_path = os.path.join(src_dir, "ode.py")
    abm_path = os.path.join(src_dir, "abm.py")
    
    issues = []
    status = "OK"
    
    if not os.path.exists(validate_path):
        return "MISSING_VALIDATE", ["validate.py missing"]
        
    with open(validate_path, "r", encoding="utf-8") as f:
        validate_content = f.read()
        
    # Check for hardcoded EDI/CR prints
    # Matches: print("... EDI=0.123 ...") or print(f"... EDI=0.123 ...")
    # Does NOT match: print(f"EDI={edi}")
    hardcoded_edi = re.findall(r'print\s*\([^)]*[\'"].*EDI\s*=\s*(\d+\.\d+)', validate_content)
    if hardcoded_edi:
        issues.append(f"Hardcoded EDI in print: {hardcoded_edi}")
        status = "SUSPICIOUS"

    # Check for run_full_validation
    if "run_full_validation" not in validate_content:
        issues.append("Missing run_full_validation call")
        status = "BROKEN"

    # Check ODE/ABM file sizes
    if os.path.exists(ode_path):
        if os.path.getsize(ode_path) < 50:
            issues.append("ode.py too small")
            status = "SUSPICIOUS"
    else:
        # common imports might mean no ode.py is needed, but usually it exists
        pass 

    if os.path.exists(abm_path):
        if os.path.getsize(abm_path) < 50:
            issues.append("abm.py too small")
            status = "SUSPICIOUS"
            
    # Check for "dummy" return in validate/make_synthetic
    # e.g., return [0.5] * steps
    if "return [0.5] * steps" in validate_content:
        issues.append("Dummy synthetic data generation")
        status = "SUSPICIOUS"

    return status, issues

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    cases = sorted(glob.glob(os.path.join(root_dir, "*_caso_*")))
    
    print(f"{'CASE':<40} | {'STATUS':<10} | {'ISSUES'}")
    print("-" * 100)
    
    results = []
    
    for case_dir in cases:
        if not os.path.isdir(case_dir):
            continue
        status, issues = audit_case(case_dir)
        case_name = os.path.basename(case_dir)
        print(f"{case_name:<40} | {status:<10} | {', '.join(issues)}")
        results.append((case_name, status, issues))

if __name__ == "__main__":
    main()
