from mpmath import mp

mp.dps = 100_010  # Set precision a bit higher than 100,000 digits

constants = {
    "pi": mp.pi,
    "e": mp.e,
    "phi": (1 + mp.sqrt(5)) / 2,
    "sqrt2": mp.sqrt(2)
}

def save_digits(name, value, digits=100_000):
    s = str(value)
    int_part, frac_part = s.split(".")
    frac_part = frac_part[:digits]
    output = int_part + frac_part
    lines = [output[i:i+100] for i in range(0, len(output), 100)]
    formatted_output = "\n".join(lines)
    filename = f"./data/{name}_100k_digits.txt"
    with open(filename, "w") as f:
        f.write(formatted_output)
    print(f"Saved {digits} digits of {name} to {filename}")

if __name__ == "__main__":
    for name, val in constants.items():
        save_digits(name, val)
