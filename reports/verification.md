# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 ml_impact.py sample_ml_incidents.csv
{'models': 1, 'endpoints': 2, 'affected_users': 11500, 'severity': 'sev1'}
test_rolls_up_affected_users (test_ml_impact.MLImpactTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
