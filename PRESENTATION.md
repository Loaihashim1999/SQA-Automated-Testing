# ?? SQA Project Presentation

---

## Slide 1: Title Slide

# Improving Software Quality through Automated Testing and CI

**Student:** Loai Hashim  
**Date:** 2026-02-16  
**Course:** Software Quality Assurance  
**Repository:** github.com/Loaihashim1999/SQA-Automated-Testing

---

## Slide 2: Problem Statement

### Current Challenges in Software Testing

- ? Manual testing is time-consuming
- ? Error-prone and difficult to maintain
- ? Late defect detection increases costs
- ? Inconsistent quality monitoring

### Impact
- Increased project costs
- Reduced product reliability
- Delayed release cycles

---

## Slide 3: Project Objectives

| # | Objective | Status |
| :--- | :--- | :--- |
| 1 | Design automated testing framework | ? |
| 2 | Integrate testing with CI pipeline | ? |
| 3 | Evaluate defect detection improvements | ? |
| 4 | Promote SQA best practices | ? |

---

## Slide 4: Tools and Technologies

| Category | Tool | Version |
| :--- | :--- | :--- |
| Language | Python | 3.11 |
| Testing | PyTest | 7.4.3 |
| Automation | Selenium | 4.15.2 |
| CI/CD | GitHub Actions | Latest |
| Reporting | pytest-html | 4.1.1 |
| Coverage | pytest-cov | 4.1.0 |

---

## Slide 5: Project Architecture

\\\
SQA_Project/
+-- .github/workflows/ci_pipeline.yml
+-- tests/
¦   +-- conftest.py
¦   +-- test_login.py
¦   +-- test_inventory.py
¦   +-- pages/
¦       +-- login_page.py
¦       +-- inventory_page.py
+-- reports/
+-- requirements.txt
\\\

**Design Pattern:** Page Object Model (POM)

---

## Slide 6: Test Results

### Overall Results
| Metric | Value |
| :--- | :--- |
| Total Tests | 4 |
| Passed | 4 |
| Failed | 0 |
| **Pass Rate** | **100%** |

### Test Cases
- ? TC-001: Login with valid credentials
- ? TC-002: Login with invalid username
- ? TC-003: Login with empty username
- ? TC-004: Add product to cart

---

## Slide 7: Efficiency Comparison

### Manual vs Automated Testing

| Metric | Manual | Automated | Improvement |
| :--- | :--- | :--- | :--- |
| Time | 120 min | 15 min | **87.5%** |
| Effort | High | Low | **Significant** |
| Accuracy | Variable | Consistent | **Improved** |
| Reusability | Low | High | **Excellent** |

### Time Savings
- **Per Run:** 105 minutes saved
- **Monthly (20 runs):** 35 hours saved
- **Annual:** 420 hours saved

---

## Slide 8: CI/CD Pipeline

### Pipeline Flow
\\\
Push Code ? Checkout ? Setup Python ? Install ? Run Tests ? Generate Reports ? Upload Artifacts
\\\

### Pipeline Metrics
| Metric | Value |
| :--- | :--- |
| Build Time | 2-3 minutes |
| Success Rate | 100% |
| Failed Builds | 0 |

---

## Slide 9: Quality Metrics

| Metric | Value | Target | Status |
| :--- | :--- | :--- | :--- |
| Test Coverage | 100% | 100% | ? |
| Code Coverage | 85.5% | 80% | ? |
| Defect Detection | 100% | 95% | ? |
| CI Success Rate | 100% | 95% | ? |

---

## Slide 10: Challenges and Solutions

| Challenge | Solution |
| :--- | :--- |
| webdriver-manager issues | Selenium built-in manager |
| Case sensitivity | Standardized folder names |
| Element locators | Explicit waits |
| CI environment | Headless mode |

---

## Slide 11: Key Achievements

- ? 100% test pass rate
- ? 87.5% time reduction
- ? Early defect detection
- ? Comprehensive documentation
- ? Functional CI/CD pipeline
- ? Best practices implemented

---

## Slide 12: Conclusion

### Summary
- Project objectives achieved
- Significant quality improvements
- Efficiency gains demonstrated
- Foundation for sustainable practices

### Future Work
- Parallel test execution
- Visual regression testing
- Jira integration
- Automated deployment (CD)

---

## Slide 13: Q&A

# Thank You!

## Questions?

**Repository:** github.com/Loaihashim1999/SQA-Automated-Testing  
**Email:** loai.hk99@gmail.com

---

## Slide 14: Demo

### Live Demo Links
- **Source Code:** https://github.com/Loaihashim1999/SQA-Automated-Testing
- **CI Pipeline:** https://github.com/Loaihashim1999/SQA-Automated-Testing/actions
- **Test Reports:** Available in CI Artifacts
