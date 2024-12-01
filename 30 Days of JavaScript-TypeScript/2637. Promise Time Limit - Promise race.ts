type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    return async function(...args: any[]): Promise<any> {
        let timerId;
        const promiseTimeout = new Promise<any>((_, reject) => {
            timerId = setTimeout(() => {
                reject("Time Limit Exceeded")
            }, t);
        });
        return Promise.race([promiseTimeout, fn(...args)]).
        finally(() => {
            clearTimeout(timerId);
        });
    };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */