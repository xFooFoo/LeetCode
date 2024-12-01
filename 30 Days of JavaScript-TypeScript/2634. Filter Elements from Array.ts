type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    const filteredArr: number[] = []
    arr.forEach((num, idx) => {
        if (Boolean(fn(num,idx)) == true) {filteredArr.push(num)}
    })
    return filteredArr
};