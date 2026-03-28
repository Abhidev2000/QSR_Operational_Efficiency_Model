import pandas as pd
import numpy as np
import random
from datetime import timedelta

print("Reading messy Excel/CSV data to find dates...")

# 1. READ THE MESSY DATA AND EXTRACT DATES
df_orders = pd.read_csv('qsr_pos_logs.csv')

# Convert the messy date column to actual Python datetime objects. 
# Looking at your screenshot (e.g., 13/04/2025), it uses Day/Month/Year.
df_orders['transaction_datetime'] = pd.to_datetime(df_orders['transaction_datetime'], dayfirst=True)

# Instantly grab the absolute first and last dates from the data
start_date = df_orders['transaction_datetime'].min().normalize()
end_date = df_orders['transaction_datetime'].max().normalize()

print(f"Data automatically detected! Generating shifts from {start_date.date()} to {end_date.date()}...")

# 2. CREATE THE PERMANENT EMPLOYEE ROSTER
# Get the exact store IDs that actually exist in your Kaggle data
store_ids = df_orders['store_id'].unique() 
# 2. CREATE THE ROSTERS WITH FIXED WAGES
employee_records = []
for store in store_ids:
    num_employees = np.random.randint(15, 21)
    for i in range(1, num_employees + 1):
        employee_records.append({
            'store_id': store,
            'employee_id': f"EMP_{store}_{i:02d}",
            'hourly_wage': np.random.choice([11, 12.5, 14]) # Assigned ONCE per employee
        })
 
# Create a master DataFrame of all employees
df_roster = pd.DataFrame(employee_records)

# Now, rosters dictionary only needs the IDs for the random sampling later
rosters = {store: df_roster[df_roster['store_id'] == store]['employee_id'].values for store in store_ids}

# 3. GENERATE THE DAILY SCHEDULE
data = []
current_date = start_date

while current_date <= end_date:
    for store in store_ids:
        # Not everyone works every day. We randomly select 6 to 10 people from the permanent roster to work today.
        daily_staff_count = np.random.randint(6, 10)
        workers_today = random.sample(list(rosters[store]), daily_staff_count)
        
        for emp_id in workers_today:
            # Assign random shift starts between 5 AM and 4 PM
            shift_start_hour = np.random.randint(5, 16)
            clock_in = current_date + timedelta(hours=shift_start_hour, minutes=random.choice([0, 15, 30, 45]))
            
            # Shifts are 6 to 9 hours long
            clock_out = clock_in + timedelta(hours=random.randint(6, 9))
            
            data.append({
                'store_id': store,
                'business_day': current_date.strftime('%Y-%m-%d'),
                'employee_id': emp_id,  # This ID will now repeat accurately on different days!
                'clock_in_time': clock_in.strftime('%Y-%m-%d %H:%M:%S'),
                'clock_out_time': clock_out.strftime('%Y-%m-%d %H:%M:%S'),
            })
            
    # Move to the next day
    current_date += timedelta(days=1)

# 4. EXPORT THE CLEAN DATA
df_staffing = pd.DataFrame(data)
df_staffing=df_staffing.merge(df_roster[['employee_id','hourly_wage']],how='left',on='employee_id')
df_staffing.to_csv('staffing_logs.csv', index=False)
print("Staffing data generated successfully! Check your folder for 'staffing_logs.csv'.")