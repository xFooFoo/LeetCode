type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let val: number = init;
    nums.forEach((num) => {
        val = fn(val, num)
    })
    return val
};