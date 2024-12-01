type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    let total: number = 0;
    await promise1.then((value) => {
        total += value
    })
    await promise2.then((value) => {
        total += value
    })
    let promise: P = new Promise<number>((resolve) => {
        resolve(total);
    });
    return promise
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */