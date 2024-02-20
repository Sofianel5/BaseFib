use rand::Rng;
use num_prime::nt_funcs::next_prime;

const N_PRIMES : usize = 10;
const TESTS_PER_PRIME: i32 = 10;

fn main() {
    let mut p: u128 = 2;
    let mut gen = rand::thread_rng();
    for _ in 0..N_PRIMES {
        for _ in 1..TESTS_PER_PRIME {
            let (a,b,c) = (1, gen.gen_range(0..p), gen.gen_range(0..p));
            let mut roots = Vec::<u128>::new();
            for x in 0..p {
                let y = (a*x.pow(2) + b*x + c) % p;
                if y == 0 {
                    roots.push(x);
                }
            }
            if roots.len() == 0 {
                println!("No roots for x^2+{}x+{} mod {}", b, c, p);
            } else {
                println!("Roots for x^2+{}x+{} mod {}: {:?}", b, c, p, roots);
            }
        }
        p = next_prime(&p, None).expect("Next prime failed");
    }
}
