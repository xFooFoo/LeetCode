function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    let output: number[] = [];
    arr.forEach((num, idx) => {
        output.push(fn(num, idx))
    });
    return output;
};