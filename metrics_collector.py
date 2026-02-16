#!/usr/bin/env python3
"""
Metrics Collector for SQA Project
??? ?????? ???? ????????? ???????
"""

import json
import os
from datetime import datetime

class MetricsCollector:
    def __init__(self):
        self.metrics = {
            'project_name': 'SQA-Automated-Testing',
            'evaluation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'test_metrics': {},
            'quality_metrics': {},
            'efficiency_metrics': {}
        }
    
    def collect_test_metrics(self, total_tests, passed, failed, skipped):
        """??? ?????? ????????"""
        self.metrics['test_metrics'] = {
            'total_tests': total_tests,
            'passed': passed,
            'failed': failed,
            'skipped': skipped,
            'pass_rate': f'{(passed/total_tests*100):.2f}%' if total_tests > 0 else '0%',
            'failure_rate': f'{(failed/total_tests*100):.2f}%' if total_tests > 0 else '0%'
        }
    
    def collect_coverage_metrics(self, coverage_percentage):
        """??? ?????? ???????"""
        self.metrics['quality_metrics'] = {
            'test_coverage': f'{coverage_percentage}%',
            'code_quality': 'Good' if coverage_percentage >= 80 else 'Needs Improvement'
        }
    
    def collect_efficiency_metrics(self, manual_time, automated_time):
        """??? ?????? ???????"""
        time_saved = manual_time - automated_time
        efficiency_gain = ((manual_time - automated_time) / manual_time * 100) if manual_time > 0 else 0
        
        self.metrics['efficiency_metrics'] = {
            'manual_testing_time_minutes': manual_time,
            'automated_testing_time_minutes': automated_time,
            'time_saved_minutes': time_saved,
            'efficiency_gain_percentage': f'{efficiency_gain:.2f}%',
            'roi': 'Positive' if efficiency_gain > 50 else 'Needs Improvement'
        }
    
    def save_report(self, filename='evaluation_report.json'):
        """??? ???????"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.metrics, f, indent=2, ensure_ascii=False)
        print(f'Evaluation report saved to {filename}')
    
    def print_summary(self):
        """??? ???? ????????"""
        print('\n' + '='*60)
        print('SQA PROJECT EVALUATION SUMMARY')
        print('='*60)
        
        print('\nTest Metrics:')
        for key, value in self.metrics['test_metrics'].items():
            print(f'  - {key}: {value}')
        
        print('\nQuality Metrics:')
        for key, value in self.metrics['quality_metrics'].items():
            print(f'  - {key}: {value}')
        
        print('\nEfficiency Metrics:')
        for key, value in self.metrics['efficiency_metrics'].items():
            print(f'  - {key}: {value}')
        
        print('\n' + '='*60)

if __name__ == '__main__':
    collector = MetricsCollector()
    
    collector.collect_test_metrics(
        total_tests=4,
        passed=4,
        failed=0,
        skipped=0
    )
    
    collector.collect_coverage_metrics(coverage_percentage=85.5)
    
    collector.collect_efficiency_metrics(
        manual_time=120,
        automated_time=15
    )
    
    collector.print_summary()
    collector.save_report()
