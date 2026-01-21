import pandas as pd                                  # Import pandas for data handling
import sys                                           # Import sys for command line arguments

class BatteryStorage:                                # Define Battery class
    def __init__(self, capacity_mwh, efficiency=0.9): # Initialize with capacity and round-trip efficiency
        self.capacity = capacity_mwh                 # Maximum storage capacity in MWh
        self.efficiency = efficiency                 # Efficiency factor (default 90%)
        self.current_soc = 0                         # Current State of Charge (SOC)
        
    def calculate_charge(self, input_energy):        # Function to calculate net energy after charging loss
        actual_stored = input_energy * self.efficiency # Actual stored energy after loss
        return actual_stored                         # Return the net stored amount

    def calculate_discharge(self, output_energy):     # Function to calculate energy needed for discharge
        needed_from_battery = output_energy / self.efficiency # Energy to extract including loss
        return needed_from_battery                   # Return total energy taken from battery

if __name__ == "__main__":                           # Script execution entry point
    # Simple test for logic validation
    bess = BatteryStorage(capacity_mwh=10, efficiency=0.85) # Create 10MWh battery with 85% efficiency
    
    test_charge = 1.0                                # Test charging 1MWh
    stored = bess.calculate_charge(test_charge)     # Calculate net storage
    print(f"Charge 1MWh -> Stored: {stored}MWh")    # Display result
    
    test_discharge = 1.0                             # Test discharging 1MWh
    taken = bess.calculate_discharge(test_discharge) # Calculate total needed
    print(f"Discharge 1MWh -> Taken: {taken}MWh")   # Display result