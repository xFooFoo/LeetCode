interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>
}


Array.prototype.groupBy = function(fn) {
    const dict = {};
    for (const item of this) {
        const key = fn(item);
        if (!dict[key]) {
            dict[key] = [];
        }
        dict[key].push(item);
    }
    return dict;
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */