gender = input("Enter biological gender (F/M/O): ").upper()
hemoglobin_value = float(input("Enter numerical hemoglobin value: "))
if gender == "F" and 117<=hemoglobin_value<=155:
    print("Your hemoglobin level is normal.")
elif gender == "F" and hemoglobin_value>155:
    print("Your hemoglobin level is high.")
elif gender == "F" and hemoglobin_value<155:
    print("Your hemoglobin level is low.")
elif gender == "M" and 134<=hemoglobin_value<=167:
    print("Your hemoglobin level is normal.")
elif gender == "M" and hemoglobin_value>167:
    print("Your hemoglobin level is high.")
elif gender == "M" and 134>hemoglobin_value:
    print("Your hemoglobin level is low.")
elif gender == "O":
    print("Medical guidelines and research often focus on the binary classification of male and female when it comes to hemoglobin levels. It's possible that in the future, as medical understanding evolves and becomes more inclusive, there might be more specific recommendations for individuals of other genders.\nIf you or someone you know is seeking information about hemoglobin levels in relation to a specific gender identity, it's recommended to consult with a medical professional who can provide personalized advice based on individual health and circumstances.")
else:
    print("N/A")