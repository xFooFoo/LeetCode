type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cachedResults = new Map()
    return function(...args) {
        const key: string = JSON.stringify(args);
        if (cachedResults.has(key)) {
            return cachedResults.get(key);
        }
        const res: number = fn(...args)
        cachedResults.set(key, res);
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