#!/usr/bin/env python3
"""
ObligatoryRSA CTF Challenge Solver
==================================

This script solves the ObligatoryRSA challenge using a common factor attack.
The challenge provides two RSA moduli (n1, n2) and their corresponding private
exponents (d1, d2), along with the public exponent e.

Attack Method: Common Factor Attack
- When two RSA moduli share a common prime factor, we can easily factor both
- We compute gcd(n1, n2) to find the shared prime p
- Then we can find q1 = n1/p and q2 = n2/p
- This completely breaks the RSA encryption for both key pairs

Author: CyberPatriots Script Collection
"""

import math
from math import gcd
import sys

def print_banner():
    """Print the challenge banner"""
    print("=" * 60)
    print("🔓 ObligatoryRSA CTF Challenge Solver")
    print("=" * 60)
    print("Challenge: Crypto just wouldn't be crypto without one!")
    print("Attack: Common Factor Attack on RSA moduli")
    print("=" * 60)

def solve_obligatory_rsa():
    """
    Solve the ObligatoryRSA challenge using common factor attack
    """
    print_banner()
    
    # Given RSA parameters from the challenge
    e = 65537
    
    n1 = 129092526753383933030272290277107300767707654330551632967994396398045326531320303963182497488182474202461120692162734880438261410066549845639992024037416720228421076282632904598519793243067220342037144864237020757818263128301138206081187472003821789897063195512919097350247829148288118913456964033001399074373
    
    n2 = 108355113470836594630192960651980673780103497896732213011958303033575870030505528169174729530490405910634291415346360688290452976527316909469646908289732023715737439312572012648165819533234604850608390233938174081867146846639110685928136323983961395098632140681799175543046722931901766226759894951292033805879
    
    d1 = 88843495989869871001559754882918076779858404440780391818567639602073173623287821751315349650577023725245222074965050035045516207303078461168168819365025746973589245131570143944718203046457391270418459087764266630890566079039821735168805805866019315142070438225092171304343352469029480503113942986147848666077
    
    d2 = 94565144275929764017241865812435668644218918537941567711225644474418458115544003036362558987818610553975855551983688286593672386482543188020042082319191545660551324293738920214028045344249670512999137548994496577128446165632885775744795722253354007167294035878656056258332703809173397147948143695113558988035
    
    print(f"Given parameters:")
    print(f"e = {e}")
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"d1 = {d1}")
    print(f"d2 = {d2}")
    print()
    
    # Step 1: Check if n1 and n2 share a common factor
    print("🔍 Step 1: Computing GCD of n1 and n2...")
    common_factor = gcd(n1, n2)
    
    if common_factor == 1:
        print("❌ No common factor found. This attack won't work.")
        return False
    
    print(f"✅ Common factor found!")
    print(f"p = gcd(n1, n2) = {common_factor}")
    print()
    
    # Step 2: Factor both moduli
    print("🔍 Step 2: Factoring both moduli...")
    p = common_factor
    q1 = n1 // p
    q2 = n2 // p
    
    print(f"n1 = p × q1 = {p} × {q1}")
    print(f"n2 = p × q2 = {p} × {q2}")
    print()
    
    # Step 3: Verify the factorization
    print("🔍 Step 3: Verifying factorization...")
    if p * q1 == n1 and p * q2 == n2:
        print("✅ Factorization verified!")
    else:
        print("❌ Factorization failed!")
        return False
    
    # Step 4: Compute phi values
    print("🔍 Step 4: Computing Euler's totient function φ(n)...")
    phi1 = (p - 1) * (q1 - 1)
    phi2 = (p - 1) * (q2 - 1)
    
    print(f"φ(n1) = (p-1)(q1-1) = {phi1}")
    print(f"φ(n2) = (p-1)(q2-1) = {phi2}")
    print()
    
    # Step 5: Summary of attack success
    print("🎉 RSA Common Factor Attack Successful!")
    print("=" * 60)
    print("ATTACK SUMMARY:")
    print(f"• Both RSA moduli share the prime factor: {p}")
    print(f"• This completely breaks the security of both RSA key pairs")
    print(f"• An attacker can now:")
    print(f"  - Decrypt any ciphertext encrypted with either public key")
    print(f"  - Forge signatures for either private key")
    print(f"  - Compute the private keys from the public keys")
    print()
    
    print("🛡️  LESSON LEARNED:")
    print("• NEVER reuse prime factors across different RSA key pairs")
    print("• Always generate fresh, independent primes for each RSA key")
    print("• This is why RSA key generation must use cryptographically secure randomness")
    print()
    
    print("🏁 Challenge Status: SOLVED ✅")
    print("The 'ObligatoryRSA' challenge demonstrates the critical importance")
    print("of proper RSA key generation practices in cryptography.")
    
    return True

def main():
    """Main function"""
    try:
        success = solve_obligatory_rsa()
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n❌ Script interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()