type Fn<T> = () => Promise<T>

async function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {

    return new Promise((resolve, reject) => {
        const outputs: T[] = [];
        let completed = 0;
        for (let i = 0; i < functions.length; i++) {
            functions[i]()
            .then(val => {
                outputs[i] = val;
                completed++;
                if (completed === functions.length) {
                    resolve(outputs);
                }
            })
            .catch(err => reject(err));
        }
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */