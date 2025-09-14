# ObligatoryRSA CTF Challenge Solution

## Challenge Description
**ObligatoryRSA** is a cryptography CTF challenge that provides RSA parameters and requires finding a vulnerability to solve it.

**Challenge Statement:**
> Crypto just wouldn't be crypto without one!

**Given Parameters:**
- `e = 65537` (public exponent)
- `n1` and `n2` (two RSA moduli)
- `d1` and `d2` (corresponding private exponents)

## Solution Overview

This challenge demonstrates a **Common Factor Attack** on RSA. The vulnerability occurs when two different RSA moduli share a common prime factor, which completely breaks the security of both key pairs.

### Attack Method: Common Factor Attack

1. **Identify Shared Factor**: Compute `gcd(n1, n2)` to find the common prime factor `p`
2. **Factor Both Moduli**: 
   - `q1 = n1 / p`
   - `q2 = n2 / p`
3. **Complete Factorization**: Both moduli are now completely factored
4. **Security Broken**: Can decrypt any ciphertext or forge signatures

### Mathematical Background

In RSA, security relies on the difficulty of factoring large numbers. When:
- `n1 = p × q1`
- `n2 = p × q2`

If `p` is shared between both moduli, then `gcd(n1, n2) = p`, making factorization trivial.

## Running the Solution

```bash
python3 ObligatoryRSA_solver.py
```

## Expected Output

The solver will:
1. Compute the GCD of the two moduli
2. Factor both moduli using the common factor
3. Verify the factorization
4. Display the attack results and educational information

## Key Results

- **Common Factor (p)**: `9925116240800973850976595132262541359576508947713626861810366840898037176246956650733841956083715917138800916619654906904656983178635430247237882300194413`
- **q1**: `13006651370258001672928188372391867422746978607439183348847464680178510492404973029962615378734440525453215135688732213505850572589678909644213600949540921`
- **q2**: `10917263923358559244780452437104994452390747320090210101682078886000637464304294064920553186449970174360769396946273160561865226393135471579417553316399283`

## Security Lessons

This challenge teaches several important cryptographic principles:

1. **Never Reuse Prime Factors**: Each RSA key pair must use unique, independently generated primes
2. **Proper Random Number Generation**: Prime generation must use cryptographically secure randomness
3. **Key Generation Best Practices**: RSA keys should be generated using well-tested libraries and procedures
4. **Common Vulnerabilities**: Understanding how seemingly small implementation flaws can completely break cryptographic systems

## Real-World Impact

Common factor attacks have been found in real-world scenarios:
- Embedded devices with poor random number generation
- Systems that reuse entropy sources
- Implementations with flawed prime generation algorithms

This demonstrates why cryptographic implementation must be done with extreme care and why security audits are crucial.

## Files

- `ObligatoryRSA_solver.py` - Main solution script
- `ObligatoryRSA_README.md` - This documentation file

## Educational Value

This challenge is perfect for understanding:
- RSA cryptosystem fundamentals
- Common cryptographic vulnerabilities
- The importance of proper key generation
- Mathematical attacks on cryptographic systems
- Real-world security implications of implementation flaws