/* wave_eqn.c
 *
 * Wave-equation bijection on the L^3 cubic lattice, mod q.
 *
 * Discrete wave equation (per Substratum §3.3(b)):
 *   f(x, t+1) = [sum_{nearest neighbors} f(y, t)] - f(x, t-1)   (mod q)
 *
 * In 3D with 6 nearest neighbors, alpha=1 fixed by max-signal-speed:
 *   f(x, t+1) = (f(x+x_hat, t) + f(x-x_hat, t) + f(x+y_hat, t) + ...
 *              + f(x+z_hat, t) + f(x-z_hat, t)) - f(x, t-1)    (mod q)
 *
 * This is a bijection on (f(x,t), f(x,t-1)) state space: given new state
 * (f(x,t+1), f(x,t)), we can recover (f(x,t), f(x,t-1)) by running the
 * equation backwards using time-reversal symmetry of the wave equation.
 *
 * Time-step rule: (f_prev, f_now) -> (f_now, f_next).
 */

#include "lattice.h"

/* Apply one timestep of the wave equation to state s.
 * Returns the new state s' = phi(s).
 */
state_t wave_step(state_t s) {
    state_t s_new = 0;
    for (int z = 0; z < L; z++) {
        for (int y = 0; y < L; y++) {
            for (int x = 0; x < L; x++) {
                int i = site_idx(x, y, z);
                int f_now = get_f_now(s, i);
                int f_prev = get_f_prev(s, i);

                /* Sum nearest neighbors */
                int sum = 0;
                sum += get_f_now(s, site_idx(x+1, y, z));
                sum += get_f_now(s, site_idx(x-1, y, z));
                sum += get_f_now(s, site_idx(x, y+1, z));
                sum += get_f_now(s, site_idx(x, y-1, z));
                sum += get_f_now(s, site_idx(x, y, z+1));
                sum += get_f_now(s, site_idx(x, y, z-1));

                /* f_next = sum - f_prev (mod Q) */
                int f_next = ((sum - f_prev) % Q + Q) % Q;

                /* New state at site i: (f_next, f_now), where f_now becomes the new f_prev */
                s_new = set_f_now(s_new, i, f_next);
                s_new = set_f_prev(s_new, i, f_now);
            }
        }
    }
    return s_new;
}

/* Inverse step: phi^{-1}.
 * Reverse the wave equation: given (f_now, f_prev) at time t,
 * the previous state had (f_prev, f_prev_prev) where
 *   f_prev_prev = sum_neighbors(f_prev) - f_now   (mod Q)
 */
state_t wave_step_inverse(state_t s) {
    state_t s_old = 0;
    for (int z = 0; z < L; z++) {
        for (int y = 0; y < L; y++) {
            for (int x = 0; x < L; x++) {
                int i = site_idx(x, y, z);
                int f_now = get_f_now(s, i);
                int f_prev = get_f_prev(s, i);

                /* Sum neighbors at the PREVIOUS timestep, which is f_prev field */
                int sum = 0;
                sum += get_f_prev(s, site_idx(x+1, y, z));
                sum += get_f_prev(s, site_idx(x-1, y, z));
                sum += get_f_prev(s, site_idx(x, y+1, z));
                sum += get_f_prev(s, site_idx(x, y-1, z));
                sum += get_f_prev(s, site_idx(x, y, z+1));
                sum += get_f_prev(s, site_idx(x, y, z-1));

                int f_prev_prev = ((sum - f_now) % Q + Q) % Q;

                s_old = set_f_now(s_old, i, f_prev);
                s_old = set_f_prev(s_old, i, f_prev_prev);
            }
        }
    }
    return s_old;
}
