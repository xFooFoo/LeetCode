interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>
}


Array.prototype.groupBy = function(fn) {
    return this.reduce((accumulator, item) => {
        const key = fn(item)
        if (!accumulator[key]) {
            accumulator[key] = [item];
        }
        else {
            accumulator[key].push(item)
        }
        return accumulator;
    }, {})
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */