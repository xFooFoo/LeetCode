class TimeLimitedCache {
    private dict: { [key: number]: [val: number, intervalId: NodeJS.Timeout | number] };
    private length: number;

    constructor() {
        this.dict = {}
        this.length = 0
    }
    
    set(key: number, value: number, duration: number): boolean {
        let returnBool: boolean;

        if (this.get(key) == -1) {
           returnBool = false
           this.length += 1
        } else {
            returnBool = true
            clearTimeout(this.dict[key][1]) // clearTimeout if key exists
        }


        const timerId = setTimeout(() => {
            delete this.dict[key];
            this.length -= 1
        }, duration)

        // Overwrite key with new val, timer
        this.dict[key] = [value, timerId]
    
        return returnBool
    }
    
    get(key: number): number {
        if (key in this.dict) {
            return this.dict[key][0]
        }
        return -1
    }
    
    count(): number {
        return this.length
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */