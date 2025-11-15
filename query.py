import sqlite3

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. SHOW ALL TESTS
    print ("ALL TESTS")
    cursor.execute('SELECT project_name, test_date, actual_strength,required_strength, passed FROM concrete_tests')
    all = cursor.fetchall()
    
    for row in all:
        name = row['project_name']
        actual = row['actual_strength']
        passed = row['passed']

        status="FAIL"
        if passed==1:
            status="PASS"
   
        print(f"{name}: {actual} PSI", status)
       
    # 2. Show ONLY failed tests
    print()
    print("FAILED TESTS")
    for row in all:
        name = row['project_name']
        date = row['test_date']
        req = row['required_strength']
        actual = row['actual_strength']
        passed = row['passed']

        if passed==0:
         print(f"{name} on {date}:\n Required: {req} PSI \n  Actual: {actual} PSI")
         print()

    print()
    print("TESTS PER PROJECT")


    # 3. Count tests by project

    


