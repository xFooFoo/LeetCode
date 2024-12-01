type F = (...args: number[]) => void

function debounce(fn: F, t: number): F {
    let timerId: number | NodeJS.Timeout;
    return function(...args) {
        clearTimeout(timerId)
        timerId = setTimeout(() => {fn(...args)}, t)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */