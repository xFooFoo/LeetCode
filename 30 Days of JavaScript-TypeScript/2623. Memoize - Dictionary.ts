type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cachedResults = {}
    return function(...args) {
        const key: string = JSON.stringify(args);
        if (key in cachedResults) {
            return cachedResults[key];
        }
        const res: number = fn(...args)
        cachedResults[key] = res;
        return res;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */