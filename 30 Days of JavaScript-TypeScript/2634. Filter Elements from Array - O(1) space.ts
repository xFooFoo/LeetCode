type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    let filteredIdx: number = 0
    arr.forEach((num, idx) => {
        if (Boolean(fn(num,idx)) == true) {
            arr[filteredIdx++] = num
        }
    })
    arr.length = filteredIdx
    return arr
};